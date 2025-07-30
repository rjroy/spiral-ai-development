## Usage
```
/sync-context <any-file>
/sync-context init
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/sync/context-integration.md` (Automatic classification and extraction to allow Target file mapping and integration rules)

## Purpose
Extract and integrate critical information from any file into core project context files.

## Process

### Regular Sync (any file)
1. **Analyze Content**: Use classification indicators to identify decisions, lessons, architecture, questions
2. **Extract Key Points**: Summarize rather than copy entire sections
3. **Integrate Smartly**: Add to appropriate target files with source references
4. **Flag Conflicts**: Only prompt when actual conflicts need resolution

### Initialization (`init`)
1. **Clean Setup**: Copy templates from `.claude/templates/project-init/`
2. **Remove SAID Meta**: Ensure no methodology content contaminates project context
3. **Ready State**: Leave placeholders for OVERVIEW.md and HIGH-LEVEL-DESIGN.md extraction

## Target Files
- `context/project-context.md` - Vision, architecture, constraints
- `context/project/decisions-made.md` - Key decisions with rationale
- `context/project/lessons-learned.md` - Research insights and mistakes
- `context/project/open-questions.md` - Unresolved questions

## Special Handling

### TODO Context Files
When syncing `todo-context.md`, extract from execution structure:
```
context/todo/{name}/execution/
├── decisions-made.md    → project/decisions-made.md
├── lessons-learned.md   → project/lessons-learned.md
├── open-questions.md    → project/open-questions.md
└── deliverables/        → Reference in project-context.md if architectural
```

## Key Principles
- Summarize, don't copy entire sections
- Always include source references
- Preserve existing content
- Apply classification patterns automatically
- Only ask user when conflicts require resolution

## Example Flow
```
User: /sync-context docs/reports/phase1-analysis.md

AI: Analyzing phase1-analysis.md for key information...

Found:
- 3 decisions (database choice, auth strategy, deployment approach)
- 2 lessons (performance bottleneck discovery, library compatibility issue)
- 1 open question (scaling strategy for year 2)

Integrating into:
- decisions-made.md: Added database and auth decisions with rationale
- lessons-learned.md: Added performance and compatibility insights
- open-questions.md: Added scaling question with context

All updates include source reference to phase1-analysis.md sections.
Context sync complete.
```