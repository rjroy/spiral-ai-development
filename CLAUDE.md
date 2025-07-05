# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **meta-template repository** for establishing AI-human collaboration patterns in software development. It contains no implementation code but provides philosophical and procedural frameworks for future projects that have been pressure-tested against systematic failure analysis.

## Core Philosophy

The development philosophy is documented in [docs/SAID/Philosophy.md](docs/SAID/Philosophy.md). Key principles include:

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

## Spiral AI Development (SAID) - Spiral Model

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

3. **Customize SAID Commands**:
   - Use existing level commands (`/level-0-vision`, `/level-1-approach`, etc.)
   - Create domain-specific commands using `docs/SAID/claude-command-template/phase-template.md`
   - Adapt validation requirements to project needs

4. **Establish Project-Specific Standards**:
   - Define technology stack and tooling
   - Set up testing and build infrastructure
   - Create project-specific coding standards
   - Implement context preservation system

### Available Commands

The template includes complete SAID commands:

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
/said-context-sync   - Maintain context across phases
/generate-next-steps - Create transition plans
/generate-phase-report - Generate comprehensive reports
```

See [Git Workflow Integration](docs/SAID/git-workflow-integration.md) for flexible guidance on git workflows that support SAID methodology without being prescriptive.

Each command includes domain calibration, context preservation, and pressure adaptation.

## Context Management and Utility Workflows

**Context File**: A structured document that preserves critical project information across development phases in the SAID methodology. Context files maintain project coherence by documenting key decisions with rationale, discovered constraints, requirements evolution, and semantic checksums.  They serve as living artifacts that prevent information degradation during phase transitions and enable rapid context restoration when project assumptions change or team members rotate. Context files follow a YAML manifest structure and include project identity, phase progression, key decisions, technical constraints, validation results, and risk assessments.

### Context File Management

**Context Manifest Storage**:
- Primary: `context/project-context.yml` - Main context manifest
- Phase/Level-specific: `context/[phase|level]-{id}-{phase/level-name}.yml` - Phase/Level artifacts
- Decomposition-specific: `context/[phase|level]-{id}-{phase/level-name}-{decomposition}.yml` - Decomposition artifacts

### Git Workflow Recommended Integration

**Suggested Approaches**:
- Consider descriptive branch naming that reflects your work
- Use git commits to preserve your decision-making process
- Collaborate through whatever review process works for your team
- Adapt any suggestions to fit your project's constraints

**Team Choice**:
- Some teams find branch naming conventions helpful
- Others prefer simple GitHub Flow with good commit messages
- Context preservation is more important than any specific git workflow
- Choose tools that support your thinking, not the other way around

For more detail see [git-workflow-integration.md](docs/SAID/git-workflow-integration.md)

**Context File Naming Convention**:
```
context/
├── project-context.yml           # Main context manifest
├── phase-0-prototype-context.yml # Phase-specific context
└── level-{n}-{name}-context.yml  # Level-specific context
```

### Utility Command Workflows

**Recommended Workflow Sequences**:

1. **Phase Completion Workflow**:
   ```
   /said-context-sync {current-phase}
   /generate-next-steps {current-phase}
   /generate-phase-report {current-phase}
   ```

2. **Phase Transition Workflow**:
   ```
   /generate-phase-report {completed-phase}
   /generate-next-steps {completed-phase}
   /said-context-sync {next-phase}
   ```

3. **Context Recovery Workflow**:
   ```
   /said-context-sync {current-phase} context/project-context.yml
   /generate-next-steps {current-phase} context/project-context.yml
   ```

### Context Manifest Structure

```yaml
# Project Context Manifest Template
context_manifest:
  version: "1.0.6
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

## Collaboration Patterns

### Context Preservation Requirements

For each level, maintain context manifest with:
- Critical requirements and their evolution
- Key decisions with rationale and alternatives
- Discovered constraints and their impact
- Semantic checksum (purpose + users + metrics + constraints)

### Git Workflow Integration

**Branch-per-Phase Collaboration**:
- Each SAID level uses dedicated feature branch
- Context preservation through structured commit messages
- Pull requests enforce domain-calibrated review requirements
- Git history serves as decision audit trail

**Validation Gates**:
- Branch protection prevents unvalidated code integration
- PR templates ensure SAID validation checklists completion
- Automated workflows verify context integrity
- Domain experts assigned based on complexity assessment

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

## Key Files

### Core Framework Files
- `docs/SAID/Philosophy.md` - Complete development philosophy with integrated patches
- `docs/SAID/git-workflow-integration.md` - Git workflow integration with SAID phases
- `docs/SAID/claude-command-template/phase-template.md` - Comprehensive template for creating SAID commands
- `docs/SAID/claude-command-template/utility-template.md` - Template for creating utility commands
- `docs/SAID/revision-rationale/` - Systematic failure analysis for historic versions. Provides deeper insight into revisions.

### Phase Commands
- `.claude/commands/phase-0-prototype.md` - Prototype validation command
- `.claude/commands/level-0-vision.md` - Vision clarity command
- `.claude/commands/level-1-approach.md` - Approach viability command
- `.claude/commands/level-2-structure.md` - Structure definition command
- `.claude/commands/level-3-specifics.md` - Implementation specifics command
- `.claude/commands/level-4-implementation.md` - Working implementation command

### Utility Commands
- `.claude/commands/said-context-sync.md` - Context preservation across phases
- `.claude/commands/generate-next-steps.md` - Transition planning utility
- `.claude/commands/generate-phase-report.md` - Comprehensive reporting utility

### Configuration
- `.claude/settings.local.json` - Claude Code permissions configuration (not shared)

## Important Notes

- This template contains no implementation code but provides pressure-tested methodology
- Addresses systematic failure modes through integrated patches and adds git workflow integration
- All principles designed to bend under pressure rather than break
- Methodology includes explicit escape valves and recovery mechanisms
- Focus on reality-tested collaboration patterns that work under constraints
   - Real-world constraint handling
   - Graceful degradation under timeline pressure
- Git workflow integration with branch protection and phase-aligned branching

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

---

When using this template for a new project, replace this generic CLAUDE.md with project-specific guidance including actual build commands, testing strategies, and architectural patterns once they're established.