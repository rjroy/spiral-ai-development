## Usage
```
/prime-context
```

## Required Patterns
Load: `.agent/patterns/sync/context-files.md` (context file management)

## Purpose
Update CLAUDE.md with a concise summary of current project context, enabling immediate AI orientation without requiring separate context commands.

## Main Role
You are a context curator specializing in AI session priming. Your expertise lies in extracting the most relevant information from comprehensive context files and presenting it in a format that enables immediate productive engagement. You understand that AI assistants need just enough context to be effective without being overwhelmed by historical details.

## Process

### 1. Read Context Files
- Read all four context files if they exist:
  - `context/project-context.md` - Main context manifest
  - `context/project/decisions-made.md` - Key decisions with rationale
  - `context/project/open-questions.md` - Unresolved questions
  - `context/project/lessons-learned.md` - Insights and patterns
- Handle missing files gracefully

### 2. Extract Key Information
- **From project-context.md**: Current phase, primary focus areas, key constraints
- **From decisions-made.md**: Most recent 3-5 decisions (last 7-14 days preferred)
- **From open-questions.md**: Top 2-3 critical unresolved questions
- **From lessons-learned.md**: Most relevant insights for current work

### 3. Generate Context Summary
Create a concise summary optimized for AI orientation:
- Current development phase and status
- Recent important decisions that affect ongoing work
- Active work areas or TODOs
- Critical constraints or blockers to remember
- Key technical choices already made

### 4. Update CLAUDE.md
- Locate the marked section in CLAUDE.md (between BEGIN/END PRIME-CONTEXT markers)
- Replace entire marked section with new summary
- Preserve all content outside the markers
- Include update timestamp

## Context Summary Template
```markdown
<!-- BEGIN PRIME-CONTEXT -->
<!-- This section is automatically updated by /prime-context command -->
<!-- Last updated: YYYY-MM-DD HH:MM:SS -->

### Current Project State

**Development Phase**: [Current phase from project-context.md]
**Primary Focus**: [Main work areas or objectives]

**Recent Key Decisions** (last 7 days):
- [Decision 1 with brief rationale]
- [Decision 2 with brief rationale]
- [Decision 3 with brief rationale]

**Active Constraints**:
- [Critical constraint 1]
- [Critical constraint 2]

**Critical Open Questions**:
- [Top priority unresolved question]
- [Second priority question if critical]

**Technical Stack Choices**:
- [Key technology decision 1]
- [Key technology decision 2]

<!-- END PRIME-CONTEXT -->
```

## Quality Standards
- Summary must be under 30 lines to maintain CLAUDE.md readability
- Focus on actionable, current information over historical context
- Include only decisions/info that directly impacts ongoing work
- Use bullet points for quick scanning
- Timestamp for context freshness awareness

## Error Handling
- If no context files exist, create minimal placeholder with initialization reminder
- If CLAUDE.md lacks markers, append marked section after "Important Notes"
- If context files are malformed, extract what's possible and note issues
- Never delete content outside the marked section

## Integration Notes
- This command complements, not replaces, detailed context commands
- Run after significant context updates or at start of new work sessions
- Safe for version control - clear separation of static/dynamic content
- Designed for "context priming" after breaks in development