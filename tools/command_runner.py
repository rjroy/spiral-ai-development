#!/usr/bin/env python3
"""Run SAID command files with pattern loading and LLM invocation.

This utility reads a command definition file (e.g. ``.claude/commands/analyze.md``),
loads any referenced pattern files from ``.agent/``, constructs a final prompt and
sends it to a configured LLM provider. The provider can be configured through
standard environment variables for Anthropic or OpenAI.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Dict, List, Tuple


Pattern = Tuple[str, str]


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
    parser = argparse.ArgumentParser(description="Run a SAID command file")
    parser.add_argument("command_file", help="Path to command markdown file")
    parser.add_argument(
        "params",
        nargs=argparse.REMAINDER,
        help="Parameters for the command (e.g. --focus problems)",
    )
    args = parser.parse_args(argv)

    try:
        with open(args.command_file, "r", encoding="utf-8") as f:
            command_text = f.read()
    except OSError as exc:
        print(f"Error reading command file: {exc}", file=sys.stderr)
        return 1

    try:
        patterns = load_patterns(command_text)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    params = parse_params(args.params)
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
