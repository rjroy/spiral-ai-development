# Report Templates

## Universal Report Infrastructure

### YAML Frontmatter Structure
```yaml
---
type: [options-analysis|risk-assessment|problem-validation]
topic: [extracted-topic]
generated: YYYY-MM-DD HH:mm:ss
input: <brief summary of input>
roles: [list of roles if used]
---
```

### File Naming Convention
- **Options Analysis**: `docs/reports/options-analysis-[topic]-YYYY-MM-DD-HHmmss.md`
- **Risk Assessment**: `docs/reports/risk-assessment-[topic]-YYYY-MM-DD-HHmmss.md`
- **Problem Validation**: `docs/reports/problem-validation-[topic]-YYYY-MM-DD-HHmmss.md`
- Use timestamp format: `date "+%Y-%m-%d-%H%M%S"`
- Ensure directory exists: `docs/reports/`

### Topic Extraction Logic
- **File path input**: Extract filename without extension
- **Text input**: Extract 1-2 most relevant keywords from description/problem/risk
- **Sanitization**: Convert to lowercase, replace spaces and special characters with hyphens
- **Length limit**: Keep topic under 20 characters, truncate if needed
- **Fallback**: Use "general" if no meaningful topic can be extracted

### Universal Quality Standards
- Must use WebSearch for industry research when applicable
- Cite all sources and include references section
- Use role-based expertise when roles are specified
- Provide evidence-based analysis and claims
- Include specific, actionable recommendations

## Options Analysis Report Template

### Complete Report Structure
```markdown
---
type: options-analysis
topic: [extracted-topic]
generated: YYYY-MM-DD HH:mm:ss
input: <brief summary of input>
roles: [list of roles if used]
---

# Options Analysis Report

## Context Summary
[Brief summary of what needs to be decided]

## Stakeholder Perspectives
### Roles Consulted
[List of roles used for this analysis with brief description]

### Key Stakeholder Priorities
[What each role values most in a solution]

## Option 1: [Approach Name]
### Description
[Clear explanation of this approach]

### Pros
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]

### Cons
- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

### Implementation Requirements
- Skills needed: [List]
- Technologies: [List]
- Estimated effort: [Assessment]
- Key dependencies: [List]

### Stakeholder Impact
- **[Role 1]**: [How this option affects them]
- **[Role 2]**: [How this option affects them]

## Option 2: [Approach Name]
[Same structure as Option 1]

## Option 3: [Approach Name]
[Same structure as Option 1]

## Comparative Analysis
| Criteria | Option 1 | Option 2 | Option 3 |
|----------|----------|----------|----------|
| Complexity | [Rating] | [Rating] | [Rating] |
| Performance | [Rating] | [Rating] | [Rating] |
| Maintainability | [Rating] | [Rating] | [Rating] |
| Resource Requirements | [Rating] | [Rating] | [Rating] |
| Risk Level | [Rating] | [Rating] | [Rating] |

## Selection Guidance
- **Choose Option 1 if**: [Conditions favoring this option]
- **Choose Option 2 if**: [Conditions favoring this option]
- **Choose Option 3 if**: [Conditions favoring this option]

## Decision Framework
[Key questions to help make the final choice]

## References and Sources
[List all sources used in research with URLs and access dates]
```

### Analysis Approach Guidelines
- Provide detailed technical recommendations with specific implementation guidance
- Focus on research and comparison with emphasis on trade-off analysis
- Include clear preferred option when evidence supports it

### Summary Format for User
After generating report, provide brief summary stating:
- Report location
- Number of options analyzed
- Stakeholder roles consulted (if any)
- Key decision criteria identified
- Recommended selection approach

## Risk Assessment Report Template

### Complete Report Structure
```markdown
---
type: risk-assessment
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

### Summary Format for User
After generating report, provide brief summary stating:
- Report location
- Roles used for assessment
- Number of high/medium/low priority risks identified
- Top 3 critical risks from role perspectives

## Problem Validation Report Template

### Complete Report Structure
```markdown
---
type: problem-validation
topic: [extracted-topic]
generated: YYYY-MM-DD HH:mm:ss
input: <brief summary of input>
roles: [list of roles if used]
---

# Problem Validation Report

## Problem Statement
[Clear, one-sentence problem description]

## Stakeholder Validation Context
### Roles Consulted
[List of roles used for validation with brief description]

### Stakeholder Problem Perspectives
[How each role views and experiences the problem]

## Current State Analysis
- How users currently handle this
- Pain points and limitations
- Workarounds being used
- Cost of current approach

## User Impact Assessment
- Primary user groups affected
- User constraints and contexts
- User success criteria
- Evidence of user need

## Problem Validation
- Evidence this is a real problem
- User validation data/feedback
- Market indicators (if applicable)
- Consequences of not solving

## Stakeholder Validation Matrix
| Role | Problem Valid? | Priority | Key Pain Points |
|------|----------------|----------|-----------------|
| [Role 1] | [Yes/No/Partial] | [High/Med/Low] | [Main issues] |
| [Role 2] | [Yes/No/Partial] | [High/Med/Low] | [Main issues] |
| [Role 3] | [Yes/No/Partial] | [High/Med/Low] | [Main issues] |

## Business Prioritization
- Business impact assessment
- Strategic alignment score
- Resource investment justification
- Timing considerations

## Scope Boundaries
- What's included in problem scope
- What's explicitly excluded
- Potential scope creep areas
- Related problems not being addressed

## Recommendations
- Problem prioritization assessment
- Suggested next steps for validation
- Areas needing additional research

## References and Sources
[List all sources used in research with URLs and access dates]
```

### Summary Format for User
After generating report, provide brief summary stating:
- Report location
- Problem statement (one line)
- Validation status (validated/needs-validation/invalidated)
- Stakeholder consensus level (if roles used)
- Business priority assessment
- Key user groups affected

### Quality Standards for Problem Validation
- Focus on problem understanding, not solutions
- Require evidence for problem claims backed by industry research
- Focus on problem constraints and requirements including technical factors, not implementation solutions
- Emphasize user perspective and validation supported by market data