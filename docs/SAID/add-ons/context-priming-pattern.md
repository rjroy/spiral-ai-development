# Context Priming

**The Problem**: AI has no memory between sessions. Starting complex work without context leads to misaligned assumptions and wasted effort.

**The Solution**: Give AI a brief context update before executing SAID commands.

## Basic Pattern

```
> Be aware, I've [what you completed]. [current state]. I'm about to [intended action].
AI: [acknowledgment]
> /your-command
```

## When to Use

**Always use when**:
- Resuming after time gaps (days/weeks)
- Major discoveries or requirement changes
- Moving between SAID workflows
- After stakeholder input or external decisions

**Skip when**:
- Continuing work in same session
- Simple, isolated tasks
- Context files are current and AI has just read them

## Examples

**After research**:
```
> Be aware, I've completed authentication research. OAuth2 with PKCE is recommended but has integration complexities with our existing session management. I'm about to decompose the project structure.

AI: Got it - OAuth2 validated but integration challenges discovered. Ready to help define system boundaries with those constraints in mind.

> /decompose .agent/layers/project.md context/approach-validation-context.md
```

**After stakeholder feedback**:
```
> Be aware, stakeholders approved our approach validation but added a requirement for audit logging throughout the system. I'm about to incorporate this into our component design.

AI: Understood - technical approach approved with new audit logging requirement. This will affect component boundaries and data flow. Ready to help integrate this.

> /decompose .agent/layers/project.md context/approach-validation-context.md
```

**After TODO work**:
```
> Be aware, I've processed the data model validation TODOs. We need both relational and document storage, plus there's a performance requirement we missed. I'm about to reprocess component specifics.

AI: Thanks for the update - hybrid storage patterns needed plus new performance constraints. These could significantly impact implementation specifics. Ready to help reprocess.

> /decompose .agent/layers/component.md context/structure-definition-context.md
```

## Why This Works

- **Prevents assumptions**: AI knows what's changed since last interaction
- **Improves recommendations**: AI suggestions account for current reality
- **Saves time**: Less back-and-forth to establish working context
- **Maintains quality**: Decision quality stays consistent across sessions

The goal is shared understanding before complex work, not perfect documentation.