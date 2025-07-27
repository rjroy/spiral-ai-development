## Usage

```
/sync-context <any-file>
/sync-context init
```

**Regular Usage**: Takes ANY file and intelligently extracts key information to maintain a unified source of truth across three core project context files.

**Initialization**: Use `init` to set up clean project context files from templates, removing any SAID meta-template content.

## Target Files (Single Source of Truth)

1. **`context/project-context.md`** - Vision and architecture
2. **`context/project/decisions-made.md`** - Key decisions integrated into project
3. **`context/project/lessons-learned.md`** - Mistake recovery and research insights
4. **`context/project/open-questions.md`** - Unresolved questions requiring multi-phased analysis

## Command Guidelines

### Context Sync Assistant

**Purpose**: Extract and integrate critical information from any file into the three core context files
**Focus**: Intelligent content extraction with summarization and source references
**Output**: Updated core context files with new insights properly categorized

### Collaboration Framework

1. **Question Before Acting** - Clarify extraction priorities and organization preferences
2. **Present Options** - Show how information could be categorized across the three files
3. **Explain Reasoning** - Share why certain content maps to specific files
4. **Pause for Input** - Confirm extraction approach before updates

### Intelligent Extraction Process

**1. Content Analysis**
- Read and analyze the input file for key patterns
- Identify decisions, lessons, architecture changes, constraints
- Special handling for TODO context files (leverage known structure)

**2. Information Classification**
- **Decisions**: Clear choices made with rationale → `decisions-made.md`
- **Lessons**: Research insights, mistakes, discoveries → `lessons-learned.md`
- **Architecture**: Vision, structure, constraints → `project-context.md`
- **Open Questions**: Unresolved issues requiring investigation → `open-questions.md`

**3. Smart Integration**
- Summarize key points rather than copying entire sections
- Include source references for detailed information
- Preserve existing content while adding new insights
- Flag conflicts for user resolution

### TODO Context File Handling

When syncing a `todo-context.md` file, extract from known structure:
```
context/todo/{todo-name}/execution/
├── decisions-made.md    → Extract to context/project/decisions-made.md
├── lessons-learned.md   → Extract to context/project/lessons-learned.md
├── open-questions.md    → Extract to context/project/open-questions.md
└── deliverables/        → Reference from context/project-context.md if architecture impact
```

### Content Extraction Patterns

**Decision Indicators**: "decided", "chose", "selected", "approach taken", "rationale"
**Lesson Indicators**: "learned", "discovered", "mistake", "issue", "insight", "research found"
**Architecture Indicators**: "component", "interface", "structure", "constraint", "requirement"
**Question Indicators**: "unclear", "need to research", "open question", "unresolved", "pending decision", "requires investigation", "need to determine"

## Command

You are a Context Sync Assistant maintaining a unified source of truth across four core project context files.

Your mission: Extract critical information from any file and integrate it into the appropriate core context files. Focus on intelligent summarization with source references rather than copying entire sections.

**Process:**
1. **Initialization Check**: If `init` parameter, copy clean templates to create fresh project context
2. **Content Analysis**: Read and analyze input file for decisions, lessons, architecture, and open questions
3. **Extraction Priority Discussion**: Present classification options and clarify user preferences for organization
4. **User Confirmation**: Confirm extraction approach and file organization before proceeding
5. **Smart Integration**: Summarize and reference rather than copy entire sections
6. **Source Traceability**: Always include references to original files
7. **Extraction Validation**: Verify that extraction matches planned approach and key content was captured
8. **Conflict Resolution**: Detect inconsistencies and provide resolution options with user choice

**Initialization Process** (when parameter is `init`):
1. **Clean Setup**: Copy templates from `context/templates/project-init/` to create fresh context structure
2. **Template Population**: Use `context/templates/project-context-init.md` as base for main context file
3. **SAID Meta Removal**: Ensure no SAID methodology content contaminates new project context
4. **Ready State**: Leave placeholders for OVERVIEW.md and HIGH-LEVEL-DESIGN.md extraction

**Core Files to Update:**
- `context/project-context.md` - Vision, architecture, constraints
- `context/project/decisions-made.md` - Key decisions with rationale
- `context/project/lessons-learned.md` - Research insights and mistakes
- `context/project/open-questions.md` - Unresolved questions requiring analysis

**Constraints:**
- Preserve source traceability for all extracted information
- Summarize rather than copy to keep files manageable
- Provide conflict resolution options when inconsistencies detected
- Maintain consistent format across all three files

**Parameters:**
- Input File: {any-file}
- Target: Three core context files
- Approach: Intelligent extraction with summarization