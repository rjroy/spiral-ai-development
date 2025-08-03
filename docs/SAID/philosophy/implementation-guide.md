# SAID Implementation Guide

_Understanding the philosophy and practice of Spiral AI Development_

---

## The Spiral Method Philosophy

SAID is fundamentally about **progressive certainty through iterative deepening**. It does this by providing AI commands that ask for research, decomposition, and context integration. The user calls these commands to gather information, break the problem into smaller problems, and record decisions.

### Core Principles

1. **Defer Commitment Until Necessary**: Make decisions only when you have enough information to make them well
2. **Preserve Optionality**: Keep multiple paths open until constraints force choices
3. **Context Over Process**: Maintain rich context that survives between sessions and even team changes
4. **Collaborative Intelligence**: Structure human-AI interaction for complementary strengths

### Progressive Detail Levels

Each level represents a **threshold of understanding**, not a phase to complete:

#### Level 0: Problem + Risk Clarity
**Focus**: Validate that you're solving a real problem worth solving

**Key Questions**:
- What evidence supports this problem's existence?
- Who experiences this problem and how severely?
- What are the consequences of not solving it?
- What could go catastrophically wrong?

**You're Ready for Level 1 When**:
- The problem is validated with evidence
- Key risks are identified with mitigation strategies
- Stakeholder needs are documented and understood
- You can explain why this problem matters in one sentence

#### Level 1: Approach Viability
**Focus**: Choose a technical direction that balances constraints

**Key Questions**:
- What are the fundamental ways to solve this problem?
- What constraints (technical, resource, timeline) shape our options?
- Which approach best fits our specific context?
- What are we explicitly choosing NOT to do?

**You're Ready for Level 2 When**:
- Multiple viable approaches have been evaluated
- A direction is chosen with documented rationale
- Trade-offs are explicit and accepted
- Technical feasibility is validated

#### Level 2: Structure Definition
**Focus**: Define system boundaries and component relationships

**Key Questions**:
- What are the natural boundaries in this system?
- How do components communicate and depend on each other?
- What interfaces enable future flexibility?
- Where are the integration points with existing systems?

**You're Ready for Level 3 When**:
- System boundaries are clearly defined
- Component interfaces are specified
- Dependencies are mapped and manageable
- Integration strategy is validated

#### Level 3: Implementation Specifics
**Focus**: Create buildable specifications with enough detail for execution

**Key Questions**:
- What are the implementation patterns for each component?
- How do we handle edge cases and error conditions?
- What testing strategy validates our assumptions?
- Where might hidden complexity emerge?

**You're Ready for Level 4 When**:
- Specifications are detailed enough to build from
- Testing approach is defined
- Implementation risks are identified
- Team has clarity on technical approach

#### Level 4: Working Implementation
**Focus**: Transform specifications into production-ready code

**Key Activities**:
- Write code that matches specifications
- Implement comprehensive testing
- Handle discovered edge cases
- Maintain context for future developers

### The Spiral Navigation Philosophy

The spiral method isn't linear - it's **adaptive navigation through uncertainty**:

#### Moving Forward
Advance to the next level when you've **resolved the critical unknowns** of your current level. This isn't about completing all possible work, but about having enough clarity to make the next set of decisions well.

#### Strategic Deferral
Some decisions can and should be **explicitly deferred**. Document what you're deferring and why. This isn't procrastination - it's preserving flexibility until you have better information.

#### Navigating Backward
When new discoveries **invalidate earlier assumptions**, loop back. This isn't failure - it's the spiral method working correctly. Each loop adds understanding even when it changes direction.

#### Context as Navigation Aid
Your context files are your **map through the spiral**. They record not just decisions but the reasoning, alternatives considered, and assumptions made. When you get lost, context shows you where you've been and why.

### The Prototype Spike Pattern

Sometimes you discover a risk that **threatens the entire approach**. The prototype spike is an escape valve - a focused effort to validate or invalidate a critical assumption before investing further.

**When to Spike**:
- A technical approach seems theoretically sound but practically uncertain
- Integration with external systems has unknown complexity
- Performance characteristics could invalidate the design
- A core assumption feels shaky but is hard to validate without code

**Spike Principles**:
- Time-boxed exploration (hours to days, not weeks)
- Throwaway code focused on learning
   - This is important
   - The code will rarely be built against all the context
   - AI makes this an easy decision
- Document what you learn, not what you build
- Exit with either confidence or a new direction

**The Spike Decision**:
After a spike, you face three options:
1. **Proceed**: Risk validated as manageable
2. **Pivot**: Change approach based on learning
3. **Abort**: Problem not solvable within constraints

---

## Context Preservation Philosophy

Context is the **persistent memory of your project's journey**. It's not documentation for documentation's sake - it's the difference between repeating mistakes and building on learned wisdom.

### Why Context Matters

**For Humans**: Context provides the "why" behind decisions when you return to code months later. It captures the alternatives you considered and rejected, preventing costly revisiting of dead ends.

**For AI Collaboration**: Rich context enables AI to provide relevant, nuanced assistance instead of generic suggestions. The AI becomes a knowledgeable team member rather than a blank slate.

**For Teams**: Context preservation enables true knowledge transfer. New team members can understand not just what was built, but why it was built that way.

### The Three-File System

SAID uses three primary context files that work together:

1. **project-context.md**: The living manifest of current understanding
   - Current state and phase
   - Active constraints and requirements
   - Integration points for all context

2. **decisions-made.md**: The audit trail of choices
   - What was decided and when
   - Alternatives considered
   - Rationale and trade-offs
   - Links to supporting analysis

3. **open-questions.md**: The uncertainty tracker
   - Questions that need answers
   - Blocked decisions awaiting information
   - Areas requiring deeper investigation

### Context Priming Pattern

When working with AI after any time gap, **prime the context** to restore shared understanding:

```
"I've completed the risk analysis phase. We identified three critical risks and chose a microservices approach. I'm about to start the system decomposition."
```

This pattern:
- Orients the AI to current state
- Highlights recent decisions
- Sets clear intent for next actions
- Takes seconds but saves hours of misdirection

Additionally the `/prime-context` allows for repeating this regularly and consistently.

---

## Working with SAID: Practical Patterns

### The Investigation-Decision-Integration Pattern

SAID workflows follow a natural rhythm:

1. **Investigate** - Gather information and analyze options
2. **Decide** - Make explicit choices with human judgment
3. **Integrate** - Preserve decisions and learning in context

This pattern repeats at every level, creating a **ratchet effect** where progress is preserved even under pressure.

### Starting a New Project

When beginning with SAID:

1. **Create Initial Vision** (not commands, human work)
   - Write a brief problem statement
   - Identify key stakeholders
   - Define success criteria

2. **Initialize Context Structure**
   - Set up the four-file system
   - Prime with initial vision
   - Ready for Level 0 investigation

3. **Begin the Spiral**
   - Start with problem validation
   - Surface risks early
   - Let discoveries guide the path

### Recovering from Interruption

Projects get interrupted. SAID's context preservation makes recovery straightforward:

1. **Read Your Context** - Start with project-context.md
2. **Review Recent Decisions** - Check decisions-made.md for latest choices
3. **Check Open Questions** - See what was pending in open-questions.md
4. **Prime and Continue** - Brief the AI and resume where you left off

### Handling Discoveries

When you discover something that changes your understanding:

1. **Document the Discovery** - What did you learn?
2. **Assess Impact** - Does this invalidate previous decisions?
3. **Navigate Accordingly** - Loop back if needed or adjust path forward
4. **Update Context** - Ensure learning is preserved

### The Pressure Valve Pattern

When timeline pressure mounts, SAID provides structured degradation:

**Moderate Pressure**: Combine investigation steps but maintain decision documentation
**High Pressure**: Jump to implementation but preserve critical context
**Extreme Pressure**: Emergency mode - build minimum viable, document debt for recovery

The key: **Always preserve enough context to recover** when pressure subsides.

---

## Common Challenges and Solutions

### "The AI Keeps Suggesting Things We Already Rejected"

**Root Cause**: Incomplete context about previous decisions

**Solution**:
- Ensure decisions-made.md captures rejected alternatives
- Use context priming to remind AI of key decisions
- Reference specific decision rationale when it matters

### "We Keep Revisiting the Same Questions"

**Root Cause**: Decisions made without sufficient investigation

**Solution**:
- Loop back to appropriate level for deeper investigation
- Document why the question keeps arising
- Consider if there's a hidden constraint not yet surfaced

### "The Spiral Feels Too Slow"

**Root Cause**: Trying to achieve perfection at each level

**Solution**:
- Focus on resolving critical unknowns, not all unknowns
- Use strategic deferral for non-critical decisions
- Remember: the spiral prevents rework, which is slower than investigation

### "Context Files Are Getting Unwieldy"

**Root Cause**: Accumulating without organizing

**Solution**:
- Periodically consolidate related decisions
- Archive completed phases while keeping references
- Focus on active context, not historical record

---

## Integration with Development Practices

### Git and Version Control

SAID context files are **first-class citizens** in your repository:

- Check in context files alongside code
- Version control preserves decision history
- Pull requests can include context updates
- Branch names can reflect spiral level:
  - `investigation/payment-options`
  - `prototype/test-stripe-integration`
  - `implementation/user-authentication`

### Code Review Through SAID Lens

When reviewing code with SAID context:

- **Check alignment**: Does implementation match documented decisions?
- **Question deviations**: If code differs from plan, is there a good reason?
- **Preserve learning**: Discoveries during implementation should update context
- **Review depth**: Match review thoroughness to documented risk level

### Testing Strategy Alignment

SAID's risk identification (Level 0) and approach decisions (Level 1) should **directly inform** your testing strategy:

- High-risk areas need comprehensive testing
- Deferred decisions need tests that allow flexibility
- Prototype code might skip tests but document why
- Integration points identified in Level 2 become integration test targets

---

## Closing Thoughts

SAID isn't a rigid process - it's a **philosophy of thoughtful progress** through uncertainty. The commands and structure support this philosophy, but the core is:

1. **Make uncertainty explicit** rather than hiding it
2. **Preserve context** for future humans and AI
3. **Navigate adaptively** based on what you discover
4. **Collaborate effectively** with both humans and AI

The spiral method acknowledges that software development is a journey of discovery. SAID provides the tools to make that journey more predictable, recoverable, and ultimately successful.

For specific command usage and syntax, refer to the [HOW-TO Guide](../getting-started/HOW-TO.md). For the underlying principles and theory, see the [SAID Philosophy](philosophy.md).

