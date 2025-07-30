# Options Workflow Patterns

## End-to-End Options Process

### Workflow Overview
```
Detect Options → Extract Details → Present to User → Get Selection → Generate Context → Plan Integration
```

## Phase 1: Option Detection and Extraction

### Expert Document Reviewer Approach

#### Detection Philosophy
- Act as expert technical document reviewer
- Identify options and alternatives regardless of formatting
- Recognize choices, approaches, recommendations in any presentation style
- Extract core content (description, advantages, limitations, requirements)
- Identify implicit options and trade-offs not explicitly labeled
- Understand context clues indicating decision points

#### What to Look For
- Explicit options: "Option 1", "Alternative A", "Approach 1"
- Implicit alternatives: "We could also...", "Another way...", "Consider..."
- Comparison sections: "vs", "compared to", "alternatively"
- Trade-off discussions: "pros/cons", "advantages/disadvantages"
- Recommendation lists: "recommended", "suggested", "preferred"

#### Content to Extract
- **Description**: What the option actually is
- **Advantages**: Benefits, strengths, why it's good
- **Limitations**: Drawbacks, weaknesses, constraints
- **Requirements**: What's needed to implement
- **Effort**: Complexity, time, resources needed

## Phase 2: Option Presentation and Selection

### Standard Presentation Template
```markdown
## Available Options:
1. **[Option Name]** - [Brief description]
   - Pros: [Key advantages]
   - Cons: [Key limitations]
   - Effort: [Rough estimate]

2. **[Option Name]** - [Brief description]
   - Pros: [Key advantages]
   - Cons: [Key limitations]
   - Effort: [Rough estimate]

## Recommendation
**Suggested Option**: [Number] - [Name]
**Rationale**: [Why this seems like the best choice]
```

### User Interaction Stages

#### 1. Present Options
- Show numbered list with clear pros/cons
- Include effort estimates
- Highlight key differentiators
- Use consistent formatting

#### 2. Provide Recommendation
- Suggest best option based on analysis
- Explain rationale clearly
- Acknowledge when multiple options are viable
- Stay open to user preference

#### 3. Get User Choice
- Ask clearly: "Which option would you like to implement?"
- Accept user selection without argument
- Clarify if choice is unclear
- Proceed with selected option

## Phase 3: Context Generation and Integration

### Generate Implementation Context
- Create focused TODO context for chosen option
- Include specific details from report
- Maintain scope boundaries from original analysis
- Provide clear integration guidance

### Integration Planning
- Identify where option fits in existing work
- Determine dependencies and prerequisites
- Suggest appropriate next commands
- Maintain traceability to original analysis

## Collaboration Principles

### User Agency
- Present options, don't choose for user
- Respect user selection even if not recommended
- Explain reasoning but don't oversell
- Make final choice easy and clear

### Information Quality
- Extract accurate details from source
- Present balanced view of each option
- Don't hide important limitations
- Be honest about effort and complexity

### Decision Support
- Provide clear recommendation when possible
- Explain rationale for suggestions
- Acknowledge trade-offs explicitly
- Help user understand implications

## Quality Standards

### Option Clarity
- Clear, distinct options (not overlapping)
- Balanced pros/cons for each
- Honest effort estimates
- Implementation-relevant details

### Selection Process
- Clear presentation format
- Explicit user choice request
- Respectful of user decision
- Smooth transition to next steps

### Integration Quality
- Maintains context from analysis
- Clear path forward
- Appropriate scope boundaries
- Actionable next steps

## Integration with Other Patterns
- Uses `todo-structuring.md` for context generation after selection
- Uses `checkpoints.md` for when to pause (always ask user to select)
- Maintains consistency with `research-protocol.md` analysis quality