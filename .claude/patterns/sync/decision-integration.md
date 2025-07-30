# Decision Integration Patterns

## Decision Documentation Format

### Standard Decision Structure
```markdown
### Decision N: [Decision Title from Report]
**Selected Option**: [Chosen Option Name]
**Rationale**: [Why this option was selected]
**Alternatives Considered**: [Brief summary of other options]
**Implementation Requirements**: [Key requirements from selected option]
**Trade-offs Accepted**: [Acknowledged limitations/cons]
**Decision Date**: [YYYY-MM-DD]
**Source Analysis**: [Reference to options analysis report]

**Key Considerations:**
- [Important factor 1 from analysis]
- [Important factor 2 from analysis]
- [Important factor 3 from analysis]
```

## Integration by Context Type

### Project Context Integration
- Add to "## Key Decisions" section
- Update affected constraints or assumptions
- Ensure consistency with project identity

### Component/Feature Context
- Document in relevant technical section
- Update implementation requirements
- Note integration impacts

### TODO Context Integration
- Document decision in task context
- Update completion status if blockers resolved
- Add implementation tasks if new work created

## Validation Checklist

### Before Integration
- Selected option clearly identified in source report
- Decision rationale matches option analysis
- Implementation requirements captured
- Trade-offs and limitations documented

### After Integration
- Context file maintains proper Markdown structure
- Decision traceability is clear
- YAML frontmatter updated with timestamp
- No existing context lost or corrupted