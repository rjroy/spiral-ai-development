# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **meta-template repository** for establishing AI-human collaboration patterns in software development. It contains no implementation code but provides philosophical and procedural frameworks for future projects that have been pressure-tested against systematic failure analysis.

## Core Philosophy v1.0.2

The development philosophy is documented in [ASDD/Philosophy.md](ASDD/Philosophy.md). Key principles include:

### Enhanced Collaboration Framework
1. **Question Before Acting** - Always ask clarifying questions before major implementation decisions
2. **Present Options** - Provide pros/cons rather than choosing for the user
3. **Explain Reasoning** - Share the "why" behind technical recommendations
4. **Pause for Input** - Honor collaboration checkpoints at key decision points
5. **Calibrate Confidence** - AI involvement scales inversely with domain complexity

### Bounded Replaceability Principle
Design components with stable interfaces and documented behavioral contracts that enable informed replacement decisions. This means:
- Clear, minimal interfaces that hide implementation complexity
- Explicit documentation of implicit knowledge and hidden behaviors
- Realistic assessment of replacement cost and required expertise
- Acceptable behavioral variance ranges clearly defined
- Tests that serve as behavioral specification

### Domain-Aware AI Collaboration
- **Simple Domains**: AI can lead implementation with human validation
- **Complex Domains**: AI assists implementation, human leads architecture
- **Extreme Domains**: AI provides boilerplate only, human owns all decisions

## AI Spec-Driven Development (ASDD) v1.0.2 - Spiral Model

This template establishes a spiral development approach with progressive detail levels:

**Phase 0: Prototype Validation** - Risk validation through minimal proof-of-concept
1. **Level 0: Vision Clarity** - Core purpose understood
2. **Level 1: Approach Viability** - Solution approach validated
3. **Level 2: Structure Definition** - System boundaries defined
4. **Level 3: Implementation Specifics** - Buildable specifications
5. **Level 4: Working Implementation** - Production-ready code

### Key Enhancements
- **Spiral Navigation**: Backward navigation when discoveries invalidate assumptions
- **Context Preservation**: Active management to prevent information degradation
- **Progressive Elaboration**: Partial completion with explicit unknowns
- **Pressure Adaptation**: Fast-track protocols for timeline pressure

## Using This Template

### For New Projects

When starting a new project with this template:

1. **Create Required Files**:
   - `OVERVIEW.md` - Elevator pitch for the project
   - `HIGH-LEVEL-DESIGN.md` - Core principles and requirements

2. **Assess Domain Complexity**:
   - Evaluate regulatory/compliance requirements
   - Assess technical constraints and performance needs
   - Determine required human expertise level
   - Set appropriate AI involvement boundaries

3. **Customize ASDD Commands**:
   - Use existing level commands (`/level-0-vision`, `/level-1-approach`, etc.)
   - Create domain-specific commands using `ASDD/claude-command-template/phase-template.md`
   - Adapt validation requirements to project needs

4. **Establish Project-Specific Standards**:
   - Define technology stack and tooling
   - Set up testing and build infrastructure
   - Create project-specific coding standards
   - Implement context preservation system

### Available Commands

The template includes complete ASDD v1.0.2 commands:

#### Core Phase Commands
```
/phase-0-prototype   - Risk validation through proof-of-concept
/level-0-vision      - Problem clarity and core purpose
/level-1-approach    - Technical approach validation
/level-2-structure   - System boundaries and components
/level-3-specifics   - Detailed implementation specifications
/level-4-implementation - Production-ready code delivery
```

#### Utility Commands
```
/asdd-context-sync   - Maintain context across phases
/generate-next-steps - Create transition plans
/generate-phase-report - Generate comprehensive reports
```

Each command includes domain calibration, context preservation, and pressure adaptation.

## Context Management and Utility Workflows v1.0.2

### Context File Management

**Context Manifest Storage**:
- Primary: `context/project-context.yml` - Main context manifest
- Phase-specific: `context/phase-{phase-name}-context.yml` - Phase artifacts
- Archive: `context/archive/` - Historical context versions

**Context File Naming Convention**:
```
context/
├── project-context.yml           # Main context manifest
├── phase-0-prototype-context.yml # Phase-specific context
├── level-{n}-{name}-context.yml  # Level-specific context
└── archive/                      # Historical versions
    ├── project-context-v1.yml
    └── phase-0-prototype-v1.yml
```

### Utility Command Workflows

**Recommended Workflow Sequences**:

1. **Phase Completion Workflow**:
   ```
   /asdd-context-sync {current-phase}
   /generate-next-steps {current-phase}
   /generate-phase-report {current-phase}
   ```

2. **Phase Transition Workflow**:
   ```
   /generate-phase-report {completed-phase}
   /generate-next-steps {completed-phase}
   /asdd-context-sync {next-phase}
   ```

3. **Context Recovery Workflow**:
   ```
   /asdd-context-sync {current-phase} context/project-context.yml
   /generate-next-steps {current-phase} context/project-context.yml
   ```

### Context Manifest Structure

```yaml
# Project Context Manifest Template
context_manifest:
  version: "1.0.2"
  project_identity:
    name: "Project Name"
    purpose: "Core project purpose"
    primary_users: "Primary user groups"
    success_metrics: "How success is measured"
    fundamental_constraints: "Non-negotiable limitations"
    
  phase_progression:
    current_phase: "phase-0-prototype"
    completed_phases: ["level-0-vision"]
    next_phase: "level-1-approach"
    
  key_decisions:
    - decision_id: "D001"
      decision: "What was decided"
      rationale: "Why this was chosen"
      alternatives_considered: "What else was evaluated"
      phase_decided: "level-0-vision"
      impact_scope: "What this affects"
      confidence_level: 0.8
      
  technical_constraints:
    - constraint_id: "C001"
      constraint: "Technical limitation"
      source: "Where this originated"
      impact: "How this affects design"
      mitigation_strategy: "How to handle this"
      
  validation_results:
    - validation_id: "V001"
      validation_target: "What was tested"
      validation_method: "How it was validated"
      result: "VALIDATED | INVALIDATED | PARTIAL"
      evidence: "Supporting data/artifacts"
      confidence: 0.9
      
  risk_assessments:
    - risk_id: "R001"
      risk_description: "What could go wrong"
      probability: "HIGH | MEDIUM | LOW"
      impact: "HIGH | MEDIUM | LOW"
      mitigation: "Prevention/response strategy"
      status: "ACTIVE | MITIGATED | ACCEPTED"
```

## Collaboration Patterns v1.0.2

### Context Preservation Requirements

For each level, maintain context manifest with:
- Critical requirements and their evolution
- Key decisions with rationale and alternatives
- Discovered constraints and their impact
- Semantic checksum (purpose + users + metrics + constraints)

### Domain-Calibrated Workflow

**Before Each Level**:
1. Assess domain complexity (Simple/Complex/Extreme)
2. Set appropriate AI boundaries
3. Ensure required human expertise available
4. Calibrate confidence expectations

### Pressure-Testing Protocol

For each level, apply enhanced validation:

1. **Context-Specific Reality Check** - Domain-appropriate validation questions
2. **Integration/Boundary Assessment** - Interface and dependency complexity
3. **Implementation Feasibility** - Team capability and resource reality
4. **Scope and Constraint Testing** - Boundary definition and scope creep prevention
5. **Risk and Failure Mode Analysis** - Breakdown points and recovery options

### Spiral Navigation

**Advancement Rules**:
- Proceed when critical unknowns resolved and validation passed
- Defer when information genuinely unavailable with explicit timeline
- Navigate backward when discoveries invalidate previous levels

**Pressure Adaptation**:
- Moderate Pressure: Combine levels, use proven patterns
- High Pressure: Skip to Level 3 with templates, plan cleanup
- Extreme Pressure: Emergency mode with damage control

## Key Files v1.0.2

### Core Framework Files
- `ASDD/Philosophy.md` - Complete v1.0.2 development philosophy with integrated patches
- `ASDD/claude-command-template/phase-template.md` - Comprehensive template for creating ASDD commands
- `ASDD/claude-command-template/utility-template.md` - Template for creating utility commands
- `ASDD/revision-rationale/v0-failure.md` - Systematic failure analysis that drove v0.1 improvements

### Phase Commands
- `.claude/commands/phase-0-prototype.md` - Prototype validation command
- `.claude/commands/level-0-vision.md` - Vision clarity command
- `.claude/commands/level-1-approach.md` - Approach viability command
- `.claude/commands/level-2-structure.md` - Structure definition command
- `.claude/commands/level-3-specifics.md` - Implementation specifics command
- `.claude/commands/level-4-implementation.md` - Working implementation command

### Utility Commands
- `.claude/commands/asdd-context-sync.md` - Context preservation across phases
- `.claude/commands/generate-next-steps.md` - Transition planning utility
- `.claude/commands/generate-phase-report.md` - Comprehensive reporting utility

### Configuration
- `.claude/settings.local.json` - Claude Code permissions configuration (not shared)

## Important Notes v1.0.2

- This template contains no implementation code but provides pressure-tested methodology
- **Version 1.0.2** addresses systematic failure modes through integrated patches
- All principles designed to bend under pressure rather than break
- Methodology includes explicit escape valves and recovery mechanisms
- Focus on reality-tested collaboration patterns that work under constraints

### Philosophy Evolution

This methodology evolves when reality proves it wrong. Version 1.0.2 incorporates:
- Systematic failure analysis and pressure-testing results
- Integration testing across all patches
- Real-world constraint handling
- Graceful degradation under timeline pressure

### Utility Command Quality Assurance

**Validation Criteria for Context Sync**:
- All critical decisions include ID, rationale, and alternatives
- Conflicts resolved with documented resolution strategy
- Context versioning maintains traceability
- Semantic checksums verify context integrity

**Validation Criteria for Next Steps**:
- All action items have clear owners and deadlines
- Resource estimates include effort and skill requirements
- Prerequisites are actionable and measurable
- Risk mitigation addresses top failure modes

**Validation Criteria for Phase Reports**:
- Executive summary accessible to non-technical stakeholders
- Technical findings include supporting evidence
- Recommendations are specific and actionable
- Report versioning enables historical tracking

**Success Indicators**:
- Context preservation: Critical decisions remain traceable with clear rationale
- Transition planning: Action items have clear ownership and realistic timelines
- Report quality: Recommendations are specific, actionable, and have clear success criteria

### Troubleshooting Common Issues

**Context Sync Issues**:
- **Merge Conflicts**: Use conflict resolution guidelines in command
- **Missing Context**: Reference previous phase reports for recovery
- **Inconsistent Format**: Validate against context manifest structure

**Next Steps Issues**:
- **Unrealistic Estimates**: Review resource estimation templates
- **Blocked Prerequisites**: Escalate to stakeholder decision
- **Resource Constraints**: Apply mitigation strategies from planning templates

**Report Generation Issues**:
- **Missing Artifacts**: Use artifact discovery methodology
- **Inconsistent Quality**: Apply quality assurance checklist
- **Version Control**: Follow report versioning strategy

When using this template for a new project, replace this generic CLAUDE.md with project-specific guidance including actual build commands, testing strategies, and architectural patterns once they're established.