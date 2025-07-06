# SAID Core Concepts

_The foundational thinking behind Spiral AI Development_

---

## The Collaboration Paradox

AI excels at generating quick small solutions for well understood domains. The current AI collaboration loop therefore relies on the user breaking the problem down and clearly defining it before starting. If you don't then you get a quick small solution for a complex problem, which doesn't work as you expect.

**The structural trap**: AI can offer answers that look complete. When working on complex problems, this creates a false confidence—you get something that sounds right but hasn't been tested against the real constraints and complexities of your domain.

**Why this matters**: The more complex your problem, the more likely AI is to miss critical details, make wrong assumptions, or optimize for the wrong constraints. But the output will still sound confident and complete.

---

## Ownership Architecture

Clear boundaries prevent collaboration breakdown when problems get complex.

### Human Judgment
- Strategy and architectural decisions
- Trade-offs and failure mode assessment
- Domain-specific knowledge and constraints
- When to trust AI suggestions vs. when to override

### AI Execution
- Implementation and pattern recognition
- Systematic application of established approaches
- Option generation and code synthesis
- Following clear specifications

### Shared Territory
- Code review and testing strategy
- Documentation structure
- Assumption validation and clarification

### Failure Mode
When AI starts making architectural decisions or humans start micromanaging syntax. Both indicate boundary drift that needs correction.

**Principle**: Decision ownership must be explicit and documented for every significant choice.

---

## Domain Calibration

AI involvement should scale inversely with domain complexity. The more complex and specialized your domain, the less architectural responsibility AI should take.

### Simple Domains (CRUD, Basic Workflows)
- **AI Role**: Full implementation, architecture suggestions
- **Human Role**: Validation, requirement clarification
- **Trust Level**: High (verify output)

### Complex Domains (Distributed Systems, ML Pipelines)
- **AI Role**: Implementation, standard pattern application
- **Human Role**: All architecture, algorithm selection
- **Trust Level**: Low (assume gaps in understanding)

### Extreme Domains (Trading, Medical, Aerospace)
- **AI Role**: Boilerplate only, syntax assistance
- **Human Role**: All design decisions, careful review
- **Trust Level**: Minimal (assume no domain knowledge)

**Why this matters**: AI will confidently suggest solutions regardless of domain complexity. You need to calibrate your trust level based on how much implicit knowledge your domain requires.

---

## Context Building

The greatest power and enemy of AI is its context. Working on a complex problem can be difficult if it loses context. You need to build it up, and preserve it.

### Why Context Is Power
- AI performs much better when it understands the full problem space
- Built-up context prevents starting from scratch every session
- Rich context enables better suggestions and fewer misunderstandings

### Why Context Is Enemy
- Context can degrade or get lost between sessions
- Wrong context can mislead AI down incorrect paths
- Context overload can reduce focus on current priorities

### Building Context Effectively
- Document key decisions and their rationale
- Preserve constraint discoveries and requirement changes
- Maintain traceability from high-level goals to implementation details
- Create context checkpoints that can restore understanding

**The key insight**: Context isn't just conversation history. It's the accumulated understanding of your problem, decisions, and constraints that makes each AI interaction more effective.

---

## Bounded Replaceability Principle

Design components and processes so that any piece can be understood and replaced without archaeological investigation.

### What This Means
- Clear, minimal interfaces that hide implementation complexity
- Explicit documentation of implicit knowledge and hidden behaviors
- Realistic assessment of replacement cost and required expertise
- Tests that serve as behavioral specification

### Why This Matters for AI Collaboration
- AI excels at implementing well-bounded components with clear specs
- AI struggles with archaeological investigation of tightly coupled legacy code
- **Clear boundaries let you regenerate components when AI gets them wrong**
- Clear interfaces make AI-human handoffs much cleaner
- Realistically bounded components can be safely delegated based on complexity

**The principle**: Every component should be designed as if it might need to be rebuilt by someone with no institutional knowledge.

---

## How These Concepts Work Together

1. **The Collaboration Paradox** explains why you need systematic approaches to AI collaboration
2. **Ownership Architecture** defines who makes what decisions
3. **Domain Calibration** determines how much to trust AI in your specific context
4. **Context Building** ensures AI has the information it needs to be useful
5. **Bounded Replaceability** creates clean handoff points for AI implementation

These aren't independent techniques—they're interconnected principles that reinforce each other. When one breaks down, the others provide backup structure to prevent total collaboration failure.

The SAID methodology and commands [implement](/docs/SAID/philosophy/implementation-guide.md) these concepts in a practical workflow, but the concepts themselves are the foundation that makes the methodology work.