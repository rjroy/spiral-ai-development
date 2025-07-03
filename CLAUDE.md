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

```
/phase-0-prototype   - Risk validation through proof-of-concept
/level-0-vision      - Problem clarity and core purpose
/level-1-approach    - Technical approach validation
/level-2-structure   - System boundaries and components
/level-3-specifics   - Detailed implementation specifications
/level-4-implementation - Production-ready code delivery
```

Each command includes domain calibration, context preservation, and pressure adaptation.

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

- `ASDD/Philosophy.md` - Complete v1.0.2 development philosophy with integrated patches
- `ASDD/claude-command-template/phase-template.md` - Comprehensive template for creating ASDD commands
- `ASDD/revision-rationale/v0-failure.md` - Systematic failure analysis that drove v0.1 improvements
- `.claude/commands/phase-0-prototype.md` - Prototype validation command
- `.claude/commands/level-0-vision.md` - Vision clarity command
- `.claude/commands/level-1-approach.md` - Approach viability command
- `.claude/commands/level-2-structure.md` - Structure definition command
- `.claude/commands/level-3-specifics.md` - Implementation specifics command
- `.claude/commands/level-4-implementation.md` - Working implementation command
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

When using this template for a new project, replace this generic CLAUDE.md with project-specific guidance including actual build commands, testing strategies, and architectural patterns once they're established.