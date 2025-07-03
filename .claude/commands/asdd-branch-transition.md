## Usage

```
/asdd-branch-transition <from-level> <to-level> [transition-type]
```

## Command Guidelines

### Branch Transition Manager

**Focus**: Manage git branch creation, merging, and transitions between ASDD levels
**Success criteria**: Clean branch transitions with context preservation and validation gates
**Output**: Properly configured branches for next ASDD level with complete context transfer

### Transition Types

**1. Forward Progression**
- Move from completed level to next level
- Create new branch from completed level
- Preserve context and decisions
- Standard advancement workflow

**2. Spiral Navigation (Backward)**
- Revisit previous level due to discoveries
- Create revision branch from earlier level
- Document reasons for backward navigation
- Maintain context integrity

**3. Emergency Transition**
- Rapid transition under pressure
- Bypass normal validation gates temporarily
- Create tracking for post-emergency cleanup
- Maintain minimum quality standards

**4. Context Sync**
- Dedicated branch for context updates
- Merge context changes across levels
- Resolve context conflicts
- Preserve decision audit trail

### Branch Naming Conventions

**Standard Level Branches**:
- `level-0-vision`
- `level-1-approach`
- `level-2-structure`
- `level-3-specifics`
- `level-4-implementation`

**Revision Branches**:
- `level-1-approach-revision-{reason}`
- `level-2-structure-revision-{date}`

**Special Purpose Branches**:
- `prototype-{risk-name}`
- `context-sync-{phase}`
- `emergency-{description}`

### Transition Workflows

**Forward Progression Workflow**:
```bash
# 1. Ensure current level is completed and merged
git checkout main && git pull

# 2. Verify previous level completion
git log --oneline | grep "level-{current}: completion"

# 3. Create new level branch
git checkout -b level-{next}-{name}

# 4. Initialize level context
# Update context manifest for new level
git add context/ && git commit -m "level-{next}: initialize context for {name} phase"

# 5. Begin level work
# ... level-specific work ...

# 6. Regular context preservation
git add . && git commit -m "level-{next}: {specific-decision} with rationale"
```

**Spiral Navigation (Backward) Workflow**:
```bash
# 1. Identify revision point
git checkout level-{target}-{name}

# 2. Create revision branch
git checkout -b level-{target}-{name}-revision-{reason}

# 3. Document revision reasons
# Update context with discoveries that triggered revision
git add context/ && git commit -m "level-{target}: revision required due to {discovery}"

# 4. Implement revisions
# ... revision work ...

# 5. Update dependent levels
# Identify and update any dependent work from later levels
```

**Emergency Transition Workflow**:
```bash
# 1. Create emergency branch
git checkout -b emergency-{description}

# 2. Document emergency context
# Record why emergency transition is necessary
git add . && git commit -m "emergency: {reason} - bypass normal validation temporarily"

# 3. Implement emergency solution
# ... emergency work ...

# 4. Create cleanup tracking
# Create issue or task for post-emergency cleanup
gh issue create --title "Emergency Cleanup: {description}" --body "Post-emergency validation and documentation required"
```

### Context Preservation During Transitions

**Context Manifest Updates**:
```yaml
transition_log:
  - transition_id: "T001"
    from_level: "level-1-approach"
    to_level: "level-2-structure"
    transition_type: "forward"
    transition_date: "2025-07-03"
    trigger_reason: "approach validation completed successfully"
    context_changes:
      - "Added database technology decision"
      - "Updated integration constraints"
      - "Confirmed performance requirements"
    
  - transition_id: "T002"
    from_level: "level-2-structure"
    to_level: "level-1-approach-revision"
    transition_type: "backward"
    transition_date: "2025-07-04"
    trigger_reason: "discovered integration complexity in level-2"
    context_changes:
      - "Revised API approach due to integration constraints"
      - "Updated technology selection rationale"
```

### Validation Gates

**Pre-Transition Validation**:
- Current level completion verified
- Context integrity checked
- No unresolved conflicts
- All decisions documented

**Post-Transition Validation**:
- New branch created successfully
- Context manifest updated
- Next level initialized
- Team notifications sent

### Integration with Pull Requests

**Transition PR Creation**:
```bash
# Create PR for level completion
gh pr create --title "Level {n}: {Name} Completion" --body "$(cat <<'EOF'
## Level {n} Completion

### Deliverables
- [ ] All level objectives met
- [ ] Context manifest updated
- [ ] Validation gates passed
- [ ] Next level preparation completed

### Transition Information
- **Next Level**: level-{n+1}-{name}
- **Transition Type**: Forward progression
- **Context Changes**: [list key context updates]

### Validation Results
- [ ] Technical validation completed
- [ ] Domain expert review completed
- [ ] Context integrity verified
- [ ] Team approval received
EOF
)"

# Merge after validation
gh pr merge --squash --delete-branch

# Create next level branch
git checkout main && git pull
git checkout -b level-{n+1}-{name}
```

### Error Handling and Recovery

**Common Issues and Solutions**:

**Merge Conflicts During Transition**:
```bash
# Create conflict resolution branch
git checkout -b context-sync-merge-resolution

# Resolve conflicts manually
# ... conflict resolution ...

# Commit resolution
git add . && git commit -m "context: resolve merge conflicts between level-{n} and level-{n+1}"

# Create PR for conflict resolution
gh pr create --title "Context Sync: Merge Conflict Resolution"
```

**Missing Context During Transition**:
```bash
# Recover context from git history
git log --oneline -- context/

# Find last known good context state
git show {commit-hash}:context/project-context.yml

# Restore and update context
git checkout {commit-hash} -- context/project-context.yml
git add context/ && git commit -m "context: restore from {commit-hash} and update for current level"
```

## Command

You are the Branch Transition Manager for ASDD v1.0.3.

Your mission: Manage smooth transitions between ASDD levels while preserving context and maintaining validation gates.

**Process:**
1. **CURRENT STATE ASSESSMENT**: Verify current level completion and context state
2. **TRANSITION VALIDATION**: Ensure prerequisites met for transition type
3. **BRANCH MANAGEMENT**: Create/manage branches according to ASDD conventions
4. **CONTEXT PRESERVATION**: Update context manifest with transition information
5. **VALIDATION GATES**: Execute appropriate validation for transition type
6. **PR MANAGEMENT**: Create pull requests with ASDD validation templates
7. **NEXT LEVEL INITIALIZATION**: Prepare next level branch and context

**Transition Types:**
- **forward**: Standard progression to next level
- **backward**: Spiral navigation to previous level for revision
- **emergency**: Rapid transition under pressure with cleanup tracking
- **context-sync**: Dedicated context synchronization

**Outputs:**
- Properly configured branch for target level
- Updated context manifest with transition log
- Pull request for validation (if applicable)
- Next level initialization
- Team notifications

Manage transition from {from-level} to {to-level} using {transition-type} workflow.