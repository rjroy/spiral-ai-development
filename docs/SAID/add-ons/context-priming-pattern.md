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
- Moving between SAID phases
- After stakeholder input or external decisions

**Skip when**:
- Continuing work in same session
- Simple, isolated tasks
- Context files are current and AI has just read them

## Examples

**After research**:
```
> Be aware, I've completed authentication research. OAuth2 with PKCE is recommended but has integration complexities with our existing session management. I'm about to run /level-2-structure.

AI: Got it - OAuth2 validated but integration challenges discovered. Ready to help define system boundaries with those constraints in mind.

> /level-2-structure context/level-1-approach-context.yml
```

**After stakeholder feedback**:
```
> Be aware, stakeholders approved our Level 1 approach but added a requirement for audit logging throughout the system. I'm about to incorporate this into our component design.

AI: Understood - technical approach approved with new audit logging requirement. This will affect component boundaries and data flow. Ready to help integrate this.

> /level-2-structure context/level-1-approach-context.yml
```

**After TODO work**:
```
> Be aware, I've processed the data model validation TODOs. We need both relational and document storage, plus there's a performance requirement we missed. I'm about to reprocess Level 3 specifics.

AI: Thanks for the update - hybrid storage patterns needed plus new performance constraints. These could significantly impact implementation specifics. Ready to help reprocess.

> /level-3-specifics context/level-2-structure-context.yml
```

## Why This Works

- **Prevents assumptions**: AI knows what's changed since last interaction
- **Improves recommendations**: AI suggestions account for current reality
- **Saves time**: Less back-and-forth to establish working context
- **Maintains quality**: Decision quality stays consistent across sessions

The goal is shared understanding before complex work, not perfect documentation.