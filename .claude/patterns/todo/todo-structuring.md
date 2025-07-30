# TODO Structuring Patterns

## SAID Integration

All TODOs in SAID use structured contexts for consistency and traceability.

## Standard TODO Context Template

```markdown
# TODO: [Generated Name]

[User-provided TODO description]

---
todo_type: "user_generated"
---

## Scope
**Deliverable**: What needs to be produced
**Boundaries**: What is and isn't included
**Success Criteria**: How to know when complete

## Complexity
**Estimated Effort**: Hours/days/weeks

## Integration
**SAID Target**: Which context/phase this fits into
**Dependencies**: What needs to happen first

## Next Steps
- [ ] [Immediate action needed]
- [ ] [Follow-up action]
```

## Processing Route Recommendations

### Route 1: Immediate Sync
**When**: TODO fits into existing SAID context
**Action**: Add to current project context using `/sync-context`
**Indicators**: 
- Related to ongoing work
- Clear integration point
- Enhances existing component

### Route 2: Decomposition Required
**When**: TODO is complex and needs breaking down
**Action**: Use `/decompose` with appropriate type definition
**Indicators**: 
- Multiple components affected
- Unclear scope that needs clarification
- Architectural impact
- > 1 day estimated effort

### Route 3: Direct Execution
**When**: TODO is well-defined but benefits from SAID structure
**Action**: Ready to implement with `/work-on-todo`
**Indicators**: 
- Clear deliverable
- Defined scope
- Medium complexity (1-8 hours)
- Benefits from structured approach

## Scope Clarification Questions

### Deliverable Clarity
- What exactly needs to be produced?
- What are the acceptance criteria?
- How will success be measured?

### Boundary Definition
- What is explicitly included?
- What is explicitly excluded?
- Where are the integration points?

### Complexity Evaluation
- Is this atomic (single task)?
- What are the dependencies?
- What decisions need to be made?

## Quality Checks

### Essential Elements
- [ ] Clear deliverable and scope boundaries
- [ ] Correct processing route selected
- [ ] Clear SAID integration path
- [ ] Actionable next steps

### Principles
- Focus on clarity and actionability
- Provide clear integration guidance
- Keep scope boundaries tight to prevent feature creep