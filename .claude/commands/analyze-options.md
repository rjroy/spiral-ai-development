## Usage
```
/analyze-options <input-description> [--roles=<role1,role2,...>]
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/analyze/research-protocol.md` (Industry research and evidence-based analysis)
Load: `.claude/patterns/analyze/stakeholder-analysis.md` (Role-based perspective integration)
Load: `.claude/patterns/analyze/report-templates.md` (Report structure and output format - use Options Analysis template)
Load: `.claude/patterns/general/checkpoints.md` (Transient decisions - this is research/analysis)

## Purpose
Research and present multiple viable approaches with objective pros/cons analysis incorporating stakeholder perspectives.

## Process

### 1. Extract Topic
- **File path input**: Extract filename without extension
- **Text input**: Extract 1-2 relevant keywords
- **Sanitize**: Lowercase, replace spaces/special chars with hyphens
- **Fallback**: Use "general" if no clear topic

### 2. Load Stakeholder Perspectives (if applicable)
- Scan `.claude/roles/` for available roles
- Auto-detect or use --roles parameter
- Load role definitions and extract evaluation criteria

### 3. Conduct Industry Research
- Use WebSearch for current best practices, standards, trends
- Research real-world implementations and case studies
- Find performance benchmarks from authoritative sources
- Look up recent technology surveys and industry reports
- Identify 2-3 fundamentally different approaches

### 4. Evidence-Based Analysis
- Cite industry sources for all technical claims
- Reference real benchmarks for resource requirements
- Use documented case studies for complexity evaluation
- Include maintenance data from industry reports
- Assess through stakeholder lenses using industry evidence

### 5. Generate Comprehensive Report
- Apply standard options analysis report template
- Include comparative analysis and stakeholder preference matrix
- Provide selection guidance based on scenarios
- Write to `docs/reports/options-analysis-[topic]-[timestamp].md`

## Key Principles
- Must use WebSearch for industry research
- Cite all sources with URLs and access dates
- Present options objectively without bias
- Include both conventional and innovative approaches
- Focus on decision-enabling information
- Provide evidence-based recommendations

## Output Summary
After report generation, provide:
- Report location
- Number of options analyzed
- Stakeholder roles consulted (if any)
- Key decision criteria identified
- Recommended selection approach