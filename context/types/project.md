# Project Decomposition Type Definition (Simple)

## Type Identity
- **Type Name**: Project
- **Input Format**: Project context Markdown file with YAML frontmatter (Level 1 approach)
- **Output Format**: Component context Markdown files with YAML frontmatter (Level 2 structure)
- **Decomposition Focus**: Define system boundaries and component interfaces from validated approach

## Input Requirements

### Expected Input Structure

**Markdown File with YAML Frontmatter:**
```markdown
---
artifact_type: "approach"
project_name: "ProjectName"
said_level: 1
---

## Project Identity

**Purpose**: Core project purpose statement
**Primary Users**: Primary user groups description
**Success Metrics**: How success is measured

## Technical Approach

**Validated Solution Approach**: Description of the validated technical approach

### Key Requirements
- Important requirement 1
- Important requirement 2
- Important requirement 3

## Validation Results

**Approach Validation**: Evidence approach works
**Risk Assessment**: Known risks and mitigations
**Feasibility Confirmation**: Team can build this
```

### Input Validation Rules
- Must have YAML frontmatter with `artifact_type: "approach"` and `said_level: 1`
- Must have "## Project Identity" section with **Purpose** field
- Must have "## Technical Approach" section
- Must have "## Validation Results" section

## Decomposition Strategy

### Decomposition Rules
- Generate 3-7 components maximum (team-scale, not micro-services)
- Each component must have single, clear responsibility
- Components must have well-defined interfaces
- Must be realistic for team to build and maintain

## Collaboration Checkpoints

### Required User Input Points
1. **Component Boundaries Validation**
   - **Trigger**: After component identification
   - **Question**: "I've identified these component boundaries: [list]. Do these align with your understanding of the system's functional areas?"
   - **Required**: User must validate component responsibilities

2. **Interface Design Discussion**
   - **Trigger**: After component definition
   - **Question**: "Here are the interface options for component communication: [options]. Which approach fits your needs?"
   - **Required**: User must choose interface patterns

3. **Component Testing Strategy**
   - **Trigger**: Before generating artifacts
   - **Question**: "How should we handle testing between components? What makes sense for your team?"
   - **Required**: User must define testing approach

## Output Specification

### Output Artifacts

#### Project Structure Document

**Markdown File with YAML Frontmatter:**
```markdown
---
artifact_type: "structure"
project_name: "ProjectName"
said_level: 2
---

## System Structure

### Components

#### Component Name 1
**Responsibility**: Single clear purpose
**Interfaces**: What it provides to other components
**Dependencies**: What it depends on

#### Component Name 2
**Responsibility**: Single clear purpose
**Interfaces**: What it provides to other components
**Dependencies**: What it depends on

## Integration Approach

**Communication**: How components talk to each other
**Data Flow**: How data moves through the system
**Testing Strategy**: How to test component integration

## Next Steps
- Component 1: Ready for Level 3 decomposition
- Component 2: Ready for Level 3 decomposition
```

## Validation Requirements
- Level 1 approach is validated and documented
- Component boundaries make sense to user
- Interfaces are well-defined
- User has validated all collaboration checkpoints

## Expert Role Definition

**Role**: Structure Definition Expert
**Mission**: Define clear system boundaries and component interfaces that support the Level 1 approach
**Focus**: System boundaries defined, component interfaces specified
**Success Measure**: Components can be built by team with clear integration pathways