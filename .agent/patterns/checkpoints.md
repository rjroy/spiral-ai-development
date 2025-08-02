# Checkpoint Patterns

## Transient Decisions (Research/Analysis)
**Proceed autonomously with:**
- Output format and structure choices
- Search strategies and tool selection
- Analysis organization
- Temporary file creation for analysis
- Research depth and breadth

**Only checkpoint if:**
- Missing critical information to even begin
- Contradictory or unclear requirements
- Access or permission issues
- User explicitly requested validation

## Consequential Decisions (Implementation)
**Always checkpoint before:**
- Programming language selection
- Framework or library choices (React vs Vue, Express vs Fastify)
- Architecture patterns (monolith vs microservices)
- Database or storage decisions
- External service integrations
- Data model changes affecting persistence
- Security-sensitive implementations

**Make reasonable decisions for:**
- Variable and function names (following project patterns)
- File organization (matching existing structure)
- Error handling style (consistent with codebase)
- Code formatting (using project standards)
- Implementation details (vector vs set for performance)
- Test structure (following project conventions)

## The Principle
Impact + Reversibility = Checkpoint Need
- High impact + Hard to reverse = Always ask
- Low impact + Easy to change = Just do it
- Uncertain impact = Brief explanation with escape valve