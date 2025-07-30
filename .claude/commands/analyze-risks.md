## Usage
```
/analyze-risks <input-description> [--focus=<risk-category>] [--roles=<role1,role2,...>]
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/analyze/research-protocol.md` (Industry research and evidence-based analysis - use Risk Assessment research type)
Load: `.claude/patterns/analyze/stakeholder-analysis.md` (Role-based perspective integration)
Load: `.claude/patterns/analyze/report-templates.md` (Report structure and output format - use Risk Assessment template)
Load: `.claude/patterns/general/checkpoints.md` (Transient decisions - this is research/analysis)

## Purpose
Identify, analyze, and categorize risks with mitigation strategies using role-based expertise and industry research.

## Process

### 1. Extract Topic
- Apply topic extraction logic for filename generation
- Sanitize and format for consistent naming

### 2. Load Role-Based Context
- Scan `.claude/roles/` for available roles
- Auto-detect relevant roles or use --roles parameter
- Load role definitions and extract risk patterns

### 3. Conduct Industry Risk Research
- Use WebSearch for industry risk patterns and failure cases
- Research project failure case studies and post-mortems
- Find industry risk reports and security advisories
- Look up common pitfalls and anti-patterns

### 4. Apply Risk Assessment Framework
- Use role-specific risk identification with industry evidence
- Apply risk discovery methods from research protocol
- Analyze likelihood and impact for each risk
- Apply risk prioritization matrix
- Develop role-informed mitigation strategies

### 5. Generate Risk Assessment Report
- Apply risk assessment report template
- Include role-based context and insights
- Provide monitoring plan with role-specific indicators
- Write to `docs/reports/risk-assessment-[topic]-[timestamp].md`

## Key Principles
- Must use WebSearch for industry research
- Cite all sources with URLs and access dates
- Use role-based expertise combined with industry evidence
- Provide specific, actionable mitigation strategies
- Include role-specific early warning indicators
- Focus on prevention and preparedness

## Output Summary
After report generation, provide:
- Report location
- Roles used for assessment
- Number of high/medium/low priority risks identified
- Top 3 critical risks from role perspectives