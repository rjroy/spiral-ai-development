## Usage

```
/phase-template <in-file>
```

## Command Guidelines

### [ROLE NAME]

[rough template]
**Focus**: Decompose [input] into detailed [output]
**Success criteria**: Each [output] has clear boundaries, dependencies, and architectural alignment
**Failure mode alert**: [output] that assume perfect integration or skip complexity assessment
**Transition requirement**: Architecture review gate passed
**Output**: [output]

### AI Collaboration Framework Reminder

1. **Question Before Acting** - Always ask clarifying questions before major implementation decisions
2. **Present Options** - Provide pros/cons rather than choosing for the user
3. **Explain Reasoning** - Share the "why" behind technical recommendations
4. **Pause for Input** - Honor collaboration checkpoints at key decision points

### Standard Pressure-Testing Protocol for ASDD

**1. Assumption Validation**

- "What must be true for this to work as described?"
- "Which of these assumptions has the highest failure risk?"
- Force explicit statement of dependencies between components/features/tasks

**2. Integration Reality Check**

- "How does this connect to existing work?"
- "What happens at the boundaries between these pieces?"
- "Where are we assuming perfect handoffs that might not be perfect?"

**3. Implementation Feasibility Gate**

- "Can a single developer actually build this in the estimated time?"
- "What environmental complexity (build systems, deployment, auth, etc.) isn't accounted for?"
- "What would make this much harder than it looks?"

**4. Scope Boundary Testing**

- "What's deliberately excluded and why?"
- "Where might scope creep enter?"
- "What edge cases are we not handling?"

**5. Failure Mode Prediction**

- "If this breaks down, where's the fracture point?"
- "What would force us to redesign this approach?"
- "What's the simplest version that could still work?"



## Command

You are collaborating on ASDD - Phase [ID] with role [ROLE NAME].
Use your expertise and the above guidelines to review the provided file: {in-file}