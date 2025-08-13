# Spiral AI Development Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Template](https://img.shields.io/badge/GitHub-Template-6e5494.svg)](https://github.com/rjroy/claude-code-template/generate)
[![Claude Code](https://img.shields.io/badge/AI_Partner-Claude_Code-D97757.svg)](https://claude.ai/code)

[![Template Version](https://img.shields.io/badge/Version-v2.1.3-blue.svg)](https://github.com/rjroy/claude-code-template)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)](https://github.com/rjroy/claude-code-template/commits/main)
[![SAID](https://img.shields.io/badge/Methodology-SAID-16A34A.svg)](docs/SAID/philosophy)


A meta-template for establishing AI-human collaboration patterns in software development. SAID addresses the collaboration paradox: AI excels at quick solutions for well-understood domains, but complex problems require progressive understanding to avoid incomplete solutions that miss critical constraints.

## Core Framework

<img src="docs/SAID/logos/said-64.png" align="right" style="margin-left: 10px">

**Spiral AI Development (SAID)** - A methodology for AI-human collaboration that navigates uncertainty through progressive certainty. Rather than linear phases, SAID uses thresholds of understanding to make decisions only when you have sufficient information.

**The Collaboration Paradox** - AI provides fluent, complete-looking solutions that often miss critical constraints. This creates false confidence - solutions that "look right" but fail when tested against reality. SAID addresses this through iterative deepening: identifying and resolving nuances before implementation, not after.

## Key Components

- **Context as Navigation Aid** - Context files are maps through the spiral, not just documentation. SAID addresses four context problems: poisoning (errors repeated), distraction (overwhelm), confusion (too many options), and clash (contradictions).

- **Progressive Detail Levels** - Make decisions only at appropriate thresholds:
  - **Level 0**: Problem + Risk Clarity
  - **Level 1**: Approach Viability
  - **Level 2**: Structure Definition
  - **Level 3**: Implementation Specifics
  - **Level 4**: Working Implementation

- **Ownership Architecture** - Clear boundaries between human judgment (strategy, trade-offs), AI assistance (research, implementation), and shared territory (review, testing).

- **High-Performing Intern Pattern** - Commands behave like skilled interns: adaptive checkpoints over rigid templates, bounded initiative, context-aware depth, and efficient question bundling.

- **Bounded Replaceability** - Design components so any piece can be understood and replaced without archaeological investigation. The Investigation-Decision-Integration pattern provides the natural workflow rhythm.

## Getting Started

This is a GitHub template repository.  Getting started is as simple as creating a repository using this as a template.

Actually, the first step is to have an idea. Be bold. Be vague. Be inspired. Whatever it is, write it down.

- **OVERVIEW.md**: A short description for the project. The elevator pitch.
- **HIGH-LEVEL-DESIGN.md**: A description of all the key core principles and requirements that are necessary to consider the project successful. This is not a detailed design, but does set up the next steps. Don't worry, you can refine it through the process.

Please follow the [Getting Started](/docs/SAID/getting-started/README.md) complete guide.

## Using commands without Claude Code

SAID commands live in `.claude/commands/` and can be executed from a terminal using a CLI runner.

### Setup

1. Install the runner (example with npm):
   ```bash
   npm install -g said-cli
   ```
2. Provide an API key for your model provider:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   # or
   export OPENAI_API_KEY="sk-openai-..."
   ```
   Additional variables such as `OPENROUTER_API_KEY` may be used depending on your provider.

### Example usage

Pass any SAID command string to the runner:

```bash
# Analyze problems for a project context
said-cli "/analyze problems context/project-context.md"

# Synchronize a report into context
said-cli "/sync-context docs/reports/problem-validation.md"

# Record a decision from an analysis report
said-cli "/sync-decision context/project/decisions.md docs/reports/solutions-analysis.md 1"
```

These examples mirror the commands documented in [HOW-TO](docs/SAID/getting-started/HOW-TO.md).

## Further Reading

- Philosophy: [Core Concepts](/docs/SAID/philosophy/core-concepts.md)
- Philosophy: [Implementation Guide](/docs/SAID/philosophy/implementation-guide.md)
- Philosophy: [Command Design Principles](/docs/SAID/philosophy/command-design-principles.md)
- Philosophy: [Version](/docs/SAID/philosophy/version.md)
- Getting Started: [README](/docs/SAID/getting-started/README.md)
- Getting Started: [How-To](/docs/SAID/getting-started/HOW-TO.md)
- Add Ons: [Context Priming Pattern](/docs/SAID/add-ons/context-priming-pattern.md)
- Add Ons: [Git Hook Testing](/docs/SAID/add-ons/git-hook-testing-integration.md)

