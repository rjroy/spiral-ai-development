# Project Context

This is the main project context file that provides vision and architecture overview. For detailed decisions and lessons, see the referenced files below.

## Related Context Files

- **[Decisions Made](./project/decisions-made.md)** - Key decisions integrated into the project
- **[Lessons Learned](./project/lessons-learned.md)** - Insights from research and mistake recovery
- **[Open Questions](./project/open-questions.md)** - Unresolved questions requiring multi-phased analysis

## Project Identity

**Purpose**: [Project purpose will be extracted from OVERVIEW.md]
**Primary Users**: [Primary user groups will be extracted from design documents]
**Success Metrics**: [Success criteria will be extracted from HIGH-LEVEL-DESIGN.md]

## Technical Approach

### Solution Architecture
[Technical approach will be defined through analysis and validation]

### Key Architectural Decisions
[Architectural choices will be documented as they are made]

### Technology Stack

**Core Technologies:**
```yaml
technology_decisions:
  - decision_area: "Backend Framework"
    selected_option: "[To be determined through /analyze solutions]"
    rationale: "[Why this was chosen]"
    alternatives_considered: ["[Option 1]", "[Option 2]"]

  - decision_area: "Database"
    selected_option: "[To be determined through /analyze solutions]"
    rationale: "[Why this was chosen]"
    alternatives_considered: ["[Option 1]", "[Option 2]"]

  - decision_area: "Frontend Framework"
    selected_option: "[To be determined through /analyze solutions]"
    rationale: "[Why this was chosen]"
    alternatives_considered: ["[Option 1]", "[Option 2]"]
```

**Integration Patterns:**
```yaml
integration_decisions:
  - integration_point: "[External System Name]"
    selected_pattern: "[REST_API | GRAPHQL | MESSAGE_QUEUE | DATABASE | FILE_SYNC]"
    rationale: "[Why this pattern was chosen]"
    data_flow: "[How data moves between systems]"
    error_handling: "[How failures are managed]"
```

## Architecture Overview

### Core Components
[Component definitions will be populated as architecture emerges]

### System Boundaries
[Scope definitions will be extracted from design documents]

### Integration Points
[Integration requirements will be discovered during development]

## Fundamental Constraints

### Technical Constraints
[Technical limitations will be identified during analysis]

### Business Constraints
[Business rules will be extracted from requirements]

### Compliance Constraints
[Regulatory requirements will be documented as discovered]

## Current Status

**Phase**: Vision Validation
**Key Risks**: [To be identified during risk assessment]
**Next Milestones**: [To be defined during planning]

---

*This file is maintained by the `/sync-context` command. For detailed decision rationale, see [decisions-made.md](./project/decisions-made.md). For implementation insights, see [lessons-learned.md](./project/lessons-learned.md). For unresolved questions, see [open-questions.md](./project/open-questions.md).*