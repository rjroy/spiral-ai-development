# TODO Workflow Integration

**The Problem**: SAID phases generate TODO items that get lost in informal tracking or bypass the collaborative framework entirely.

**The Solution**: Structured commands for handling TODOs that maintain SAID's context preservation and collaboration principles.

## When to Use TODO Workflow

**Use for complex TODOs that need**:
- Multiple steps or decisions
- Research with unclear approach
- Cross-cutting concerns affecting multiple SAID levels
- Stakeholder input at decision points

**Skip for simple TODOs**:
- Single actions (fix typo, add comment)
- Well-defined implementation with clear approach
- Routine maintenance following established patterns

## Core Commands

```bash
/extract-todo-context     # Pull TODO from SAID artifacts with source context
/generate-todo-context    # Create context for newly discovered TODOs
/decompose-todo          # Break complex TODOs into atomic tasks
/work-on-todo           # Execute TODO with collaboration checkpoints
/said-todo-sync         # Integrate results back into SAID contexts
```

## Basic Workflow

**1. Extract or generate TODO context**
```bash
# From existing document
/extract-todo-context docs/level-1-report.md "Database schema needs validation"

# From new discovery
/generate-todo-context "Missing authentication error handling"
```

**2. Decompose if complex**
```bash
# If TODO has multiple parts
/decompose-todo context/todo/database-validation/todo-context.yml
# Creates atomic subtasks you can work on independently
```

**3. Work on atomic tasks**
```bash
/work-on-todo context/todo/database-validation/schema-review/todo-context.yml
# AI provides collaboration checkpoints for decisions
```

**4. Integrate results**
```bash
/said-todo-sync context/todo/database-validation
# Updates affected SAID contexts, archives deliverables, cleans up
```

## Example: Authentication Research TODO

**Extracted from Level 1 transition report**:
```bash
/extract-todo-context docs/level-1-to-2-transition.md "Authentication approach needs deeper evaluation"
```

**Complex enough to decompose**:
```bash
/decompose-todo context/todo/auth-evaluation/todo-context.yml
# Creates subtasks: security-analysis, integration-patterns, implementation-complexity
```

**Work on specific aspect**:
```bash
/work-on-todo context/todo/auth-evaluation/security-analysis/todo-context.yml
# AI asks about threat model, compliance requirements, presents options
```

**Integrate findings**:
```bash
/said-todo-sync context/todo/auth-evaluation
# Updates Level 2 context with security requirements and constraints discovered
```

## What You Get

- **No lost TODOs**: Systematic capture and tracking
- **Context preservation**: Source relationships maintained
- **Collaborative execution**: AI checkpoints for complex decisions
- **Integration**: Results feed back into SAID contexts properly
- **Quality consistency**: Same standards as main SAID work

The goal is handling complex TODOs without losing SAID's collaborative benefits or context integrity.