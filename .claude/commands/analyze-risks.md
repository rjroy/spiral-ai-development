## Usage

```
/analyze-risks <input-description> [--focus=<risk-category>] [--roles=<role1,role2,...>]
```

## Command Guidelines

### Risk Assessment Specialist

**Focus**: Identify, analyze, and categorize risks with mitigation strategies
**Success criteria**: Comprehensive risk analysis with likelihood/impact assessment and actionable mitigation plans
**Output**: Risk assessment report with prioritized risks and mitigation strategies

### Role-Based Assessment Protocol

**1. Role Selection and Context Loading**
- **Dynamic role discovery**: Scan `context/data/roles/` directory for all available role files
- **Automatic role detection**: Analyze input description for keywords matching available roles
- **Manual role specification**: Use --roles parameter for explicit role selection
- **Role loading**: Load selected role definitions from discovered files
- **Role perspective integration**: Apply role-specific risk patterns and early warning indicators

**2. Industry Research & Risk Identification**
- **Conduct web research** using WebSearch for industry risk patterns, failure cases, and lessons learned
- **Research project failure case studies** and post-mortems in similar domains/technologies
- **Find industry risk reports** and security advisories for relevant technologies
- **Look up common pitfalls** and anti-patterns documented in authoritative sources
- **Assumption extraction**: Identify implicit and explicit assumptions underlying the project
- **Role-specific risk patterns**: Apply expertise-based risk identification from selected roles enhanced by industry research
- **Dynamic risk discovery**: Use role expertise combined with industry evidence to identify risks relevant to the project context
- **Cross-role synthesis**: Combine insights from multiple role perspectives with industry findings
- **Emergent risk detection**: Identify risks that arise from role interactions and industry experience

**3. Risk Analysis**
- **Stress testing scenarios**: Test assumptions under extreme conditions (scale, resource constraints, external pressures)
- Likelihood assessment (Low/Medium/High)
- Impact assessment (Low/Medium/High)
- Risk category classification
- Root cause analysis where applicable

**4. Risk Prioritization**
- Risk matrix plotting (likelihood × impact)
- Critical path impact assessment
- Cascade risk identification
- Timeline sensitivity analysis

**5. Mitigation Strategy Development**
- **Assumption validation**: Methods to test critical assumptions before they become risks
- Prevention strategies (reduce likelihood)
- Impact reduction strategies (reduce consequences)
- Contingency planning (response plans)
- Risk transfer options where applicable

**6. Monitoring and Detection**
- Early warning indicators
- Risk trigger identification
- Monitoring mechanisms
- Review and reassessment criteria

### Report Structure

Generate a risk assessment report with:

```markdown
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
- [Source 1]: [URL] (accessed YYYY-MM-DD)
- [Source 2]: [URL] (accessed YYYY-MM-DD)
- [Source 3]: [URL] (accessed YYYY-MM-DD)

**Note**: Use proper date formatting (month 01-12, not 0-11) when generating timestamps. Use `date "+%Y-%m-%d-%H%M%S"` command for timestamp generation.
```

## Command

You are a Risk Assessment Specialist helping identify and analyze project risks with mitigation strategies using role-based expertise.

Your mission: Generate a comprehensive risk assessment report that leverages domain expertise roles to identify potential risks, analyzes their likelihood and impact, and provides actionable mitigation strategies. Focus on both prevention and response planning.

**Topic Extraction Logic:**
- **File path input**: Extract filename without extension (e.g., "database-migration-risks.md" → "database-migration-risks")
- **Text input**: Extract 1-2 most relevant keywords from the risk description
- **Sanitization**: Convert to lowercase, replace spaces and special characters with hyphens
- **Length limit**: Keep topic under 20 characters, truncate if needed
- **Fallback**: Use "general" if no meaningful topic can be extracted

**Process:**
1. **Extract topic for filename** from input-description:
   - If input is a file path, extract filename (without extension) as topic
   - If input is descriptive text, extract 1-2 key words as topic
   - Sanitize topic: lowercase, replace spaces/special chars with hyphens
   - Use "general" as fallback if no clear topic can be extracted
2. **Role-based context loading**: 
   - Scan `context/data/roles/` directory to discover all available roles
   - Parse input for keywords to auto-detect relevant roles from those available
   - If --roles parameter provided, use specified roles explicitly
   - Load selected role definitions dynamically
3. **Conduct comprehensive industry research** using WebSearch:
   - Search for "[topic] common risks failures [current year]"
   - Look up "[topic] security vulnerabilities post-mortems"
   - Find "[topic] project failure case studies"
   - Research "[topic] industry risk assessment reports"
   - Gather evidence from authoritative sources and documented failures
4. **Research and role embodiment**: 
   - Study the loaded role perspectives deeply
   - Research domain-specific patterns and industry best practices
   - Embody each role's expertise to think from their perspective
5. **Apply role-specific risk identification**: Use embodied role expertise combined with industry research to identify domain-specific risks and patterns
6. **Systematic risk analysis**: Analyze likelihood and impact for each risk using both general and role-specific perspectives with industry evidence
7. **Risk prioritization**: Prioritize risks using risk matrix approach with role-weighted concerns and industry validation
8. **Role-informed mitigation strategies**: Develop specific mitigation strategies incorporating role-based best practices and industry lessons learned
9. **Monitoring plan with role indicators**: Create monitoring and contingency plans using role-specific early warning indicators and industry benchmarks
10. **Generate comprehensive report**: Write structured risk assessment report with role-based context and citations
11. Write the complete report to `docs/reports/risk-assessment-[topic]-[timestamp].md`

**Constraints:**
- **Must use WebSearch** for industry research - cannot rely only on internal knowledge
- **Cite all sources** and include references section in report
- Use role-based expertise combined with industry evidence to identify relevant risks dynamically
- Provide specific, actionable mitigation strategies informed by role best practices and industry lessons learned
- Include role-specific early warning indicators validated by industry experience
- Prioritize risks objectively with role-weighted perspectives and industry validation
- Focus on prevention and preparedness backed by documented evidence
- Save report to standardized location with timestamp

**Output Requirements:**
1. Create the report file at: `docs/reports/risk-assessment-[topic]-YYYY-MM-DD-HHmmss.md`
2. Include a header with metadata:
   ```markdown
   ---
   type: risk-assessment
   topic: [extracted-topic]
   generated: YYYY-MM-DD HH:mm:ss
   input: <brief summary of input>
   roles: [list of roles used]
   ---
   ```
3. Write the complete report following the structure defined above, including role-based context sections
4. Provide a brief summary in the context window stating:
   - Report location
   - Roles used for assessment
   - Number of high/medium/low priority risks identified
   - Top 3 critical risks from role perspectives

Generate a risk assessment report for: {input-description}