## Usage
```
/create-todo-from-report <report-file>
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/todo/options-workflow.md` (Complete options process: detection, presentation, selection)
Load: `.claude/patterns/todo/todo-structuring.md` (TODO context template for selected option)
Load: `.claude/patterns/general/checkpoints.md` (Consequential decisions - always get user selection)

## Purpose
Extract options from reports, help users choose through collaborative selection, and generate focused TODO contexts for implementation.

## Process

### 1. Expert Analysis
- Apply document reviewer expertise to identify options regardless of format
- Extract descriptions, pros/cons, requirements from any presentation style
- Identify implicit alternatives and trade-offs

### 2. Present Options
- Show numbered list with clear pros/cons for each option
- Include effort estimates and key differentiators
- Provide recommendation with rationale

### 3. Interactive Selection
- Ask user which option to implement
- Respect user choice even if different from recommendation
- Clarify if selection is unclear

### 4. Generate TODO Context
- Create focused context using standard template
- Include specific details from selected option
- Provide integration guidance for next steps

## Key Principles
- Focus on option extraction and selection, not complex orchestration
- Always collaborative - present options and get user input
- Generate single focused TODO context per selected option
- Keep scope boundaries clear to prevent feature creep

## Example Flow
```
User: /create-todo-from-report docs/database-options-analysis.md

AI: Found 3 database approaches in the report:

## Available Options:
1. **PostgreSQL with Prisma** - Full-featured relational database
   - Pros: Strong consistency, rich queries, mature ecosystem
   - Cons: More complex setup, higher resource usage
   - Effort: Medium (schema design, ORM setup)

2. **SQLite for MVP** - Lightweight embedded database
   - Pros: Simple setup, no server needed, perfect for prototyping
   - Cons: Limited concurrent users, no distributed support
   - Effort: Low (just install and connect)

3. **MongoDB with Mongoose** - Document-based NoSQL
   - Pros: Flexible schema, rapid development, JSON-native
   - Cons: Eventual consistency, less mature tooling
   - Effort: Medium (learn NoSQL patterns)

## Recommendation
**Suggested Option**: 2 - SQLite for MVP
**Rationale**: Project is early stage, team wants to move fast, can migrate later

Which option would you like to implement?

User: Let's go with PostgreSQL, we'll need the features eventually

AI: Great choice! Generated TODO context for PostgreSQL implementation:

# TODO: Implement PostgreSQL Database with Prisma

Set up PostgreSQL database with Prisma ORM for the application

## Scope
**Deliverable**: Working PostgreSQL database with Prisma integration
**Boundaries**: Includes: DB setup, schema design, ORM config, basic CRUD. Excludes: migrations, advanced queries, performance tuning
**Success Criteria**: Can create, read, update, delete core entities

Recommended route: `/work-on-todo` - well-scoped implementation task
```