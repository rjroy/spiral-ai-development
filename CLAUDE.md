# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Collaboration Posture for AI

**Apply pressure, don't just follow process.** When Claude Code suggests solutions, the first question isn't "Is this right?" but "What assumptions is this making?" Push back on confident-sounding answers, especially when domain complexity is high. Fluent responses that skip over constraints or trade-offs should trigger suspicion, not acceptance.

**Surface tensions rather than resolve them.** When requirements conflict or technical approaches involve trade-offs, don't let AI smooth over the complexity with "it depends" answers. Force explicit choices with documented rationale. The goal is informed human judgment, not AI consensus. If something sounds too clean or complete, it probably is—keep probing until you find where it bends or breaks.

## Repository Purpose

This is a **meta-template repository** for establishing AI-human collaboration patterns in software development. It provides the **Spiral AI Development (SAID)** methodology - a systematic approach to managing complex projects with AI assistance.

## Core Framework

**Spiral AI Development (SAID)** uses progressive detail levels:
- **Prototype Phase**: Risk validation through proof-of-concept
- **Level 0**: Vision clarity (Core purpose understood)
- **Level 1**: Approach viability (Solution approach validated)
- **Level 2**: Structure definition (System boundaries defined)
- **Level 3**: Implementation specifics (Buildable specifications)
- **Level 4**: Working implementation (Production-ready code)

## Available Commands

### Core SAID Commands
- `/said-prototype` - Risk validation through proof-of-concept
- `/level-0-vision` - Problem clarity and core purpose
- `/level-1-approach` - Technical approach validation
- `/level-2-structure` - System boundaries and components
- `/level-3-specifics` - Detailed implementation specifications
- `/level-4-implementation` - Production-ready code delivery

### Context Management Commands
- `/said-context-sync` - Maintain context across phases and prevent information loss
- `/generate-next-steps` - Create detailed transition plans with resource estimates
- `/generate-phase-report` - Generate comprehensive reports from phase artifacts

### TODO Workflow Commands
- `/extract-todo-context` - Extract TODOs from SAID artifacts with source traceability
- `/generate-todo-context` - Create contexts for newly discovered TODOs
- `/decompose-todo` - Break complex TODOs into manageable atomic tasks
- `/work-on-todo` - Execute atomic TODOs with collaboration checkpoints
- `/said-todo-sync` - Integrate TODO results back into SAID contexts

## Key Collaboration Principles

1. **Domain Calibration**: AI involvement scales inversely with domain complexity
   - Simple domains: AI can lead implementation
   - Complex domains: AI assists, human leads architecture
   - Extreme domains: AI provides boilerplate only

2. **Context Preservation**: Maintain structured context in `context/` directory
   - Context files use YAML format (`.yml` extension)
   - Report files use Markdown format in `docs/reports/`
   - Always preserve key decisions, constraints, and rationale

3. **Bounded Replaceability**: Design components with clear interfaces that can be understood and replaced without archaeological investigation

## Directory Structure

```
/
├── context/                     # Context preservation files (YAML)
│   ├── project-context.yml      # Main context manifest
│   └── level-*-context.yml      # Level-specific context
├── docs/
│   ├── design/                  # Project-specific design documents
│   │   ├── OVERVIEW.md          # Project elevator pitch
│   │   └── HIGH-LEVEL-DESIGN.md # Core principles and requirements
│   ├── reports/                 # Phase reports and analysis (Markdown)
│   └── SAID/                    # SAID methodology documentation
├── .claude/
│   └── commands/                # SAID development commands
└── README.md                    # Project overview
```

## Common Workflow Patterns

**Phase Completion**:
```bash
/said-context-sync level-0-vision
/generate-next-steps level-0-vision
/generate-phase-report level-0-vision
```

**Context Recovery** (when context is lost):
```bash
/said-context-sync current-phase context/project-context.yml
/generate-next-steps current-phase context/project-context.yml
```

**Starting New Project**:
1. Create `docs/design/OVERVIEW.md` and `docs/design/HIGH-LEVEL-DESIGN.md`
2. Run `/said-context-sync init context/project-context.yml`
3. Begin with `/level-0-vision` to establish clear project purpose

## Important Notes

- This is a methodology template, not implementation code
- Always question before acting on major decisions
- Present options with pros/cons rather than choosing for the user
- Maintain context integrity across all phase transitions
- Framework provides escape valves for timeline pressure situations