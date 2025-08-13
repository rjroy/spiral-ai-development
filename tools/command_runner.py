#!/usr/bin/env python3
"""Run SAID commands using front-matter metadata.

This utility locates command files in ``.claude/commands/`` via the ``name`` field
in their YAML front-matter, loads any referenced pattern files from ``.agent/``,
constructs a final prompt, and sends it to a configured LLM provider. The provider
can be configured through standard environment variables for Anthropic or OpenAI.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Dict, List, Tuple



Pattern = Tuple[str, str]


def parse_command_file(path: str) -> Tuple[Dict, str]:
    """Load front matter and content from a command file."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        raise RuntimeError(f"Command file {path} missing front matter")
    front_text = match.group(1)
    content = match.group(2)
    front: Dict = {}
    current_item: Dict | None = None
    for line in front_text.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - "):
            current_item = {}
            front.setdefault("parameters", []).append(current_item)
            line = line[4:]
            key, value = line.split(":", 1)
            current_item[key.strip()] = value.strip()
        elif line.startswith("    ") and current_item is not None:
            key, value = line.strip().split(":", 1)
            current_item[key.strip()] = value.strip()
        else:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key == "parameters" and value == "":
                front[key] = []
            else:
                front[key] = value
            current_item = None
    if isinstance(front.get("parameters"), str):
        if front["parameters"].strip() == "[]":
            front["parameters"] = []
    # convert optional flags to booleans
    for item in front.get("parameters", []):
        if "optional" in item:
            item["optional"] = item["optional"].lower() == "true"
    return front, content


def render_template(content: str, front: Dict) -> str:
    """Replace placeholders with front matter values."""
    def format_parameters(params: List[Dict]) -> str:
        if not params:
            return "None"
        lines = []
        for p in params:
            line = f"- `{p['name']}`: {p.get('description', '')}"
            if p.get("optional"):
                line += " (optional)"
            lines.append(line)
        return "\n".join(lines)

    replacements = {
        "name": front.get("name", ""),
        "description": front.get("description", ""),
        "parameters": format_parameters(front.get("parameters", [])),
    }
    for key, value in replacements.items():
        content = content.replace(f"{{{{{key}}}}}", value)
    return content


def load_command_by_name(name: str) -> Tuple[str, Dict, str]:
    """Find command file by name and return its path, front matter, and content."""
    base_dir = os.path.join(os.getcwd(), ".claude", "commands")
    available: List[str] = []
    for fname in os.listdir(base_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(base_dir, fname)
        front, content = parse_command_file(path)
        cmd_name = front.get("name")
        if cmd_name:
            if cmd_name == name:
                return path, front, content
            available.append(cmd_name)
    raise RuntimeError(
        f"Unknown command '{name}'. Available commands: {', '.join(sorted(available))}"
    )


def parse_params(param_list: List[str]) -> Dict[str, str]:
    """Convert CLI parameters into a dictionary.

    Supports ``--key value`` and ``--key=value`` forms.
    """
    params: Dict[str, str] = {}
    key: str | None = None
    for item in param_list:
        if item.startswith("--"):
            if "=" in item:
                k, v = item[2:].split("=", 1)
                params[k] = v
                key = None
            else:
                key = item[2:]
        else:
            if key:
                params[key] = item
                key = None
    return params


def load_patterns(command_text: str) -> List[Pattern]:
    """Extract and load pattern files referenced in the command text."""
    pattern_paths = re.findall(r"Load:\s*`([^`]+)`", command_text)
    patterns: List[Pattern] = []
    for path in pattern_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                patterns.append((path, f.read()))
        except OSError as exc:  # pragma: no cover - simple CLI tool
            raise RuntimeError(f"Failed to load pattern file {path}: {exc}")
    return patterns


def build_prompt(command_text: str, patterns: List[Pattern], params: Dict[str, str]) -> str:
    """Combine pattern contents, command text, and parameters into the final prompt."""
    parts: List[str] = []
    for path, content in patterns:
        parts.append(f"# Pattern: {path}\n{content.strip()}")
    parts.append(command_text.strip())
    if params:
        parts.append("# Parameters\n" + json.dumps(params, indent=2))
    return "\n\n".join(parts)


def send_prompt(prompt: str) -> str:
    """Send the prompt to a configured LLM provider and return the response text."""
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            import anthropic  # type: ignore
        except Exception as exc:  # pragma: no cover - runtime dependency
            raise RuntimeError(f"Anthropic SDK not available: {exc}")
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        model = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
        response = client.messages.create(
            model=model,
            max_tokens=int(os.getenv("ANTHROPIC_MAX_TOKENS", "1000")),
            messages=[{"role": "user", "content": prompt}],
        )
        # anthropic v1 returns response.content as a list
        return "".join(block.text for block in response.content if block.type == "text")

    if os.getenv("OPENAI_API_KEY"):
        try:
            from openai import OpenAI  # type: ignore
        except Exception as exc:  # pragma: no cover - runtime dependency
            raise RuntimeError(f"OpenAI SDK not available: {exc}")
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message["content"]

    raise RuntimeError("No LLM provider configured")


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a SAID command")
    parser.add_argument("command", help="Command name to run")
    parser.add_argument(
        "params",
        nargs=argparse.REMAINDER,
        help="Parameters for the command (e.g. --focus problems)",
    )
    args = parser.parse_args(argv)
    try:
        _, front, content = load_command_by_name(args.command)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    command_text = render_template(content, front)

    try:
        patterns = load_patterns(command_text)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    params = parse_params(args.params)
    defined = {p["name"]: p for p in front.get("parameters", [])}
    missing = [n for n, p in defined.items() if not p.get("optional") and n not in params]
    unknown = [k for k in params if k not in defined]
    if missing:
        print(f"Missing parameters: {', '.join(missing)}", file=sys.stderr)
        return 1
    if unknown:
        print(f"Unknown parameters: {', '.join(unknown)}", file=sys.stderr)
        return 1

    prompt = build_prompt(command_text, patterns, params)

    try:
        result = send_prompt(prompt)
    except Exception as exc:
        print(f"LLM request failed: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
