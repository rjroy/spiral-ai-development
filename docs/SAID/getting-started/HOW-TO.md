# SAID Commands HOW-TO Guide

This guide provides practical usage instructions for all Spiral AI Development (SAID) commands. Each command entry includes syntax, arguments, purpose, usage timing, and examples.

## Table of Contents

- [Analysis Commands](#analysis-commands)
  - [/analyze](#analyze)
- [Context Management Commands](#context-management-commands)
  - [/sync-context](#sync-context)
  - [/sync-decision](#sync-decision)
  - [/prime-context](#prime-context)
- [Decomposition Commands](#decomposition-commands)
  - [/decompose](#decompose)
- [Planning Commands](#planning-commands)
  - [/plan-next-steps](#plan-next-steps)
- [TODO Workflow Commands](#todo-workflow-commands)
  - [/create-todo](#create-todo)
  - [/create-todo-from-report](#create-todo-from-report)
  - [/work-on-todo](#work-on-todo)

---

## Analysis Commands

### /analyze

**Command**: `/analyze <focus> <input-description> [--roles=<role1,role2,...>]`

**Arguments**:
- `<focus>`: Type of analysis to perform
  - Available focuses found in `.agent/focus/`: `problems`, `risks`, `solutions`
- `<input-description>`: Topic or context to analyze
- `[--roles]`: Optional comma-separated list of stakeholder perspectives
  - Available roles found in `.agent/roles/`: `developer`, `architect`, `tester`, `user`, `product-owner`, etc.

**Purpose**: Identify and analyze contexts based on specific focus areas with role-based expertise integration. Performs industry research and generates comprehensive reports.

**Why Use**: To gain structured insights into problems, identify risks, or evaluate solution options with multiple stakeholder perspectives.

**When to Use**:
- **Level 0**: Use with `problems` or `risks` focus for vision clarity
- **Level 1**: Use with `solutions` focus for approach viability

**Example**:
```bash
/analyze problems "User authentication system showing performance degradation under load"
/analyze risks "Migrating monolithic application to microservices architecture"
/analyze solutions "Implementing real-time collaboration features" --roles=developer,architect,user
```

---

## Context Management Commands

### /sync-context

**Command**: `/sync-context <any-file>` or `/sync-context init`

**Arguments**:
- `<any-file>`: Path to any file containing information to integrate
- `init`: Special argument to initialize project context from templates

**Purpose**: Extract and intelligently integrate critical information from any file into the project's core context files, maintaining context integrity across all development phases.

**Why Use**: To preserve important information, decisions, and insights without manual copying, ensuring nothing is lost during phase transitions.

**When to Use**:
- **All Levels**: After any significant analysis, decision, or discovery
- **Project Start**: Use `init` to set up context structure from templates

**Example**:
```bash
/sync-context init
/sync-context docs/reports/risks-security-20241215-143022.md
/sync-context meeting-notes.txt
```

### /sync-decision

**Command**: `/sync-decision <context-file> <decision-report> <selected-option>`

**Arguments**:
- `<context-file>`: Target context file (usually `context/project/decisions-made.md`)
- `<decision-report>`: Report file containing the analysis and options
- `<selected-option>`: The option number or identifier selected by the user

**Purpose**: Formally integrate a selected decision from an analysis report into the project's decision history with full traceability and rationale.

**Why Use**: To maintain a clear decision audit trail with context, alternatives considered, and rationale for future reference.

**When to Use**:
- **Level 1+**: After analyzing options and selecting an approach
- **Any Level**: When making consequential project decisions

**Example**:
```bash
/sync-decision context/project/decisions-made.md docs/reports/solutions-auth-20241215-150000.md 2
/sync-decision context/project/decisions-made.md analysis-report.md "Option A"
```

### /prime-context

**Command**: `/prime-context`

**Arguments**: None

**Purpose**: Update CLAUDE.md with a concise summary of current project context from the four context files, enabling immediate AI orientation without requiring separate context review.

**Why Use**: To quickly restore working context for AI assistants after breaks or when starting new sessions, ensuring continuity and reducing repeated discovery.

**When to Use**:
- **All Levels**: At the start of new AI sessions
- After significant context updates
- When returning to work after breaks
- As part of context recovery workflow

**Example**:
```bash
/prime-context
```

---

## Decomposition Commands

### /decompose

**Command**: `/decompose <type-definition-file> <context-file>`

**Arguments**:
- `<type-definition-file>`: Path to decomposition type definition
  - Available types in `.agent/layers/`:
    - `project.md` - High-level project breakdown
    - `component.md` - System component analysis
    - `feature.md` - Feature-level decomposition
    - `todo.md` - Atomic task decomposition
- `<context-file>`: Source context to decompose (project context, component spec, etc.)

**Purpose**: Execute type-specific decomposition using configurable definitions, breaking down complex contexts into manageable pieces based on the selected type.

**Why Use**: To systematically break down large problems into smaller, actionable pieces while maintaining relationships and dependencies.

**When to Use**:
- **Level 2+**: Progressive decomposition phases
- Use `project.md` for initial breakdown
- Use `component.md` for system design
- Use `feature.md` for feature planning
- Use `todo.md` for task-level breakdown

**Example**:
```bash
/decompose .agent/layers/project.md context/project-context.md
/decompose .agent/layers/component.md context/components/auth-service.md
/decompose .agent/layers/feature.md context/features/user-registration.md
/decompose .agent/layers/todo.md context/todos/implement-jwt-tokens.md
```

---

## Planning Commands

### /plan-next-steps

**Command**: `/plan-next-steps <current-phase> [context-file]`

**Arguments**:
- `<current-phase>`: Description of the current project phase or state
- `[context-file]`: Optional path to specific context file (defaults to main project context)

**Purpose**: Generate detailed transition plans with prioritized actions, resource estimates, and risk mitigation strategies for moving to the next phase.

**Why Use**: To create clear, actionable plans when transitioning between phases or when unsure about next steps.

**When to Use**:
- **All Levels**: At phase transitions
- When context is recovered after interruption
- When planning major transitions

**Example**:
```bash
/plan-next-steps "Completed initial problem analysis"
/plan-next-steps "Finished component design" context/components/payment-service.md
/plan-next-steps "Ready for implementation phase"
```

---

## TODO Workflow Commands

### /create-todo

**Command**: `/create-todo <todo-description>`

**Arguments**:
- `<todo-description>`: Clear description of the task or work item

**Purpose**: Transform a TODO description into a structured context suitable for SAID integration, with clear boundaries and success criteria.

**Why Use**: To capture newly discovered work items in a structured format that can be properly decomposed or executed.

**When to Use**:
- **Level 3+**: When discovering new work during decomposition
- When identifying tasks that need structured planning

**Example**:
```bash
/create-todo "Implement rate limiting for API endpoints"
/create-todo "Add comprehensive error handling to payment processing"
/create-todo "Create integration tests for user authentication flow"
```

### /create-todo-from-report

**Command**: `/create-todo-from-report <report-file>`

**Arguments**:
- `<report-file>`: Path to analysis report containing options or recommendations

**Purpose**: Extract actionable options from analysis reports, facilitate user selection, and generate focused TODO contexts for chosen items.

**Why Use**: To convert analysis recommendations into actionable work items with user input on priorities.

**When to Use**:
- **Level 1+**: After generating analysis reports with options
- When reports contain multiple possible actions

**Example**:
```bash
/create-todo-from-report docs/reports/solutions-caching-20241215-160000.md
/create-todo-from-report docs/reports/risks-security-20241215-143022.md
```

### /work-on-todo

**Command**: `/work-on-todo <todo-context-file> [--expert=<expert-name>]`

**Arguments**:
- `<todo-context-file>`: Path to the TODO context file to execute
- `[--expert]`: Optional expert system to use
  - Available experts found in `.agent/experts/`: domain-specific expertise definitions

**Purpose**: Execute atomic TODO items with appropriate collaboration checkpoints and expert guidance when needed.

**Why Use**: To systematically work through implementation tasks with proper documentation and collaboration points.

**When to Use**:
- **Level 4**: Implementation execution phase
- When ready to execute well-defined atomic tasks

**Example**:
```bash
/work-on-todo context/todos/implement-jwt-tokens.md
/work-on-todo context/todos/database-migration.md --expert=database
/work-on-todo context/todos/setup-monitoring.md --expert=devops
```

---

## Quick Reference: Command Usage by SAID Level

### Level 0 (Vision Clarity)
```bash
/analyze problems context/project-context.md
/analyze risks docs/reports/problems-*.md
/sync-context docs/reports/problems-*.md
/sync-context docs/reports/risks-*.md
```

### Level 1 (Approach Viability)
```bash
/analyze solutions context/project-context.md --role=solutions-architect
/sync-decision context/project/project-context.md report.md 'option 1'
/sync-context docs/reports/solutions-*.md
```

### Level 2+ (Progressive Decomposition)
```bash
/decompose .agent/layers/project.md context/project-context.md
/decompose .agent/layers/component.md context/components/service.md
/decompose .agent/layers/feature.md context/features/feature.md
/plan-next-steps "Completed component design"
```

### Level 3 (TODO Discovery)
```bash
/create-todo "New task discovered during decomposition"
/create-todo-from-report docs/reports/analysis-report.md
/decompose .agent/layers/todo.md context/todos/task.md
```

### Level 4 (Implementation)
```bash
/work-on-todo context/todos/implement-feature.md
/work-on-todo context/todos/complex-task.md --expert=typescript
```

### Context Recovery
```bash
/sync-context any-file-with-important-info.md
/prime-context
/plan-next-steps "Current situation description"
```

### Starting New AI Session
```bash
/prime-context
```