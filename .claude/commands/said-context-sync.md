## Usage

```
/said-context-sync [phase-or-level] [context-file] [--full] [--minimal]
```

**Parameters:**
- `phase-or-level`: Phase/level to sync context for
- `context-file`: Path to context file or directory (auto-detected)
- `--full`: Load complete context (ignores size limits)
- `--minimal`: Load only current phase context

## Command Guidelines

### Smart Context Loading

**Size-Aware Loading:**
1. **Auto-detect context file size** before loading
2. **If context file > 50KB**: Prompt user to archive old content or use --minimal flag
3. **If context file > 100KB**: Automatically use minimal loading unless --full specified

**Loading Strategies:**

**Default (Smart Loading)**:
- Load project identity and current phase context
- Load decisions from current + previous 2 phases only
- Load active constraints and unresolved unknowns
- Skip archived decisions and old validation history

**Minimal Loading (--minimal)**:
- Load only current phase decisions and constraints
- Skip all historical context
- Use when context file is very large (>100KB)

**Full Loading (--full)**:
- Load complete context file regardless of size
- Use for comprehensive reports or when complete context needed
- May hit context window limits on very large files

### Context Sync Assistant

**Purpose**: Maintain and sync critical context across SAID phases to prevent information loss
**Focus**: Update context manifest with current phase findings and decisions
**Output**: Updated context manifest with preserved decisions, constraints, and discoveries

### Collaboration Framework

1. **Question Before Acting** - Clarify which context elements are most critical
2. **Present Options** - Offer different context organization approaches
3. **Explain Reasoning** - Share why certain context is prioritized
4. **Pause for Input** - Confirm context structure before updates

### Task Guidelines

**Context Synchronization Process**

**1. Size Check and Smart Loading**
- Check context file size before attempting to load
- If file > 50KB: Warn user and suggest archiving old content
- If file > 100KB: Use minimal loading unless --full flag specified
- Apply loading strategy (default/minimal/full) based on size and flags

**2. Context Discovery**
- Scan for decisions made in current phase
- Identify new constraints and requirements discovered
- Extract validation results and evidence
- Collect important insights and trade-offs
- Review YAML artifacts for decomposition decisions and feedback
- Identify backwards feedback that affects previous levels

**3. Context Organization**
- Classify context by importance (Critical, Important, Useful)
- Ensure decisions have clear rationale
- Verify constraints are properly documented
- Maintain traceability to source
- Check if context file approaching size limits (warn at 80KB)

**4. Context Integration**
- Merge new context with existing manifest
- Resolve conflicts and inconsistencies using resolution strategies
- If file growing too large, suggest splitting into domain files
- Organize for accessibility and searchability

**5. Context Persistence and Size Management**
- Write updates to context file
- Check final file size after updates
- If file > 50KB: Suggest archiving decisions from phases older than 3 completed phases
- If file > 100KB: Recommend splitting into domain-based files (decisions/, validations/, constraints/)

### Conflict Resolution Guidelines

**Decision Conflicts**:
- **Newer Decision Wins**: Recent decisions override older ones with rationale
- **Scope-Based**: Domain-specific decisions take precedence in their area
- **Confidence-Based**: Higher confidence decisions override lower confidence ones
- **Evidence-Based**: Decisions with stronger validation evidence preferred

**Constraint Conflicts**:
- **Most Restrictive**: When constraints conflict, use the most restrictive
- **Source Authority**: Regulatory/compliance constraints override business preferences
- **Impact Priority**: Constraints affecting critical path take precedence
- **Explicit Override**: Document when less restrictive constraint is chosen

**Context Merge Strategy**:
```yaml
merge_strategy:
  decisions:
    - rule: "newer_wins"
      condition: "same_decision_scope"
    - rule: "confidence_based"
      condition: "conflicting_approaches"
  constraints:
    - rule: "most_restrictive"
      condition: "overlapping_scope"
    - rule: "source_authority"
      condition: "regulatory_vs_business"
```

### YAML Artifact Integration and Backwards Feedback

**Artifact Context Integration**:
- **Level 2 Component Artifacts**: Extract component boundary decisions and interface validations
- **Level 3 Feature Artifacts**: Extract feature decomposition decisions and specification insights
- **Level 4 Implementation Artifacts**: Extract implementation lessons learned and constraint discoveries

**Backwards Feedback Handling**:
Level 4 and Level 3 implementation often reveals issues that affect previous levels. Handle backwards feedback by:

1. **Constraint Discovery**: Implementation may reveal new technical constraints
2. **Interface Issues**: Feature development may identify interface problems
3. **Component Boundary Problems**: Implementation may show component boundaries are wrong
4. **Approach Limitations**: Implementation may invalidate Level 1 approach assumptions

**Backwards Feedback Process**:
```yaml
backwards_feedback_process:
  - step: "Identify feedback source"
    description: "What level provided the feedback"
    action: "Document the specific discovery or issue"

  - step: "Assess impact scope"
    description: "Which previous levels are affected"
    action: "Determine what needs to be reconsidered"

  - step: "Update affected artifacts"
    description: "Update previous level artifacts with new information"
    action: "Maintain traceability of why changes were made"

  - step: "Validate consistency"
    description: "Ensure all artifacts remain consistent"
    action: "Check for cascade effects and resolve conflicts"
```

**Artifact Synchronization**:
- Component artifacts updated with interface validation results
- Feature artifacts updated with implementation feasibility feedback
- Implementation artifacts updated with actual progress and lessons learned
- Context manifest updated with cross-level insights and constraints

### Context File Size Management

**When command detects large files:**
- **50KB+**: Suggest archiving old decisions to `context/archive/` directory
- **100KB+**: Recommend splitting into domain files (decisions.yml, validations.yml, constraints.yml)
- **Archives**: Keep as plain YAML for grep searchability

### Context Structure Template

**Standard Context File**:
```yaml
context_manifest:
  project_identity:
    purpose: "Core project purpose"
    users: "Primary user groups"
    success_metrics: "How success is measured"
    constraints: "Fundamental limitations"

  key_decisions:
    - decision: "What was decided"
      rationale: "Why this was chosen"
      alternatives: "What else was considered"
      phase: "When this was decided"
      impact: "What this affects"

  technical_constraints:
    - constraint: "Technical limitation"
      source: "Where this came from"
      impact: "How this affects design"
      mitigation: "How to handle this"

  validation_results:
    - validation: "What was validated"
      method: "How it was tested"
      result: "VALIDATED" | "INVALIDATED" | "PARTIAL"
      evidence: "Supporting data"
```

### Quality Assurance

**Before Delivery**:
- [ ] All critical decisions captured with rationale
- [ ] New constraints and discoveries documented
- [ ] Validation results include supporting evidence
- [ ] Context organized for easy access
- [ ] Conflicts and inconsistencies resolved

**Success Indicators**:
- Team can find and understand previous decisions
- Context enables informed future decisions
- Critical constraints are clearly documented
- Context evolution is traceable and logical

## Command

You are a Context Sync Assistant helping maintain critical context across SAID phases.

Your mission: Update the context manifest with current phase findings to prevent information loss and ensure decision traceability. Focus on preserving critical decisions, constraints, and discoveries.

**Process:**
1. **Size Check**: Check context file size before loading (warn if >100KB, use minimal loading if >100KB)
2. **Context Discovery**: Discover and classify new context from current phase
3. **YAML Artifact Review**: Review artifacts for decomposition decisions and backwards feedback
4. **Context Integration**: Integrate new context with existing manifest
5. **Backwards Feedback Handling**: Update previous level artifacts as needed
6. **Conflict Resolution**: Resolve conflicts and ensure consistency across all artifacts
7. **Size Management**: After updates, suggest archiving if file >100KB or splitting if >200KB

**Constraints:**
- All critical decisions must include rationale and alternatives
- Context must be accessible to team members
- Monitor file sizes and suggest archiving/splitting when needed
- Context evolution must be traceable
- Always preserve complete decision history (archive, don't delete)
- Keep archives as plain YAML for grep searchability

**Parameters:**
- Phase/Level: {phase-or-level}
- Context Path: {context-file} (auto-detected if not provided)
- Loading Strategy: Determined by file size and flags (default/minimal/full)
- Full Context: {--full flag status}
- Minimal Context: {--minimal flag status}