# AI-Human Collaboration Template

A meta-template for establishing effective AI-human collaboration patterns in software development, featuring pressure-tested methodologies for managing complex projects with Claude Code.

## Core Framework

**AI Spec-Driven Development (ASDD) v1.0.2** - Spiral development approach with progressive detail levels (Vision → Approach → Structure → Specifics → Implementation) that handles changing requirements, timeline pressure, and context preservation.

**Philosophy** - A comprehensive collaboration framework that has been forged through pressure and refined by reality. This philosophy addresses the collaboration paradox where AI can offer answers that look complete but may miss critical domain complexities. It establishes clear ownership boundaries: human judgment handles strategy and architecture, AI handles implementation and pattern recognition, with explicit accountability for every significant choice. The framework includes domain-aware collaboration patterns that scale AI involvement inversely with domain complexity, pressure-adaptive protocols that maintain quality under stress, and bounded replaceability principles that design components with stable interfaces enabling informed replacement decisions.

## Key Components

- **Spiral Navigation** - Flexible progression through development levels with backward navigation when discoveries invalidate assumptions
- **Domain Calibration** - AI involvement scales from full implementation in simple domains to boilerplate-only in extreme domains
- **Context Preservation** - Active management to prevent information degradation across phase transitions
- **Pressure Adaptation** - Protocols for maintaining quality under timeline stress without abandoning process
- **Bounded Replaceability** - Design components with realistic replacement cost assessment and clear behavioral contracts

## Getting Started

**Before starting any project with this template, create these two files:**

- **OVERVIEW.md**: A short description for the project. The elevator pitch.
- **HIGH-LEVEL-DESIGN.md**: A description of all the key core principles and requirements that are necessary to consider the project successful. This is not a detailed design, but should be defined enough for reasonable repeatability.

### First Steps

1. Create a GitHub repo using `rjroy/claude-code-template` as a template
2. Clone the repo
3. Create project directories: `mkdir -p docs/design context docs/reports`
4. Add `OVERVIEW.md` and `HIGH-LEVEL-DESIGN.md` to `docs/design`
5. Move this `README.md` to the `ASDD` directory
6. Move `ASDD` into `docs`
7. Copy `docs/design/OVERVIEW.md` to `README.md`
8. Open `claude`
9. Run `/init`
10. You may need to run the following prompt:
```
This is no longer a template project.
Update CLAUDE.md to reflect the fact that this project is now an instantiation.
```

This will result in a structure close to this:

```
repo-name/
├── docs/                        # Documentation
│   ├── design/                  # Core design documents
│   |   ├── OVERVIEW.md          # Project specific overview
│   |   └── HIGH-LEVEL-DESIGN.md # Project specific design
│   ├── reports/                 # Phase reports and analysis
│   └── ASDD/                    # ASDD philosophy documentation
│       ├── README.md            # This document
│       └── ...                  # Remaining ASDD documentation
├── context/                     # Context preservation
│   ├── project-context.yml      # Main context manifest
│   └── archive/                 # Historical context versions
├── .claude/                     # Claude Code integration
|   └── commands/                # ASDD Development commands
├── CLAUDE.md                    # Claude base instructions
└── README.md                    # Project specific overview
```

## Available Commands

### Core Phase Commands
Complete ASDD v1.0.2 command set:
- `/phase-0-prototype` - Risk validation through proof-of-concept
- `/level-0-vision` - Problem clarity and core purpose
- `/level-1-approach` - Technical approach validation
- `/level-2-structure` - System boundaries and components
- `/level-3-specifics` - Detailed implementation specifications
- `/level-4-implementation` - Production-ready code delivery

### Utility Commands
Context management and workflow support:
- `/asdd-context-sync` - Maintain context across phases and prevent information loss
- `/generate-next-steps` - Create detailed transition plans with resource estimates
- `/generate-phase-report` - Generate comprehensive reports from phase artifacts

### Common Workflow Patterns

**Phase Completion Workflow**:
```bash
/asdd-context-sync level-0-vision
/generate-next-steps level-0-vision
/generate-phase-report level-0-vision
```

**Phase Transition Workflow**:
```bash
/generate-phase-report phase-0-prototype
/generate-next-steps phase-0-prototype
/asdd-context-sync level-1-approach
```

**Context Recovery** (when context is lost):
```bash
/asdd-context-sync current-phase context/project-context.yml
/generate-next-steps current-phase context/project-context.yml
```

## What You Get

### **Structured Collaboration Framework**
- **Domain-Aware Boundaries**: AI involvement scales from full implementation (simple domains) to boilerplate-only (extreme domains)
- **Pressure-Adaptive Protocols**: Methodology bends under timeline pressure without breaking
- **Context Preservation**: Prevent information loss across phase transitions with structured context management
- **Spiral Navigation**: Move backward when discoveries invalidate assumptions, forward when ready to proceed

### **Practical Tools**
- **9 Ready-to-Use Commands**: Complete workflow from prototype validation to production implementation
- **Context Management**: Automated context sync with conflict resolution and versioning
- **Transition Planning**: Resource estimation, risk assessment, and clear next steps
- **Comprehensive Reporting**: Executive and technical reports with artifact discovery

### **Quality Assurance Built-In**
- **Validation Criteria**: Critical decisions remain traceable with clear rationale, action items have clear ownership and realistic timelines
- **Conflict Resolution**: Systematic approaches for handling conflicting requirements or constraints
- **Success Indicators**: Clear qualitative measures for each phase and utility command
- **Troubleshooting Guide**: Common issues and resolution strategies

## What Makes This Different

This template has been pressure-tested against systematic failure analysis and incorporates real-world learnings from project breakdowns. Version 1.0.2 addresses timeline pressure, context degradation, domain complexity mismatches, and collaboration boundary drift - the common failure modes that break clean development processes.

**Philosophy**: Trust through verification, not verification through trust. This template provides the structure for AI-human collaboration that bends under pressure rather than breaking.

## Next Steps After Setup

1. **Start with Vision**: Run `/level-0-vision` to establish clear project purpose
2. **Validate Early**: Use `/phase-0-prototype` for risk validation before deep implementation
3. **Maintain Context**: Run `/asdd-context-sync` after each significant phase
4. **Plan Transitions**: Use `/generate-next-steps` before moving to next phase
5. **Document Progress**: Generate reports with `/generate-phase-report` for stakeholders

**Pro Tip**: When under pressure, the framework provides fast-track protocols - combine levels, use proven patterns, but never abandon the context preservation that makes recovery possible.
