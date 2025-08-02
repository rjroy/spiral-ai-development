# SAID Implementation Guide

_How to apply Spiral AI Development in practice_

---

## The SAID Methodology

Spiral development approach with progressive detail levels that handles changing requirements, timeline pressure, and context preservation.

### Progressive Detail Levels

#### Level 0: Problem + Risk Clarity
**Deliverables**: Problem validated with evidence, key risks identified with mitigation strategies, stakeholder needs documented

**Workflow Pattern**:
```bash
/analyze-problem [input] → problem-validation-[timestamp].md
/sync-context problem-validation-[timestamp].md
/analyze-risks [context] → risk-assessment-[timestamp].md
/sync-context risk-assessment-[timestamp].md
```

**Complete When**:
- Problem statement backed by evidence of user need
- Top 3 project risks identified with mitigation plans
- Stakeholder perspectives documented
- Context integrates problem validation and risk insights

#### Level 1: Approach Decision
**Deliverables**: 2-3 viable approaches analyzed, decision made with documented rationale, technical feasibility validated

**Workflow Pattern**:
```bash
/analyze-options [context] → options-analysis-[timestamp].md
[human review and decision]
/sync-decision [context] [options-report] [chosen-option]
/sync-context [updated-context]
```

**Complete When**:
- Multiple viable approaches evaluated with pros/cons
- Technical feasibility validated for chosen approach
- Decision rationale documented with alternatives considered
- Context reflects chosen approach and reasoning

#### Level 2: Structure Definition
**Deliverables**: System boundaries defined, component interfaces specified
**Workflow**: `/decompose .agent/layers/project.md [parent-context]`

#### Level 3: Implementation Specifics
**Deliverables**: Buildable specifications, detailed component designs
**Workflow**: `/decompose .agent/layers/component.md [parent-context]`

#### Level 4: Working Implementation
**Deliverables**: Production-ready code, tested features
**Workflow**: `/decompose .agent/layers/feature.md [parent-context]`

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
> /decompose .agent/layers/project.md context/approach-context.md
```

---

## Common Workflow Patterns

### Complete Level 0 (Problem + Risk Clarity)
```bash
# Problem analysis
/analyze-problem "[your problem description]"
/sync-context docs/reports/problem-validation-[topic]-[timestamp].md

# Risk assessment
/analyze-risks context/project-context.md
/sync-context docs/reports/risk-assessment-[topic]-[timestamp].md

# Verify completion
# Can you explain the core problem in one sentence?
# Are the top 3 risks identified with mitigation plans?
```

### Complete Level 1 (Approach Decision)
```bash
# Options analysis using integrated context
/analyze-options context/project-context.md
# [Human review of options-analysis-[timestamp].md]

# Decision integration
/sync-decision context/project-context.md docs/reports/options-analysis-[topic]-[timestamp].md "[chosen option]"
/sync-context context/project-context.md

# Verify completion
# Do you have a chosen technical approach with documented rationale?
# Are alternative approaches preserved for future reference?
```

### Context Recovery (when context is lost)
```bash
/sync-context current-phase context/project-context.md
/plan-next-steps current-phase context/project-context.md
```

### Starting New Layer
```bash
# Context priming first
> Be aware, I've completed approach validation. The technical approach is validated. I'm about to start structure definition.
> /decompose .agent/layers/project.md context/project-context.md
```

---

## Troubleshooting

### When Context Gets Lost
1. Run `/sync-context` with last known good context
2. Review context files to reconstruct decisions
3. Use git history to trace requirement changes
4. Regenerate context from artifact discovery

### When AI Suggestions Don't Fit
1. Verify context includes relevant constraints
2. Ask AI to explain assumptions behind suggestions
3. Consider if you're in wrong spiral level for the decision

### When Timeline Pressure Mounts
1. Activate appropriate pressure protocol
2. Document what's being deferred
3. Maintain context preservation above all else
4. Communicate trade-offs clearly to stakeholders

---

## Pressure Adaptation Guidelines

### Timeline Pressure

The concepts of _Moderate_, _High_, and _Extreme_ are subjective. They are provided here to illustrate common adaptions.

**Moderate Pressure**:
- Combine levels where safe
- Use proven patterns instead of custom solutions
- Maintain context preservation

**High Pressure**:
- Skip to Level 3 using context priming instead of context files
- Follow the remaining processes
- Maintain context preservation of what you can

**Extreme Pressure**:
- Emergency mode with damage control
- Focus only on critical functionality

**Recovery**:
- When the pressure is over
- Recover context using `/sync-context` when pressure subsides
- Use `/create-todo` to find cleanup tasks that need to occur

---

## Git Workflow with SAID

Use descriptive branch names that help your team understand what's happening:

```
feature/user-authentication
prototype/test-oauth-approach
level-1/technical-feasibility
fix/broken-login-redirect
```

**Protect your main branch** - require PRs for integration. Here's the GitHub Flow guide if you need a refresher.

**Consider matching code review depth to system complexity** - simple systems need basic review, complex systems need domain experts, critical systems need multiple expert reviewers. Teams might want a lightweight PR checklist to prompt thinking about tests, documentation, and context preservation.

**Preserve context in git**:

- Use meaningful commit messages that explain decisions
- Keep your SAID context files in the repository
- Reference important discussions in PR descriptions

That's it. Your existing git knowledge + descriptive naming + context preservation.

---

## TODO Workflow Integration

**Core Principle**: Use structured TODO commands for complex work while allowing direct execution for simple tasks.

### When to Use Full TODO Workflow

**Use structured commands for complex TODOs**:
- Multiple steps or decisions required
- Research with unclear approach
- Cross-cutting concerns affecting multiple SAID workflows
- Stakeholder input needed at decision points

**Execute directly for simple TODOs**:
- Single actions (fix typo, add comment)
- Well-defined implementation with clear approach
- Routine maintenance following established patterns

### TODO Commands

```bash
/create-todo                         # Create context for newly discovered TODOs
/decompose .agent/layers/todo.md     # Break complex TODOs into atomic tasks
/work-on-todo                        # Execute TODO with collaboration checkpoints
/sync-context                        # Integrate results back into SAID contexts
```

### Flexible Application

**You don't need strict step-by-step adherence**. The workflow provides structure when complexity warrants it, but simple TODOs can bypass formal commands entirely. The goal is maintaining SAID's collaborative benefits and context integrity for work that benefits from structure, while avoiding overhead for straightforward tasks.

