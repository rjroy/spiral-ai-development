## Usage
```
/create-todo <todo-description>
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/todo/todo-structuring.md` (Scope assessment, TODO context template and processing routes)
Load: `.claude/patterns/general/checkpoints.md` (Transient decisions - this is analysis/structuring)

## Purpose
Transform TODO descriptions into structured contexts for SAID integration.

## Process

### 1. Generate Context
- Apply standard TODO context template
- Clarify deliverable, boundaries, success criteria
- Identify SAID integration target

### 2. Recommend Processing Route
- **Immediate Sync**: Fits existing context → `/sync-context`
- **Decomposition**: Needs breakdown → `/decompose`
- **Direct Execution**: Well-defined → `/work-on-todo`

## Key Principles
- Generate single focused context per TODO
- Ensure clear scope boundaries to prevent feature creep
- Structure for optimal SAID integration

## Example Flow

```
User: /create-todo "Add user authentication to the application"

AI: Created SAID context:

# TODO: Add User Authentication System

Add user authentication to the application

## Scope
**Deliverable**: Complete auth system with login/logout, session management
**Boundaries**: Includes: user model, auth middleware, login/logout endpoints. Excludes: social login, password reset
**Success Criteria**: Users can register, login, access protected routes

## Integration
**SAID Target**: Core application architecture
**Dependencies**: Database schema finalization

## Next Steps
- [ ] Decompose into components (auth service, middleware, endpoints)
- [ ] Design user data model

Recommended route: `/decompose .claude/decompose-types/feature.md`
```