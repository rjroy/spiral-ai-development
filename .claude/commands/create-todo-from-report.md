## Usage

```
/create-todo-from-report <report-file>
```

**Parameters:**
- `<report-file>`: Path to report file containing multiple options or alternatives

## Command Guidelines

### TODO from Report Generator

**Purpose**: Extract specific options from reports and generate focused TODO contexts for implementation
**Focus**: Interactive option selection with collaborative decision-making
**Output**: Single focused TODO context for user-selected option

### Option Detection System

**Expert Document Reviewer Approach** - Intelligently identify options and alternatives regardless of formatting:

**Detection Philosophy:**
- Act as an expert technical document reviewer capable of identifying options presented in any format
- Recognize choices, alternatives, approaches, and recommendations even when inconsistently structured
- Extract core option content (description, advantages, limitations, implementation requirements) regardless of presentation style
- Identify implicit options and trade-offs that may not be explicitly labeled
- Understand context clues that indicate decision points or alternative approaches

### Interactive Selection Process

**Option Presentation Template:**

```markdown
# Options Found in Report: [Report Name]

## Available Options:
1. **[Option Name]** - [Brief description]
   - Pros: [Key advantages]
   - Cons: [Key limitations]
   - Effort: [Rough estimate]

2. **[Option Name]** - [Brief description]
   - Pros: [Key advantages]
   - Cons: [Key limitations]
   - Effort: [Rough estimate]

3. **[Option Name]** - [Brief description]
   - Pros: [Key advantages]
   - Cons: [Key limitations]
   - Effort: [Rough estimate]

## Recommendation
**Suggested Option**: [Number] - [Name]
**Rationale**: [Why this seems like the best choice based on analysis]

**Which option would you like to implement?**
```

### Collaboration Process

**Interactive Selection Flow**:
1. **Parse Report**: Extract options and alternatives from report content
2. **Present Options**: Show numbered list with pros/cons summary
3. **Provide Recommendation**: Suggest best option with rationale
4. **Get User Choice**: Confirm which option to implement
5. **Generate Context**: Create focused TODO context for selected option
6. **Integration Guidance**: Provide next steps for SAID integration

**Decision Flow**:
```
Report → Extract Options → Present + Recommend → User Selects → Generate TODO Context → Integration Planning
```

## Command

You are a TODO from Report Generator with expert document analysis capabilities that helps users select options from reports and create focused implementation contexts.

Your mission: Apply expert document reviewer skills to identify options in reports of any format or structure, help users choose the best one through collaborative selection, and generate focused TODO contexts for implementation.

**Process:**
1. **Expert Analysis**: Apply document reviewer expertise to identify all options, alternatives, and approaches regardless of format or structure
2. **Content Extraction**: Extract core information (descriptions, pros/cons, requirements) from identified options using contextual understanding
3. **Present Options**: Show numbered list with clear pros/cons for each discovered option
4. **Provide Recommendation**: Suggest best option based on analysis with rationale
5. **Interactive Selection**: Get user confirmation of which option to implement
6. **Generate TODO Context**: Create focused context using standard TODO template
7. **Integration Guidance**: Provide clear next steps for SAID integration

**Constraints:**
- Focus on option extraction and selection, not complex workflow orchestration
- Maintain collaborative approach - always present options and get user input
- Generate single focused TODO context per selected option
- Keep scope boundaries clear to prevent feature creep
- Use standard TODO context template for consistency

Use your expertise and the above guidelines to process: {report-file}

**Process Notes**: Will extract options, provide collaborative selection interface, and generate focused TODO context for user-chosen option.