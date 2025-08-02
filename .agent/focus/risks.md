## Purpose
Identify, analyze, and categorize risks with mitigation strategies using role-based expertise and industry research.

## Goal
- Identify risk patterns

## Research Area
- Research industry risk patterns and failure cases
- Research project failure case studies and post-mortems
- Find industry risk reports and security advisories
- Look up common pitfalls and anti-patterns

### Risk Discovery Methods
- **Assumption extraction**: Identify implicit and explicit assumptions
- **Stress testing scenarios**: Test assumptions under extreme conditions
- **Role-specific risk patterns**: Apply expertise-based risk identification
- **Cross-role synthesis**: Combine insights from multiple perspectives
- **Emergent risk detection**: Identify risks from role interactions

### Analysis Guidelines
- Analyze likelihood and impact for each risk
- Apply risk prioritization matrix
- Develop role-informed mitigation strategies
- Use role-based expertise combined with industry evidence
- Provide specific, actionable mitigation strategies
- Prioritize prevention and preparedness
- Include role-specific early warning indicators

### Risk Classification
- **Category**: Technical/Implementation/Integration/Business/Operational
- **Likelihood**: Low/Medium/High with justification
- **Impact**: Low/Medium/High with consequences
- **Root Cause**: Why this risk exists

### Risk Prioritization
- Risk matrix plotting (likelihood × impact)
- Critical path impact assessment
- Cascade risk identification
- Timeline sensitivity analysis

### Mitigation Strategy Framework
- **Prevention**: How to reduce likelihood
- **Impact Reduction**: How to minimize consequences
- **Contingency**: What to do if it happens
- **Risk Transfer**: Options for shifting risk

### Validation Methods
- **Assumption validation**: Methods to test critical assumptions
- **Early warning indicators**: Signals to watch for
- **Risk trigger identification**: Specific activation conditions
- **Monitoring mechanisms**: Ongoing assessment methods

### Risk Interconnection Analysis
- How risks might amplify each other
- Sequential failure patterns
- Common mode failures
- System-wide vulnerabilities

### Monitoring and Response
- **Review Frequency**: When to reassess risks
- **Key Indicators**: Metrics to track
- **Escalation Triggers**: When to take action
- **Responsibility Matrix**: Who monitors what

### Contingency Planning
- **Resources needed**: For risk response
- **Decision trees**: When to activate responses
- **Communication plans**: Who to notify when
- **Recovery procedures**: How to restore operations

# Report Template
```markdown
---
type: risks
topic: [extracted-topic]
generated: YYYY-MM-DD HH:mm:ss
input: <brief summary of input>
roles: [list of roles used]
---

# Risk Assessment Report

## Executive Summary
[High-level risk overview with key concerns]

## Role-Based Assessment Context
### Selected Roles
[List of roles used for this assessment with brief expertise summary]

### Role-Specific Insights
[Key risk patterns and concerns identified through role-based analysis]

## Risk Matrix
| Risk | Likelihood | Impact | Priority | Category |
|------|------------|--------|----------|----------|
| [Risk 1] | [L/M/H] | [L/M/H] | [Score] | [Technical/Business/etc] |
| [Risk 2] | [L/M/H] | [L/M/H] | [Score] | [Technical/Business/etc] |

## Detailed Risk Analysis

### High Priority Risks

#### Risk: [Risk Name]
- **Category**: [Technical/Implementation/Integration/Business/Operational]
- **Description**: [What could go wrong]
- **Likelihood**: [Low/Medium/High] - [Justification]
- **Impact**: [Low/Medium/High] - [Consequences if it occurs]
- **Root Cause**: [Why this risk exists]

**Mitigation Strategies**:
- **Prevention**: [How to reduce likelihood]
- **Impact Reduction**: [How to minimize consequences]
- **Contingency**: [What to do if it happens]
- **Early Warning Signs**: [Indicators to watch for]

### Medium Priority Risks
[Same structure for medium priority risks]

### Low Priority Risks
[Same structure for low priority risks]

## Risk Interconnections
[How risks might cascade or amplify each other]

## Monitoring Plan
- **Review Frequency**: [When to reassess risks]
- **Key Indicators**: [Metrics to track]
- **Escalation Triggers**: [When to take action]
- **Responsibility Matrix**: [Who monitors what]

## Contingency Resources
[Resources needed for risk response]

## Risk Acceptance Recommendations
[Which risks might be acceptable vs. must-address]

## References and Sources
[List all sources used in research with URLs and access dates]
```

### Updated Output Summary
After generating report, provide brief summary stating:
- Report location
- Roles used for assessment
- Number of high/medium/low priority risks identified
- Top 3 critical risks from role perspectives
