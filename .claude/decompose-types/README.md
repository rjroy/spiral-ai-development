# Type Definition Format Specification

## Overview

Type definition files define how the universal `/decompose` command should process different kinds of contexts. Each type definition specifies the input format, decomposition rules, collaboration checkpoints, and output specifications for a particular decomposition domain.

## Format Philosophy: Markdown + Checkboxes

The SAID system uses **Markdown with YAML frontmatter** and **checkbox task lists** (`- [ ] task`) for optimal human-AI collaboration:

**For Humans:**
- ✅ Natural, scannable format that's easy to read and edit
- ✅ Universal tool support (GitHub, VS Code, Obsidian, etc.)
- ✅ Interactive checkboxes that can be literally checked off as work progresses
- ✅ Rich formatting support for explanations and documentation

**For AI:**
- ✅ Native understanding of Markdown structure and task lists
- ✅ Can parse, modify, and generate checkbox lists naturally
- ✅ YAML frontmatter provides structured metadata when needed
- ✅ Can reason about task dependencies and completion status

**When to Use Each Format:**
- **Markdown Headers & Text**: Human-readable content, explanations, descriptions
- **YAML Frontmatter**: Structured metadata that needs machine processing
- **Checkbox Lists** (`- [ ] task`): Any actionable items, dependencies, or trackable work
- **Inline YAML blocks**: Complex structured data that needs to be machine-readable

### Example: Modern Context File Format
```markdown
# TODO: Implement User Authentication

Implement secure user authentication with JWT tokens and session management.

---
todo_type: "complex_feature"
complexity: "COMPLEX"
urgency: "HIGH"
estimated_effort: "2-3 days"
---

## Work Scope

**Primary Deliverable**: Working authentication system with JWT tokens
**Success Criteria**: Users can register, login, and access protected routes

### Prerequisites
- [ ] Database schema designed and migrated
- [ ] Security requirements reviewed with team
- [ ] JWT library selected and approved

### Dependencies
- [ ] User management API (must be completed first)
- [ ] Database connection established

## Next Actions
- [ ] Design authentication flow
- [ ] Implement JWT token generation
- [ ] Add session management
- [ ] Write integration tests
```

## Standard Type Definition Format

### File Structure
```markdown
# {Type} Decomposition Type Definition

## Type Identity
- **Type Name**: {TypeName}
- **Input Format**: {InputDescription}
- **Output Format**: {OutputDescription}
- **Decomposition Focus**: {PurposeStatement}

## Input Requirements
### Expected Input Structure
{MarkdownWithYAMLFrontmatterExample}
### Input Validation Rules
{ValidationCriteria}

## Decomposition Strategy
### Analysis Process
{StepByStepAnalysis}
### Decomposition Rules
{RulesAndConstraints}

## Collaboration Checkpoints
### Required User Input Points
{CheckpointDefinitions}

## Output Specification
### Directory Structure
{OutputDirectoryLayout}
### Output Artifacts
{ArtifactTemplates}

## Validation Requirements
{ValidationCriteria}

## Quality Assurance
{QAChecklists}

## Expert Role Definition
{RoleDescription}
```

## Required Sections

### 1. Type Identity (Required)
**Purpose**: Defines the basic identity and purpose of the decomposition type.

**Required Fields:**
- `Type Name`: Single word identifier for the type
- `Input Format`: Description of expected input structure
- `Output Format`: Description of generated output structure
- `Decomposition Focus`: One sentence describing the decomposition purpose

**Example:**
```markdown
## Type Identity
- **Type Name**: TODO
- **Input Format**: TODO context Markdown file with YAML frontmatter
- **Output Format**: Subtask context Markdown files with checkbox task lists
- **Decomposition Focus**: Break complex work into atomic, executable tasks
```

### 2. Input Requirements (Required)
**Purpose**: Defines what input the decomposition type expects and how to validate it.

**Required Subsections:**
- `Expected Input Structure`: Markdown example with YAML frontmatter showing required fields
- `Input Validation Rules`: List of validation criteria

**Example:**
```markdown
### Input Validation Rules
- Must have TODO name in header and clear description
- Must have primary deliverable and success criteria defined
- Must have valid Markdown structure with YAML frontmatter
- Task lists should use checkbox format (`- [ ] task`) for actionable items
```

### 3. Decomposition Strategy (Required)
**Purpose**: Defines how the input should be analyzed and broken down.

**Required Subsections:**
- `Analysis Process`: Step-by-step analysis approach
- `Decomposition Rules`: Rules governing how decomposition is performed

**Example:**
```markdown
### Decomposition Rules
- Generate 3-7 subtasks maximum (avoid over-decomposition)
- Each subtask must be atomic and independently executable
- Subtasks should enable parallel execution where possible
```

### 4. Collaboration Checkpoints (Required)
**Purpose**: Defines when and how to involve the user in the decomposition process.

**Required Structure:**
Each checkpoint must have:
- `Trigger`: When this checkpoint occurs
- `Question`: What to ask the user
- `Required`: What the user must provide

**Example:**
```markdown
1. **Decomposition Strategy Validation**
   - **Trigger**: After complexity assessment, before subtask generation
   - **Question**: "I've identified these potential approaches: [options]. Which aligns best with your priorities?"
   - **Required**: User must confirm approach before proceeding
```

### 5. Output Specification (Required)
**Purpose**: Defines the structure and format of generated artifacts.

**Required Subsections:**
- `Directory Structure`: File/folder organization
- `Output Artifacts`: Templates for generated files

**Example:**
```markdown
### Directory Structure
```
context/todo/{parent-todo-name}/
├── todo-context.md              # Original context (Markdown + YAML frontmatter)
├── decomposition/
│   ├── decomposition-plan.md    # Strategy with checkbox task dependencies
│   └── {subtask-1}/
│       └── todo-context.md      # Subtask context with checkbox lists
```
```

### 6. Validation Requirements (Required)
**Purpose**: Defines how to validate successful decomposition.

**Required Subsections:**
- `Pre-Decomposition Validation`: Requirements before starting
- `Post-Decomposition Validation`: Requirements after completion
- `Success Criteria`: How to measure success

### 7. Quality Assurance (Required)
**Purpose**: Defines quality checks and pressure testing questions.

**Required Subsections:**
- `Domain-Specific QA Checklist`: Specific quality checks
- `Pressure Testing Questions`: Questions to validate assumptions

### 8. Expert Role Definition (Required)
**Purpose**: Defines the AI assistant role and mission.

**Required Fields:**
- `Role`: Name of the expert role
- `Mission`: One sentence mission statement
- `Focus`: Primary focus area
- `Success Measure`: How success is measured

## Optional Sections

### Advanced Validation
- Spike requirements (integration spike, component spike, etc.)
- Performance validation requirements
- Security validation requirements

### Domain-Specific Extensions
- Specialized analysis techniques
- Advanced collaboration patterns
- Custom artifact templates

## Type Definition Validation

### Required Validation Checks
- [ ] All required sections are present
- [ ] All collaboration checkpoints have trigger, question, and required fields
- [ ] Input validation rules are specific and testable
- [ ] Output templates use proper Markdown format with YAML frontmatter
- [ ] Task lists use checkbox format (`- [ ] task`) for actionable items
- [ ] Expert role definition includes all required fields

### Optional Validation Checks
- [ ] Examples are provided for complex concepts
- [ ] Pressure testing questions challenge key assumptions
- [ ] Directory structure aligns with project conventions
- [ ] Artifact templates reference appropriate base templates

## Usage by `/decompose` Command

The universal `/decompose` command will:

1. **Load Type Definition**: Parse the specified type definition file
2. **Validate Input**: Apply input validation rules to the context file
3. **Execute Analysis**: Follow the analysis process steps
4. **Apply Collaboration**: Execute collaboration checkpoints in order
5. **Generate Artifacts**: Create output artifacts using templates
6. **Validate Results**: Apply post-decomposition validation
7. **Apply QA**: Run quality assurance checks

## Creating New Type Definitions

### Process
1. **Identify Decomposition Pattern**: What input → output transformation is needed?
2. **Define Input Requirements**: What Markdown structure and YAML frontmatter is needed?
3. **Design Decomposition Strategy**: How should the analysis work?
4. **Plan Collaboration**: Where does user input add value?
5. **Specify Outputs**: What Markdown artifacts with checkbox lists should be generated?
6. **Define Validation**: How to ensure quality results?
7. **Test with Examples**: Validate with real Markdown input examples

### Format Guidelines
- **Use Markdown**: All context files should be readable by humans
- **YAML Frontmatter**: For structured metadata that machines need to process
- **Checkbox Lists**: For any actionable items (`- [ ] task` format)
- **Rich Formatting**: Bold, italic, headers to improve human readability
- **External References**: Link to separate files for complex technical specs

### Naming Convention
- File: `.claude/decompose-types/{type-name}.md`
- Type Name: Single word, capitalized (TODO, Project, Component)
- Expert Role: "{Type} Decomposition Assistant" or "{Domain} Expert"

This format ensures consistency across all type definitions while preserving domain-specific expertise and flexibility.