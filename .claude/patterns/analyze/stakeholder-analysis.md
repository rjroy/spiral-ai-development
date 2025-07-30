# Stakeholder Analysis Patterns

## Role-Based Context Loading

### Dynamic Role Discovery
- Scan `.claude/roles/` directory for available roles
- Auto-detect roles from input or use --roles parameter
- Load selected role definitions
- Extract evaluation criteria for each role

### Stakeholder Perspective Integration
- Identify what each role values in solutions
- Consider approaches favored by different stakeholders
- Assess each option through stakeholder lenses using industry evidence
- Include role-specific priorities in decision framework

## Multi-Stakeholder Evaluation

### Stakeholder Impact Analysis Template
```markdown
### Stakeholder Impact
- **[Role 1]**: [How this option affects them]
- **[Role 2]**: [How this option affects them]
- **[Role 3]**: [How this option affects them]
```

### Stakeholder Preference Matrix Template
```markdown
| Role | Option 1 | Option 2 | Option 3 | Key Concerns |
|------|----------|----------|----------|--------------|
| [Role 1] | [Preference] | [Preference] | [Preference] | [Main concerns] |
| [Role 2] | [Preference] | [Preference] | [Preference] | [Main concerns] |
| [Role 3] | [Preference] | [Preference] | [Preference] | [Main concerns] |
```

## Integration Guidelines

### When to Include Stakeholder Analysis
- Roles specified via --roles parameter
- Roles auto-detected from input context
- Complex decisions affecting multiple team members
- Cross-functional impact expected

### When to Skip Stakeholder Analysis
- Simple technical decisions with single domain impact
- Individual developer workflow optimizations
- Internal implementation details with no external visibility

### Stakeholder Readiness Assessment
- Capability gaps from each role's perspective
- Training requirements for different approaches
- Organizational change implications
- Communication needs across roles