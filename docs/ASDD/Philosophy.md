# Project Philosophy

_A foundation forged through pressure, refined by reality._

> **Core Thesis**: Philosophy emerges when process breaks down. These principles exist to guide judgment when clean guidelines hit messy reality. They have been pressure-tested against systematic failure analysis.

---

## 🎯 Philosophical Foundation

### The Collaboration Paradox

AI can offer answers that look complete. **That's the structural trap.** This philosophy applies pressure to both human and AI judgment—not to break collaboration, but to see how it bends under real project stress.

**Principle**: _Trust through verification, not verification through trust._

- When Claude Code suggests a solution, the first question isn't "Is this right?" but "What assumptions is this making?"
- When guidelines conflict with reality, the reality wins—but gets documented as a philosophical update
- When AI confidence is high but domain complexity is extreme, human expertise takes precedence

### Ownership Architecture

**Human Judgment**: Strategy, trade-offs, architectural decisions, failure mode assessment, domain-specific knowledge

**AI Execution**: Implementation, pattern recognition, systematic application, option generation, code synthesis

**Shared Territory**: Code review, testing strategy, documentation structure, assumption validation

**Failure Mode**: When AI starts making architectural decisions or humans start micromanaging syntax. Both indicate boundary drift.

**Clarity**: Decision ownership is explicit and documented for every significant choice.

### 🏗️ Bounded Replaceability Principle

**Core Thesis**: Design components with stable interfaces and documented behavioral contracts that enable informed replacement decisions.

**What "Bounded Replaceability" Means:**

- Clear, minimal interfaces that hide implementation complexity
- Explicit documentation of implicit knowledge and hidden behaviors
- Realistic assessment of replacement cost and required expertise
- Acceptable behavioral variance ranges clearly defined
- Tests that serve as behavioral specification

**The Honest Test**: If this component disappeared tomorrow, what would someone need to rebuild it compatibly without archaeological investigation? Document that need realistically.

**Why This Matters for AI Collaboration:**

- AI excels at implementing well-bounded components with clear specs
- AI struggles with archaeological investigation of tightly coupled legacy code
- Clear interfaces make AI-human handoffs much cleaner
- Realistically bounded components can be safely delegated based on complexity

---

## 🤝 AI Collaboration Framework

### Core Collaboration Principles

1. **Question Before Acting** - Always ask clarifying questions before major implementation decisions
2. **Present Options** - Provide pros/cons rather than choosing for the user
3. **Explain Reasoning** - Share the "why" behind technical recommendations
4. **Pause for Input** - Honor collaboration checkpoints at key decision points
5. **Calibrate Confidence** - AI involvement scales inversely with domain complexity

### Domain-Aware Collaboration Patterns

**Simple Domains** (CRUD, Basic Workflows):
- AI Role: Full implementation, architecture suggestions
- Human Role: Validation, requirement clarification
- Trust Level: High (verify output)

**Complex Domains** (Distributed Systems, ML Pipelines):
- AI Role: Implementation, standard pattern application
- Human Role: All architecture, algorithm selection
- Trust Level: Low (assume gaps in understanding)

**Extreme Domains** (Trading, Medical, Aerospace):
- AI Role: Boilerplate only, syntax assistance
- Human Role: All design decisions, careful review
- Trust Level: Minimal (assume no domain knowledge)

### Collaboration Failure Modes & Responses

**When AI Assumes Instead of Asks:**

- **Trigger**: Solution appears without options or explanation
- **Response**: "What other approaches did you consider? What would break if we chose differently?"
- **Prevention**: Explicitly request multiple approaches for any non-trivial decision

**When Questions Become Procrastination:**

- **Trigger**: 3+ rounds of questions without progress toward implementation
- **Response**: "Choose the simplest viable approach and we'll iterate."
- **Prevention**: Set decision deadlines: "We need to move on this by end of discussion."

**When High Confidence Meets High Complexity:**

- **Trigger**: AI suggests complex domain solution with high confidence
- **Response**: "This domain requires deep expertise. Let's validate core assumptions first."
- **Prevention**: Domain complexity assessment before AI architectural involvement

---

## 🔄 Version Control Collaboration

### Git Workflow Integration with ASDD

**Core Principle**: Version control workflows can support collaboration and quality through thoughtful design.

**Consider Using Branch Protection**:
- Protected main branch encourages review before integration
- Pull requests create natural collaboration checkpoints
- Code review allows sharing of domain expertise
- Automated checks can catch objective issues early

### Suggested Branching Patterns

**Consider Descriptive Branch Names**:
- Feature branches with clear intent: `feature/user-authentication`
- Prototype branches for experiments: `prototype/test-new-api`
- Include ASDD phase if helpful: `feature/level-1-technical-approach`
- Keep names meaningful to your team

**Simple GitHub Flow**:
```
main
├── feature/descriptive-name
├── fix/bug-description
├── docs/what-youre-documenting
└── prototype/experiment-name
```

**Context Preservation Through Git**:
- Use meaningful commit messages that explain decisions
- Document major choices in context files
- PR descriptions can capture important discussions
- Git history naturally preserves your journey

### Thoughtful Code Review Practices

**For Simple Domains**:
- Consider lighter review for straightforward changes
- Focus on integration and consistency
- Trust automated tests for basic validation

**For Complex Domains**:
- Involve team members with relevant expertise
- Take time to review architectural implications
- Discuss design decisions as a team

**For Extreme Domains**:
- Multiple reviewers may be valuable
- Consider compliance and safety requirements
- Document review decisions and rationale

### Supporting Component Replaceability

**Consider These Practices**:
- Keep changes focused and cohesive
- Document interfaces clearly in PRs
- Note dependencies that might affect others
- Think about future maintainability

**Merge Strategy Options**:
- Squash merge: Clean history for feature branches
- Merge commit: Preserve development context
- Rebase: Linear history (if team prefers)
- Choose what works for your team

### Encouraging Good Collaboration

**Pull Request Templates Can Include**:
- Helpful checklists (not rigid requirements)
- Prompts for important context
- Reminders about documentation
- Space for explaining decisions

**Review Assignment Suggestions**:
- Consider who has relevant expertise
- Rotate reviews to share knowledge
- Use CODEOWNERS as suggestions, not rules
- Trust teams to find the right reviewers

**Quality Checkpoints to Consider**:
- Are tests passing?
- Is the change well-explained?
- Have the right people reviewed?
- Is documentation current?

### Handling Timeline Pressure

**When Deadlines Are Tight**:
- Focus on essential quality checks
- Document what's being deferred
- Create follow-up issues for cleanup
- Communicate with the team

**Suggested Priorities Under Pressure**:
- Keep: Security review, critical tests
- Consider deferring: Perfect documentation, nice-to-have features
- Always: Communicate trade-offs clearly
- Plan: Schedule time for technical debt

---

## 💻 Code Philosophy

### Technical Principles

- **Bounded replaceability first** - Design components with realistic replacement assessments
- **Clarity over cleverness** - Write code that future you will understand
- **Consistency over personal preference** - Follow established patterns
- **Type safety first** - Leverage TypeScript's type system fully
- **Performance awareness** - Consider performance implications, especially for large collections
- **Accessibility by default** - Every UI component should be accessible

### Bounded Design Application

**Interface Design:**

- Minimize surface area—expose only what consumers actually need
- Make dependencies explicit—no hidden global state or implicit contracts
- Design for testability—complex logic should be easily isolatable
- Document implicit behaviors and hidden business rules

**Component Boundaries:**

- Each component should solve exactly one problem well
- Avoid components that know too much about their context
- Prefer composition over inheritance for flexibility
- Assess and document actual replaceability cost

**Documentation Requirements:**

- Decision logs for non-obvious choices
- Behavioral specifications through tests
- Clear examples of intended usage patterns
- Capture implicit knowledge and domain-specific constraints

---

## 🔄 AI Spec-Driven Development (ASDD) - Reality-Tested

### The Theory

Spiral collaboration with AI using progressive elaboration to break large specs into implementable tasks through flexible detail levels with built-in feedback loops.

### The Reality Integration

**This workflow has been updated to handle:**

- Domain complexity that exceeds AI's pattern matching
- Requirements that change faster than decomposition
- Implementation discoveries that invalidate earlier phases
- Timeline pressure that threatens process abandonment
- Context degradation across phase transitions

### Enhanced Workflow with Integrated Patches

#### Phase 0: Prototype Validation

**Input**: High Level Design
**Output**: Risk validation + Go/No-Go decision

**Purpose**: Build minimal proof-of-concept to validate highest-risk technical assumptions before full decomposition.

**Activities**:
- Identify 3 highest technical risks
- Build throwaway prototypes to test feasibility
- Validate integration points with real systems
- Document discovered complexities

**Success Gate**: Core technical approach proven viable
**Failure Response**: Pivot approach or abort before sunk cost

#### Spiral Navigation with Context Preservation

**Progressive Detail Levels** (replaces rigid phases):

1. **Level 0**: Vision clarity (Core purpose understood)
2. **Level 1**: Approach viability (Solution approach validated)
3. **Level 2**: Structure definition (System boundaries defined)
4. **Level 3**: Implementation specifics (Buildable specifications)
5. **Level 4**: Working implementation (Production-ready code)

**Advancement Rules**:
- Can proceed when critical unknowns resolved
- Can defer decisions with explicit documentation
- Can navigate backward when discoveries invalidate assumptions
- Must maintain context integrity across transitions

**Context Preservation Requirements**:
```yaml
context_manifest:
  critical_requirements: [documented and traced]
  key_decisions: [with rationale and alternatives]
  discovered_constraints: [impact assessment included]
  semantic_checksum: [core purpose + users + metrics + constraints]
```

#### Domain-Calibrated AI Involvement

**Before Each Level**:
1. Assess domain complexity
2. Set appropriate AI boundaries
3. Ensure required human expertise available
4. Calibrate confidence expectations

**Accountability Matrix**:
- Explicit decision ownership per complexity level
- Audit trail for all significant choices
- Escalation paths for conflicts
- Blameless learning from failures

#### Pressure-Adaptive Protocols

**Timeline Pressure Response**:
- Moderate Pressure: Combine levels, use proven patterns
- High Pressure: Skip to Level 3 with templates, plan cleanup
- Extreme Pressure: Emergency mode with damage control

**Quality Gates Under Pressure**:
- Never Compromise: Security, data integrity, basic functionality
- Defer If Needed: Performance optimization, UI polish, comprehensive docs

### Success Metrics

1. **Spiral Effectiveness**: <20% of level outputs require complete revision
2. **Context Retention**: >80% of Level 0 requirements traceable in Level 4
3. **Domain Calibration**: 90% of AI suggestions match confidence scores
4. **Pressure Adaptation**: 80% of high-pressure projects deliver working software
5. **Accountability Clarity**: 100% of decisions have identified owners

### Failure Indicators

- Multiple backward navigations without learning
- Context checksums diverge >40% between levels
- AI making architectural decisions in extreme domains
- Teams abandon process under moderate pressure
- Decision ownership ambiguity causing delays

---

## 🛡️ Structural Reflexes

### Enhanced Drift Detection

**Code Quality Drift**:
- Trigger: Test coverage drops, context integrity fails, documentation gaps
- Response: Immediate level review, technical debt assessment

**Collaboration Drift**:
- Trigger: AI exceeds domain-calibrated boundaries, ownership confusion
- Response: Reset boundaries, clarify decision authority, reassess domain complexity

**Process Drift**:
- Trigger: Pressure protocols unused, context preservation skipped
- Response: Update protocols or strengthen training

### Philosophy Evolution

This document must change when reality proves it wrong.

Changes require:
1. Documentation of what broke and why
2. Assessment of whether breakage was environmental or structural
3. Updated principles that would have prevented the failure
4. Testing of new principles against historical project pressure
5. Integration testing with other patches

**Anti-Pattern**: Treating this philosophy as immutable doctrine rather than living guidance that adapts to project realities.

---

## 🧭 Dual Audience Integration

### For Future Developers

This philosophy provides:

- Spiral development patterns that handle changing requirements
- Context preservation techniques that maintain project coherence
- Domain complexity assessment frameworks
- Pressure adaptation protocols that maintain quality under stress
- Realistic component boundary assessment

### For Claude Code

This philosophy provides:

- Domain-calibrated collaboration boundaries with confidence scoring
- Context validation checkpoints for drift detection
- Progressive elaboration guidance for flexible detail levels
- Pressure-responsive adaptation protocols
- Explicit accountability frameworks for decision support

**Integration Test**: Can both audiences use this philosophy to make better decisions under pressure while maintaining quality and learning from failures?

---

## 🔥 Philosophy Under Fire

- **When everything breaks:** Revert to core principles—safety, clarity, ownership boundaries, context preservation
- **When timelines collapse:** Activate pressure protocols—maintain non-negotiable gates, plan recovery
- **When AI fails:** Domain calibration provides fallback boundaries and human expertise requirements
- **When context degrades:** Preservation checkpoints enable rapid restoration
- **When decisions fail:** Accountability matrix ensures learning without blame

This philosophy exists for the moments when clean process hits messy reality.
Version 1.0 has been designed to bend without breaking, adapting to pressure while preserving essential benefits.

---

_Philosophy version: 1.0.4_
_Last pressure-tested: 2025-07-03_
_Failure analysis integrated: docs/ASDD/revision-rationale/v0.1-analysis.md_
_Improved collaboration hooks: docs/ASDD/revision-rationale/v1.0-analysis.md_
_Git workflow integration: v1.0.3 (flexible guidance for thoughtful collaboration)_
_Report templates: v1.0.4_
_Next philosophical review: After 10 projects using v1.0.4 methodology_