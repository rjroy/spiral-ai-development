# Component Decomposition Type Definition (Simple)

## Type Identity
- **Type Name**: Component
- **Input Format**: Component context Markdown file with YAML frontmatter (Level 2 component)
- **Output Format**: Feature context Markdown files with YAML frontmatter (Level 3 features)
- **Decomposition Focus**: Create buildable specifications from validated structure

## Input Requirements

### Expected Input Structure

**Markdown File with YAML Frontmatter:**
```markdown
---
artifact_type: "component"
component_name: "ComponentName"
said_level: 2
---

## Component Definition

**Name**: ComponentName
**Purpose**: Single clear purpose statement
**Responsibility**: Primary responsibility description
**Boundaries**: What this component does NOT do

## Component Interfaces

### What This Component Provides
- Interface 1: What it does
- Interface 2: What it does

### What This Component Needs
- Dependency 1: What it needs from others
- Dependency 2: What it needs from others

## Integration Approach

**Communication**: How this component talks to others
**Data**: What data this component manages
**Testing**: How to test this component
```

### Input Validation Rules
- Must have YAML frontmatter with `artifact_type: "component"` and `said_level: 2`
- Must have "## Component Definition" section with **Name** and **Purpose** fields
- Must have "## Component Interfaces" section
- Must be valid Markdown with proper frontmatter

## Decomposition Strategy

### Decomposition Rules
- Generate 3-5 features maximum per component
- Each feature must have clear business value
- Features must be buildable by the team
- Features should not overlap with each other

## Collaboration Checkpoints

### Required User Input Points
1. **Feature Boundaries Validation**
   - **Trigger**: After feature identification
   - **Question**: "I've identified these features within the component: [list]. Do these make sense for your implementation?"
   - **Required**: User must validate feature scope

2. **API Design Discussion**
   - **Trigger**: After feature definition
   - **Question**: "Here are the API options for each feature: [options]. Which approach fits your needs?"
   - **Required**: User must approve API approaches

3. **Testing Strategy Discussion**
   - **Trigger**: Before generating artifacts
   - **Question**: "What testing approach makes sense for this component?"
   - **Required**: User must define testing standards

## Output Specification

### Output Artifacts

#### Component Features Document

**Markdown File with YAML Frontmatter:**
```markdown
---
artifact_type: "features"
component_name: "ComponentName"
said_level: 3
---

## Feature Overview

### Feature 1: Feature Name
**Purpose**: What this feature does for users
**Priority**: HIGH | MEDIUM | LOW

### Feature 2: Another Feature Name
**Purpose**: What this feature does for users
**Priority**: HIGH | MEDIUM | LOW

## Implementation Approach

**Development Order**: Which features to build first
**Integration Points**: How features connect
**Testing Strategy**: How to test the features

## Next Steps
- Feature 1: Ready for implementation planning
- Feature 2: Ready for implementation planning
```

#### Feature Artifact Document

**Uses simplified feature template focusing on:**
- **Feature Definition**: Name, purpose, and user value
- **Basic Requirements**: What the feature must do
- **Implementation Notes**: Key technical considerations
- **Testing Approach**: How to validate the feature works

## Validation Requirements
- Level 2 component is well-defined
- All component features have clear business value
- Features are buildable by the team
- User has validated all collaboration checkpoints

## Expert Role Definition

**Role**: Implementation Specifics Expert
**Mission**: Create clear, buildable specifications that enable the team to implement the Level 2 structure successfully
**Focus**: Each component has detailed implementation plan that's realistic for the team
**Success Measure**: Specifications enable successful component implementation with clear business value