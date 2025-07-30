# Conversational Memory

Static instructions miss nuances. Good interns keep notebooks:
- "Sarah prefers user-friendly error messages"
- "When John says 'clean', he means minimal dependencies"
- "Team tried Redis - bad experience, don't suggest"

## Structure
```
.claude/memory/
├── preferences.md     # Style and approach preferences
├── patterns.md       # What works, what doesn't
└── nuances.md        # Reading between the lines
```

## Example Entries

**preferences.md**
```
- Prefers conversational over formal docs
- Skeptical of over-engineering
- "Setup rules" = create principles, not prescriptions
```

**patterns.md**
```
- Works: Meta-application, explaining "why" before "what"
- Avoid: Too many templates, obvious confirmations
- Mental model: AI as evolving relationship
```

**nuances.md**
```
- "Apply pressure" = understand exploring vs executing
- User doubts = explore, don't rush to fix
- "Crisis of faith" → fundamental redesign opportunity
```

## Implementation

Simple start: Commands check memory for preferences
```
if (memory.has("bundled questions preferred")) {
    // Group questions before asking
}
```

Future: Automatic pattern detection, cross-session learning.

## The Vision

Six months later: "I remember you prefer bundled checkpoints and conversational docs. Should I apply our adaptive patterns?"

That's a collaborator, not a tool.