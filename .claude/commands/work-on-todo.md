## Usage
```
/work-on-todo <todo-context-file>
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/general/checkpoints.md` (Implementation decisions - when to pause vs proceed)

## Purpose
Execute atomic TODO items with appropriate human collaboration.

## Process

### 1. Understand Context
- Load TODO context and parse requirements
- Identify deliverables and constraints
- Note any undefined areas that need clarification

### 2. Validate Understanding
Present to user:
- "Here's what I understand needs to be done..."
- "Success looks like..."
- "I'll need clarification on..." (if applicable)

### 3. Execute with Smart Checkpoints
- For consequential decisions (language, framework, architecture): Always ask
- For implementation details (naming, structure): Follow project patterns
- For new discoveries: "I found X, which means Y. Should I proceed with Z?"

### 4. Complete and Document
```
context/todo/{todo-name}/execution/
├── deliverables/        # The actual work products
├── execution-log.md     # What was done and why
├── lessons-learned.md   # Insights for future work
└── integration.md       # How this fits with parent context
```

## Key Principles
- Don't interrupt for trivial decisions
- Bundle related questions together
- Show work in progress naturally
- Match user's communication style

## Example Flow
```
User: /work-on-todo context/todo/add-user-auth/todo-context.md

AI: I need to implement user authentication. Based on the context, you need:
- JWT-based auth with refresh tokens
- Integration with existing User model
- Protected API endpoints

One key decision: Should I use Passport.js (more features, heavier) or
implement lightweight JWT handling directly? The project already uses
Express but no auth library yet.

User: Let's keep it lightweight

AI: Got it. I'll implement direct JWT handling.
*[Shows implementation progress naturally]*
Found that we need to decide on token expiry times - using industry
standard 15min access/7day refresh unless you prefer different?

User: That's fine

AI: *[Completes implementation, shows result]*
Done! Created the auth module with middleware, token handling, and tests.
All files are in context/todo/add-user-auth/execution/deliverables/
```