# Template Detection Patterns

## Template Selection Logic

### Filename Pattern Mapping
- `component*.md` → `.claude/templates/component-artifact.md`
- `feature*.md` → `.claude/templates/feature-artifact.md`
- `implementation*.md` → `.claude/templates/implementation-artifact.md`
- `project-context.md` → `.claude/templates/project-context-init.md`
- Generic context files → `.claude/templates/project-context-init.md`

## File Creation Process

### Template Application Steps
1. **Detect Template**: Match filename pattern to appropriate template
2. **Load Template**: Read template file from `.claude/templates/`
3. **Update Metadata**: Set YAML frontmatter (created_date, project_name, artifact_type, said_level)
4. **Replace Placeholders**: Substitute ProjectName, YYYY-MM-DD, ComponentName
5. **Create Structure**: Ensure directory structure exists (`context/` directory)
6. **Write File**: Create initial context file with template structure
7. **Proceed**: Continue with main operation on new file

### Error Handling
- **Template Missing**: Provide fallback basic Markdown structure with YAML frontmatter
- **Directory Missing**: Create directory structure as needed
- **Template Malformed**: Use basic structure, warn user

### Fallback Structure
```markdown
---
project_name: "ProjectName"
created_date: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
artifact_type: "context"
---

# [Context Name]

## Overview
[Context description]

## Key Decisions
[Decisions made for this context]

## Implementation Notes
[Technical details and requirements]
```