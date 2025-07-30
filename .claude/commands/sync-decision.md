## Usage
```
/sync-decision <context-file> <decision-report> <selected-option>
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/sync/decision-integration.md` (Decision documentation format and validation)
Load: `.claude/patterns/sync/template-detection.md` (File creation when context doesn't exist)
Load: `.claude/patterns/general/checkpoints.md` (Consequential decisions - always validate integration)

## Purpose
Integrate selected decisions from options analysis reports into context files with full traceability.

## Process

### 1. Parse Decision Report
- Extract selected option details, rationale, alternatives
- Identify decision context and implementation requirements
- Validate option exists in source report

### 2. Handle Context File
- **Exists**: Load and parse structure
- **Missing**: Detect template pattern, create from template
- **Malformed**: Suggest validation/repair

### 3. Preview Integration
Show user:
- Selected option summary
- Where decision will be documented
- How it fits with existing context
- Any affected constraints or assumptions

### 4. Integrate Decision
- Add decision using standard format
- Update YAML frontmatter timestamp
- Preserve all existing context
- Maintain Markdown structure

## Examples

### Basic Usage
```
/sync-decision context/project-context.md options-analysis.md "Option 2"
```

### Component Decision
```
/sync-decision context/auth-component.md auth-options.md "JWT with refresh tokens"
```

## Key Principles
- Always preview integration before writing
- Preserve full decision rationale, not just choice
- Include alternatives considered for future reference
- Maintain traceability to source analysis
- Create files from templates when needed

## Example Flow
```
User: /sync-decision context/project-context.md arch-options.md "Microservices Architecture"

AI: Found "Microservices Architecture" in arch-options.md:
- Rationale: Better scalability and team autonomy
- Trade-offs: Increased complexity, network overhead
- Requirements: Container orchestration, service mesh

Context file exists. Will add to "Key Decisions" section.

Preview integration:
### Decision 3: System Architecture Approach
**Selected Option**: Microservices Architecture
**Rationale**: Better scalability and independent team development
**Alternatives Considered**: Monolith (simpler but scaling limits), Modular Monolith (middle ground)
**Trade-offs Accepted**: Increased operational complexity, network latency

Proceed with integration? (y/n)

User: y

AI: Decision integrated into context/project-context.md
Updated timestamp in YAML frontmatter
All existing context preserved
```