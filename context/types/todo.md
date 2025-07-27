# TODO Decomposition Type Definition (Simple)

## Type Identity
- **Type Name**: TODO
- **Input Format**: TODO context Markdown file
- **Output Format**: Subtask context Markdown files  
- **Decomposition Focus**: Break complex work into atomic, executable tasks

## Input Requirements

### Expected Input Structure
```markdown
# TODO: [Name]

Description of what needs to be accomplished.

---
todo_type: "complex_work"
complexity: "SIMPLE | COMPLEX | EXTREME"
urgency: "HIGH | MEDIUM | LOW"
---

## Work Scope

**Primary Deliverable**: What needs to be produced
**Success Criteria**: How to know when complete

### What Needs to Be Done
- Key task 1
- Key task 2
- Key task 3

## Collaboration Needs

### Decisions Needed
- [ ] Choice requiring user input 1
- [ ] Choice requiring user input 2

### People to Involve
- Who needs to provide input
- Who needs to review results
```

### Input Validation Rules
- Must have TODO name and clear description
- Must have primary deliverable and success criteria defined
- If complexity is "COMPLEX" or "EXTREME", decomposition is recommended
- Must have valid Markdown structure with YAML frontmatter

## Decomposition Strategy

### Decomposition Rules
- Generate 3-7 subtasks maximum (avoid over-decomposition)
- Each subtask must be atomic and independently executable
- Subtasks should enable parallel execution where possible
- Each subtask gets its own directory and context file

## Collaboration Checkpoints

### Required User Input Points
1. **Decomposition Strategy Validation**
   - **Trigger**: After complexity assessment
   - **Question**: "I've identified these approaches for breaking down the work: [options]. Which strategy works best for you?"
   - **Required**: User must confirm approach before proceeding

2. **Priority Ordering**
   - **Trigger**: After subtask identification
   - **Question**: "Which subtasks should be tackled first? Are there any dependencies or priorities?"
   - **Required**: User must confirm execution sequence

3. **Deliverable Expectations**
   - **Trigger**: Before final generation
   - **Question**: "What quality level and deliverables do you expect from each subtask?"
   - **Required**: User must specify expectations

## Output Specification

### Output Artifacts

#### Decomposition Plan Template
```markdown
# Decomposition Plan: [Parent TODO Name]

Why decomposition was needed and the approach taken for breaking down the work.

---
plan_type: "todo_decomposition"
parent_todo: "Original TODO name"
strategy: "Approach taken"
---

## Subtasks

### Subtask 1: [Name]
**Description**: What this subtask accomplishes
**Deliverable**: Specific output expected
**Estimated Effort**: Time estimate
**Skills Required**: What expertise is needed

### Subtask 2: [Name]
**Description**: What this subtask accomplishes
**Deliverable**: Specific output expected
**Estimated Effort**: Time estimate
**Skills Required**: What expertise is needed

## Dependencies

**Task Order**: Which tasks must be done in sequence
**Parallel Work**: Which tasks can be done simultaneously

## Coordination

**Check-in Points**: When to sync progress between subtasks
**Final Assembly**: How results will be combined
```

#### Subtask Context Template
```markdown
# Subtask: [Name]

Clear, atomic work description of what this subtask accomplishes.

---
subtask_type: "atomic_work"
parent_todo: "Reference to parent TODO"
deliverable: "Specific expected output"
estimated_effort: "Time estimate"
---

## Success Criteria
How to know when this subtask is complete.

## Work Definition

**Scope**: Clear boundaries of this subtask

### What to Do
- [ ] Specific action 1
- [ ] Specific action 2
- [ ] Specific action 3

### Constraints
- Important limitation 1
- Important limitation 2

### Prerequisites
- [ ] What must be done first
- [ ] Required setup

## Coordination

### Dependencies
- [ ] Other subtask this depends on
- [ ] External dependency

### What This Enables
- What this subtask makes possible
- Who depends on this output

## Collaboration Needs

### Decision Points
- [ ] Choice requiring user input
- [ ] Design decision needed

### Review Points
- [ ] When to pause and confirm approach
- [ ] Quality check before completion
```

## Validation Requirements

- Input file has valid Markdown structure with YAML frontmatter
- Each subtask is atomic and independently executable
- Dependencies are clearly defined
- User has validated decomposition strategy and expectations

## Expert Role Definition

**Role**: Decompose TODO Assistant
**Mission**: Transform complex TODO contexts into atomic, executable subtasks with clear coordination
**Focus**: Creating work items that can be independently executed while maintaining coordination
**Success Measure**: Subtasks enable effective execution with clear integration points