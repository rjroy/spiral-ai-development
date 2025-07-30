## Usage
```
/decompose <type-definition-file> <context-file>
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/plan/dynamic-role-assignment.md` (Type definition loading and role adaptation)
Load: `.claude/patterns/general/checkpoints.md` (When collaboration checkpoints are undefined in type definition)

## Purpose
Execute type-specific decomposition using configurable type definitions to transform contexts into domain-specific artifacts.

## Process

### 1. Initialize
- Load and validate type definition and context files
- Extract expert role and decomposition strategy from type definition
- Adopt mission, focus, and success measures as specified

### 2. Analyze
- Apply decomposition rules from type definition to identify opportunities
- Execute analysis process steps as defined in type definition
- Follow domain-specific expertise guidelines

### 3. Collaborate
- Execute checkpoints defined in type definition with required user input
- **Fallback**: If type definition lacks collaboration checkpoints, ask user: "The type definition doesn't specify collaboration checkpoints. What key decisions or validation points would you like me to pause for during this decomposition?"

### 4. Generate
- Create artifacts using templates and specifications from type definition
- Apply validation criteria and quality assurance checks
- Confirm success criteria are met and deliverables ready for next phase

## Examples
```
/decompose .claude/decompose-types/todo.md context/todos/complex-feature/todo-context.md
/decompose .claude/decompose-types/project.md context/project-context.md
/decompose .claude/decompose-types/component.md context/components/auth.md
```

## Key Principles
- Follow type definition rules precisely
- Execute all collaboration checkpoints as specified
- Generate artifacts exactly as templated
- Apply all validation and QA criteria
- Honor expert role mission and focus from type definition

## Dynamic Behavior
Based on loaded type definition, assumes the expert role specified in "Expert Role Definition" section and applies the mission, focus, and success measures defined there.

Command adapts behavior based on type definition, enabling consistent decomposition patterns across domains while preserving domain-specific expertise.