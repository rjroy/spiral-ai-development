# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Collaboration Posture for AI

**Apply pressure, don't just follow process.** When Claude Code suggests solutions, the first question isn't "Is this right?" but "What assumptions is this making?" Push back on confident-sounding answers. Fluent responses that skip over constraints or trade-offs should trigger suspicion, not acceptance.

**Surface tensions rather than resolve them.** When requirements conflict or technical approaches involve trade-offs, don't let AI smooth over the complexity with "it depends" answers. Force explicit choices with documented rationale. The goal is informed human judgment, not AI consensus. If something sounds too clean or complete, it probably is—keep probing until you find where it bends or breaks.

## Repository Purpose

This is a meta-template repository for the **Spiral AI Development (SAID)** methodology - a systematic approach for managing complex projects through AI-human collaboration. It provides commands and patterns for progressive understanding and implementation.

## Existing SAID Commands

All commands are located in `.claude/commands/`:

### /analyze `<focus>` `<input-description>` `[--roles=<role1,role2,...>]`
Universal analysis command that performs focused research and analysis. Available focus types (from `.agent/focus/`):
- `problems` - Problem identification and clarification
- `risks` - Risk assessment and mitigation strategies
- `solutions` - Solution options with trade-offs

### /sync-context `<any-file>` or `init`
Extracts and integrates critical information from any file into project context files. Use `init` to initialize context structure from templates.

### /sync-decision `<context-file>` `<decision-report>` `<selected-option>`
Formally integrates a selected decision from an analysis report into the project's decision history with full traceability.

### /prime-context
Updates the CLAUDE.md file with a concise summary of current project state from context files, enabling quick AI orientation.

### /decompose `<type-definition-file>` `<context-file>`
Executes type-specific decomposition using definitions from `.agent/layers/`:
- `project.md` - High-level project breakdown
- `component.md` - System component analysis
- `feature.md` - Feature-level decomposition
- `todo.md` - Atomic task decomposition

### /plan-next-steps `<current-phase>` `[context-file]`
Generates detailed transition plans with prioritized actions and resource estimates.

### /create-todo `<todo-description>`
Transforms a TODO description into structured context suitable for SAID integration.

### /create-todo-from-report `<report-file>`
Extracts actionable items from analysis reports and creates TODO contexts.

### /work-on-todo `<todo-context-file>` `[--expert=<expert-name>]`
Executes atomic TODO items with collaboration checkpoints. Expert systems available in `.agent/experts/`.

## Key Directories

- `.claude/commands/` - SAID command definitions
- `.agent/` - Framework support files:
  - `focus/` - Analysis focus definitions (problems, risks, solutions)
  - `layers/` - Decomposition type definitions
  - `roles/` - Stakeholder role definitions for analysis
  - `experts/` - Domain expert systems for implementation
  - `patterns/` - Reusable pattern files
  - `templates/` - Context initialization templates
- `docs/reports/` - Generated analysis reports
- `context/` - Project context files (created by SAID)

## Working with SAID

1. **Starting a Project**: Create design documents then run `/sync-context init`
2. **Analysis Phase**: Use `/analyze` with appropriate focus
3. **Decision Making**: Use `/sync-decision` to record choices
4. **Decomposition**: Use `/decompose` progressively from project to TODO level
5. **Implementation**: Use `/work-on-todo` for atomic task execution
6. **Context Management**: Use `/prime-context` to restore context between sessions

## Development Notes

This is a methodology template repository - there are no traditional build, test, or lint commands. The focus is on the SAID commands and workflows for managing AI-human collaboration in software projects.