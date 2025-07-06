# SAID Implementation Guide

_How to apply Spiral AI Development in practice_

---

## The SAID Methodology

Spiral development approach with progressive detail levels that handles changing requirements, timeline pressure, and context preservation.

### Progressive Detail Levels

1. **Level 0**: Vision clarity (Core purpose understood)
2. **Level 1**: Approach viability (Solution approach validated)
3. **Level 2**: Structure definition (System boundaries defined)
4. **Level 3**: Implementation specifics (Buildable specifications)
5. **Level 4**: Working implementation (Production-ready code)

### Spiral Navigation Rules

- **Advance when**: Critical unknowns resolved for current level
- **Defer when**: Decisions can be explicitly documented for later
- **Navigate backward when**: Discoveries invalidate earlier assumptions
- **Always**: Maintain context integrity across transitions

### Prototype Phase (When Risk Is Discovered)

**Purpose**: Validate highest-risk technical assumptions when they're identified. May occur before Level 0, during Level 1 investigation, or whenever core risks surface.

**Activities**:
- Identify 3 highest technical risks
- Build throwaway prototypes to test feasibility
- Validate integration points with real systems
- Document discovered complexities

**Success Gate**: Core technical approach proven viable
**Failure Response**: Pivot approach or abort before sunk cost

---

## Context Preservation

### Context Requirements
```yaml
context_manifest:
  critical_requirements: [documented and traced]
  key_decisions: [with rationale and alternatives]
  discovered_constraints: [impact assessment included]
  semantic_checksum: [core purpose + users + metrics + constraints]
```

### Context Priming Pattern
Brief context orientation before SAID command execution ensures state continuity across sessions.

**When to Use**:
- Resuming after time gaps
- Post-discovery work
- Phase transitions
- When significant context has changed

**How to Use**:
```
> Be aware, I've [completed work]. [Current state]. I'm about to [intended action].
AI: [Acknowledgment and readiness confirmation]
> /level-2-structure context/level-1-approach-context.yml
```

---

## Common Workflow Patterns

### Phase Completion Workflow
```bash
/said-context-sync level-0-vision
/generate-next-steps level-0-vision
/generate-phase-report level-0-vision
```

### Context Recovery (when context is lost)
```bash
/said-context-sync current-phase context/project-context.yml
/generate-next-steps current-phase context/project-context.yml
```

### Starting New Level
```bash
# Context priming first
> Be aware, I've completed level-1-approach. The technical approach is validated. I'm about to start level-2-structure.
> /level-2-structure context/level-1-approach-context.yml
```

---

## Troubleshooting

### When Context Gets Lost
1. Run `/said-context-sync` with last known good context
2. Review phase reports to reconstruct decisions
3. Use git history to trace requirement changes
4. Regenerate context from artifact discovery

### When AI Suggestions Don't Fit
1. Check domain calibration - may need to reduce AI involvement
2. Verify context includes relevant constraints
3. Ask AI to explain assumptions behind suggestions
4. Consider if you're in wrong spiral level for the decision

### When Timeline Pressure Mounts
1. Activate appropriate pressure protocol
2. Document what's being deferred
3. Maintain context preservation above all else
4. Communicate trade-offs clearly to stakeholders

---

## Pressure Adaptation Protocols

### Timeline Pressure Response

**Moderate Pressure**:
- Combine levels where safe
- Use proven patterns instead of custom solutions
- Maintain context preservation

**High Pressure**:
- Skip to Level 3 with templates
- Plan cleanup work explicitly
- Never abandon context preservation

**Extreme Pressure**:
- Emergency mode with damage control
- Focus only on critical functionality
- Document all shortcuts taken

### Quality Gates Under Pressure

**Never Compromise**:
- Security review
- Data integrity
- Basic functionality
- Context preservation

**Defer If Needed**:
- Performance optimization
- UI polish
- Comprehensive documentation

---

## Git Workflow Integration

### Branching Strategy

**Descriptive Branch Names**:
- `feature/user-authentication`
- `prototype/test-new-api`
- `feature/level-1-technical-approach`
- `fix/bug-description`

**Simple GitHub Flow**:
```
main
├── feature/descriptive-name
├── fix/bug-description
├── docs/what-youre-documenting
└── prototype/experiment-name
```

### Context Preservation Through Git
- Use meaningful commit messages that explain decisions
- Document major choices in context files
- PR descriptions capture important discussions
- Git history preserves your development journey

### Code Review Practices

**For Simple Domains**:
- Lighter review for straightforward changes
- Focus on integration and consistency

**For Complex Domains**:
- Involve team members with relevant expertise
- Take time to review architectural implications

**For Extreme Domains**:
- Multiple reviewers may be valuable
- Document review decisions and rationale

---

## TODO Workflow Integration

### When to Use TODO Workflow
- Multi-step work items requiring 3+ activities
- Cross-cutting concerns affecting multiple levels
- Research tasks with approach uncertainty
- Work items needing stakeholder input at decision points

### TODO Commands
- `/extract-todo-context` - Extract TODOs from SAID artifacts
- `/generate-todo-context` - Create contexts for new TODOs
- `/decompose-todo` - Break complex TODOs into atomic tasks
- `/work-on-todo` - Execute atomic TODOs with checkpoints
- `/said-todo-sync` - Integrate results back into SAID contexts

