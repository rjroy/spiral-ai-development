## Usage
```
/analyze-problem <input-description> [--roles=<role1,role2,...>]
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/analyze/research-protocol.md` (Industry research and evidence-based analysis - use Problem Validation research type)
Load: `.claude/patterns/analyze/stakeholder-analysis.md` (Multi-role perspective integration)
Load: `.claude/patterns/analyze/report-templates.md` (Report structure and output format - use Problem Validation template)
Load: `.claude/patterns/general/checkpoints.md` (Transient decisions - this is research/analysis)

## Purpose
Analyze problem space to identify core issues, user needs, and validate problem importance through stakeholder perspectives.

## Process

### 1. Extract Topic
- Apply topic extraction logic for filename generation
- Sanitize and format for consistent naming

### 2. Load Stakeholder Perspectives (if applicable)
- Scan `.claude/roles/` for available roles
- Auto-detect or use --roles parameter
- Load role definitions and extract problem validation criteria

### 3. Conduct Problem Space Research
- Use WebSearch for industry research on similar problems
- Research existing solutions and their limitations
- Find market studies and user research reports
- Gather evidence about problem space and user pain points

### 4. Problem Analysis
- Apply problem validation research framework from research protocol
- Assess current state and user impact
- Validate through stakeholder lenses using industry evidence
- Define scope boundaries and business context

### 5. Generate Validation Report
- Apply problem validation report template
- Include stakeholder validation matrix
- Provide business prioritization assessment
- Write to `docs/reports/problem-validation-[topic]-[timestamp].md`

## Key Principles
- Must use WebSearch for industry research
- Cite all sources with URLs and access dates
- Focus on problem understanding, not solutions
- Require evidence for problem claims
- Emphasize user perspective and validation
- Focus on problem constraints and requirements, not implementation solutions

## Output Summary
After report generation, provide:
- Report location
- Problem statement (one line)
- Validation status (validated/needs-validation/invalidated)
- Stakeholder consensus level (if roles used)
- Business priority assessment
- Key user groups affected