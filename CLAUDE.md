# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Collaboration Posture for AI

**Apply pressure, don't just follow process.** When Claude Code suggests solutions, the first question isn't "Is this right?" but "What assumptions is this making?" Push back on confident-sounding answers, especially when domain complexity is high. Fluent responses that skip over constraints or trade-offs should trigger suspicion, not acceptance.

**Surface tensions rather than resolve them.** When requirements conflict or technical approaches involve trade-offs, don't let AI smooth over the complexity with "it depends" answers. Force explicit choices with documented rationale. The goal is informed human judgment, not AI consensus. If something sounds too clean or complete, it probably is—keep probing until you find where it bends or breaks.

## Repository Purpose

This is a **meta-template repository** for establishing AI-human collaboration patterns in software development. It provides the **Spiral AI Development (SAID)** methodology - a systematic approach to managing complex projects with AI assistance.

## Core Framework

**Spiral AI Development (SAID)** uses task-focused workflows achieving progressive detail levels:
- **Level 0**: Vision clarity through `/analyze-problem` and `/analyze-risks`
- **Level 1**: Approach viability through `/analyze-options` and `/sync-decision`
- **Level 2+**: Progressive decomposition using `/decompose` with type definitions:
  - Project-level: `/decompose context/types/project.md`
  - Component-level: `/decompose context/types/component.md`
  - Feature-level: `/decompose context/types/feature.md`
  - TODO execution: `/decompose context/types/todo.md` → `/work-on-todo`

## Available Commands

### Analysis Commands
- `/analyze-problem` - Validate and clarify problem understanding
- `/analyze-options` - Present solution options with trade-offs
- `/analyze-risks` - Identify and analyze project risks

### Context Management Commands
- `/sync-decision` - Integrate decisions into context with rationale
- `/sync-context` - Maintain context across phases and prevent information loss

### Decomposition Commands
- `/decompose` - Universal decomposition using type definitions (project/component/feature/todo)

### Planning Commands
- `/plan-next-steps` - Create detailed transition plans with resource estimates

### TODO Workflow Commands
- `/create-todo` - Create contexts for newly discovered TODOs
- `/create-todo-from-report` - Extract TODOs from analysis reports
- `/work-on-todo` - Execute atomic TODOs with collaboration checkpoints

## Key Collaboration Principles

1. **Domain Calibration**: AI involvement scales inversely with domain complexity
   - Simple domains: AI can lead implementation
   - Complex domains: AI assists, human leads architecture
   - Extreme domains: AI provides boilerplate only

2. **Context Preservation**: Maintain structured context using three-file system
   - `context/project-context.md` - Main context manifest with current state
   - `context/project/decisions-made.md` - Key decisions with rationale and traceability
   - `context/project/open-questions.md` - Unresolved questions requiring multi-phased analysis
   - `context/project/lessons-learned.md` - Insights and patterns discovered
   - Context templates in `context/templates/` for initialization
   - Type definitions in `context/types/` for decomposition guidance

3. **Bounded Replaceability**: Design components with clear interfaces that can be understood and replaced without archaeological investigation

4. **Git-Hook Testing Integration**: Define testing automation strategies early to prevent massive failures
   - Level 2: Component testing boundaries and responsibilities
   - Level 3: Comprehensive git-hook testing strategy (primary integration point)
   - Level 4: Git-hook implementation and team onboarding
   - See `docs/SAID/add-ons/git-hook-testing-integration.md` for detailed guidance

## Directory Structure

```
/
├── context/                     # Context preservation files (Markdown)
│   ├── project-context.md       # Main context manifest
│   ├── templates/               # Context initialization templates
│   ├── types/                   # Decomposition type definitions
│   │   ├── project.md           # Project decomposition type
│   │   ├── component.md         # Component decomposition type
│   │   ├── feature.md           # Feature decomposition type
│   │   └── todo.md              # TODO decomposition type
│   └── project/                 # Project-specific context files
│       ├── decisions-made.md    # Key decisions with rationale
│       ├── open-questions.md    # Unresolved questions
│       └── lessons-learned.md   # Insights and patterns
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

**Level 0 (Vision Clarity)**:
```bash
/analyze-problem
/analyze-risks
/sync-context
```

**Level 1 (Approach Viability)**:
```bash
/analyze-options
/sync-decision
/sync-context
```

**Level 2+ (Progressive Decomposition)**:
```bash
/decompose context/types/project.md [parent-context]
/decompose context/types/component.md [parent-context]
/decompose context/types/feature.md [parent-context]
```

**Context Recovery** (when context is lost):
```bash
/sync-context [source-file]
/plan-next-steps
```

**Starting New Project**:
1. Create `docs/design/OVERVIEW.md` and `docs/design/HIGH-LEVEL-DESIGN.md`
2. Run `/sync-context init`
3. Begin with `/analyze-problem` to establish clear problem understanding

## Important Notes

- This is a methodology template, not implementation code
- Always question before acting on major decisions
- Present options with pros/cons rather than choosing for the user
- Maintain context integrity across all phase transitions
- Framework provides escape valves for timeline pressure situations