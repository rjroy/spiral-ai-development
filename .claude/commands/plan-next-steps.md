## Usage
```
/plan-next-steps <current-phase> [context-file]
```

## Required Patterns
Load: `.claude/patterns/general/core.md` (core command memory)
Load: `.claude/patterns/plan/action-planning.md` (Action prioritization, next steps structure, and transition scenarios)
Load: `.claude/patterns/general/checkpoints.md` (Consequential decisions - confirm transition strategy)

## Purpose
Generate detailed transition plans based on current phase outcomes with prioritized actions and risk mitigation.

## Process

### 1. Current State Analysis
- Apply Current State Analysis Framework from action-planning.md
- Assess completion status of current phase
- Identify unresolved issues and their blocking impact
- Evaluate outcomes and lessons learned
- Review critical decisions and constraints

### 2. Next Phase Planning
- Apply Next Phase Planning from transition scenarios
- Determine appropriate next phase based on outcomes
- Identify prerequisites and blocking issues
- Assess resource and capability needs
- Define success criteria for transition

### 3. Action Plan Creation
- Apply action planning framework and guidelines
- Rank actions by criticality and dependency
- Identify parallel vs. sequential activities
- Assign ownership and realistic timelines
- Include risk mitigation strategies for transitions

### 4. Generate Next Steps Document
- Apply standard next steps template
- Include transition assessment and readiness evaluation
- Provide specific, actionable tasks with clear success criteria
- Document key risks and mitigation approaches

## Key Principles
- All prerequisites must have clear validation criteria
- Action items must be specific and measurable
- Risk mitigation must address key failure modes
- Timeline estimates must be realistic
- Focus on actionable tasks, not aspirational statements

## Context File Support
Optional context file provides additional information about:
- Previous decisions and constraints
- Project history and lessons learned
- Stakeholder requirements and priorities
- Resource limitations and capabilities

## Quality Standards
- Team understands what needs to be done next
- Prerequisites are actionable and measurable
- Risk mitigation addresses key failure modes
- Timeline and resource estimates are realistic
- Success criteria defined for transition