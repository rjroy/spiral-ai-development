# Git Workflow Integration with ASDD v1.0.3

_Practical guidance for implementing branch protection and phase-aligned branching strategies_

---

## 🎯 Overview

This document provides comprehensive guidance for integrating git workflows with the AI Spec-Driven Development (ASDD) methodology. The approach combines branch protection with phase-aligned branching to reinforce collaboration boundaries and validation gates.

## 🔧 Repository Setup

### Initial Repository Configuration

**1. Branch Protection Setup**

```bash
# Configure main branch protection via GitHub CLI
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":[]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_reviews":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

**2. Branch Naming Convention**

```
main (protected)
├── level-0-vision
├── level-1-approach
├── level-2-structure
├── level-3-specifics
├── level-4-implementation
├── prototype-{risk-name}
└── context-sync-{phase}
```

**3. Repository Structure Integration**

```
project/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md    # ASDD-aligned PR template
│   └── workflows/
│       └── asdd-validation.yml     # Automated ASDD validation
├── context/                        # Context management
├── docs/                          # Documentation
└── .claude/                       # Claude commands
```

## 🌊 Phase-Aligned Branching Strategy

### Branch Lifecycle Management

**Phase 0: Prototype Validation**
```bash
# Create prototype branch for high-risk validation
git checkout -b prototype-auth-integration
# Work on throwaway prototype
git add . && git commit -m "prototype: validate OAuth integration approach"
# Create PR for validation discussion
gh pr create --title "Prototype: OAuth Integration Validation" --body "Risk validation for authentication approach"
```

**Level 0: Vision Clarity**
```bash
# Create vision branch from main
git checkout main && git pull
git checkout -b level-0-vision
# Work on vision documentation
git add . && git commit -m "level-0: define core project vision and success metrics"
# Create PR for vision validation
gh pr create --title "Level 0: Vision Clarity" --body "$(cat .github/PULL_REQUEST_TEMPLATE.md)"
```

**Level 1: Approach Viability**
```bash
# Create approach branch from completed vision
git checkout level-0-vision && git pull
git checkout -b level-1-approach
# Work on approach validation
git add . && git commit -m "level-1: validate technical approach and feasibility"
# Create PR for approach review
gh pr create --title "Level 1: Approach Viability" --body "Technical approach validation"
```

**Spiral Navigation (Backward)**
```bash
# When level-2 discoveries invalidate level-1 approach
git checkout level-1-approach
git checkout -b level-1-approach-revision
# Address discovered issues
git add . && git commit -m "level-1: revise approach based on level-2 discoveries"
```

### Context Preservation Through Git

**Context Sync Branches**
```bash
# Create dedicated branch for major context updates
git checkout -b context-sync-level-1
# Update context files
git add context/ && git commit -m "context: sync level-1 approach decisions and constraints"
# Merge context changes back to main
gh pr create --title "Context Sync: Level 1 Approach" --body "Context preservation for level-1 completion"
```

**Git History as Audit Trail**
```bash
# View decision history for a specific level
git log --oneline --grep="level-1"
# View context evolution
git log --oneline -- context/
# View spiral navigation decisions
git log --oneline --grep="revision"
```

## 🤝 Domain-Calibrated Code Review

### Review Assignment Strategy

**Simple Domains:**
```yaml
# .github/CODEOWNERS
# Simple domain code can be reviewed by team members
src/utils/          @team-members
src/components/ui/  @team-members
```

**Complex Domains:**
```yaml
# .github/CODEOWNERS
# Complex domains require domain expert review
src/auth/           @auth-expert @team-lead
src/payment/        @payment-expert @security-team
src/database/       @db-expert @backend-team
```

**Extreme Domains:**
```yaml
# .github/CODEOWNERS
# Extreme domains require multiple expert reviews
src/trading/        @trading-expert @compliance-team @security-team
src/medical/        @medical-expert @compliance-team @qa-team
```

### Pull Request Templates

**ASDD-Aligned PR Template** (`.github/PULL_REQUEST_TEMPLATE.md`):

```markdown
# ASDD Level Validation

## Level Information
- [ ] Level: [0-4] - [Vision/Approach/Structure/Specifics/Implementation]
- [ ] Phase: [Prototype/Level/Context-Sync]
- [ ] Domain Complexity: [Simple/Complex/Extreme]

## Validation Checklist

### Context Preservation
- [ ] Context manifest updated with key decisions
- [ ] Rationale documented for major choices
- [ ] Alternatives considered and documented
- [ ] Dependencies and constraints identified

### Domain-Calibrated Review
- [ ] **Simple Domain**: Basic integration and style review completed
- [ ] **Complex Domain**: Architectural review by domain expert completed
- [ ] **Extreme Domain**: Multiple expert reviews completed

### Bounded Replaceability
- [ ] Clear interfaces defined and documented
- [ ] Dependencies explicitly documented
- [ ] Replacement cost assessed and documented
- [ ] Behavioral contracts defined through tests

### ASDD Progression
- [ ] Level prerequisites satisfied
- [ ] Validation gates passed
- [ ] Next level preparation documented
- [ ] Spiral navigation decisions justified (if applicable)

## Testing Strategy
- [ ] Unit tests for new functionality
- [ ] Integration tests for interface changes
- [ ] End-to-end tests for critical paths
- [ ] Performance tests for scalability concerns

## Documentation Updates
- [ ] API documentation updated
- [ ] Architecture documentation updated
- [ ] Context files updated
- [ ] Troubleshooting guide updated

## Risk Assessment
- [ ] Technical risks identified and mitigated
- [ ] Integration risks assessed
- [ ] Performance impact evaluated
- [ ] Security implications reviewed

## Post-Merge Actions
- [ ] Monitoring and alerts configured
- [ ] Rollback plan documented
- [ ] Team notification completed
- [ ] Next phase preparation initiated
```

## 🔄 Automated Validation

### GitHub Actions Integration

**ASDD Validation Workflow** (`.github/workflows/asdd-validation.yml`):

```yaml
name: ASDD Validation
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  asdd-validation:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Validate Context Integrity
      run: |
        # Check context files are properly maintained
        if [ -f "context/project-context.yml" ]; then
          echo "✓ Context manifest found"
        else
          echo "✗ Context manifest missing"
          exit 1
        fi
    
    - name: Validate Branch Naming
      run: |
        BRANCH_NAME="${{ github.head_ref }}"
        if [[ "$BRANCH_NAME" =~ ^(level-[0-4]|prototype-|context-sync-) ]]; then
          echo "✓ Branch naming follows ASDD convention"
        else
          echo "✗ Branch naming does not follow ASDD convention"
          echo "Expected: level-{0-4}-{name}, prototype-{name}, or context-sync-{name}"
          exit 1
        fi
    
    - name: Validate PR Template Usage
      run: |
        # Check if PR description contains ASDD validation checklist
        if grep -q "Level Information" <<< "${{ github.event.pull_request.body }}"; then
          echo "✓ PR template used"
        else
          echo "✗ PR template not used"
          exit 1
        fi
    
    - name: Check Documentation Updates
      run: |
        # Verify documentation is updated for significant changes
        if git diff --name-only origin/main | grep -E '\.(md|yml|yaml)$' > /dev/null; then
          echo "✓ Documentation changes detected"
        else
          echo "⚠ No documentation changes detected"
        fi
```

## 📊 Workflow Examples

### Complete Level Implementation

**Example: Level 1 Approach Validation**

```bash
# 1. Create level branch
git checkout main && git pull
git checkout -b level-1-approach

# 2. Implement level requirements
# ... work on approach validation ...

# 3. Update context
git add context/
git commit -m "level-1: document approach decisions and technical constraints"

# 4. Create PR with validation
gh pr create --title "Level 1: Technical Approach Validation" \
  --body "Validates technical approach feasibility and documents key architectural decisions"

# 5. Address review feedback
git add . && git commit -m "level-1: address review feedback on database approach"

# 6. Merge after validation
gh pr merge --squash --delete-branch

# 7. Prepare next level
git checkout main && git pull
git checkout -b level-2-structure
```

### Spiral Navigation Example

**Example: Level 2 Discovery Invalidates Level 1**

```bash
# 1. Discover issue during level-2 work
git checkout level-1-approach
git checkout -b level-1-approach-revision-db

# 2. Address discovered issues
git add . && git commit -m "level-1: revise database approach based on level-2 integration constraints"

# 3. Create revision PR
gh pr create --title "Level 1 Revision: Database Approach" \
  --body "Revises database approach based on integration discoveries from level-2 work"

# 4. Merge revision
gh pr merge --squash --delete-branch

# 5. Rebase level-2 on updated level-1
git checkout level-2-structure
git rebase level-1-approach
```

### Emergency Procedures

**High-Pressure Situations**

```bash
# Emergency hotfix with tracking
git checkout main
git checkout -b emergency-security-patch
# Fix critical issue
git add . && git commit -m "emergency: patch security vulnerability"
# Create PR with emergency tag
gh pr create --title "EMERGENCY: Security Patch" \
  --body "Critical security fix - requires immediate review and cleanup tracking"
# Merge after minimal review
gh pr merge --squash --delete-branch
# Create cleanup tracking issue
gh issue create --title "Cleanup: Security Patch Documentation" \
  --body "Add comprehensive documentation and testing for emergency security patch"
```

## 🛠️ Integration with ASDD Commands

### Command Enhancement Examples

**Enhanced /level-1-approach Command**
```bash
# Auto-create branch for level
git checkout -b level-1-approach-$(date +%Y%m%d)

# Auto-update context after completion
git add context/ && git commit -m "level-1: sync context after approach validation"

# Auto-create PR
gh pr create --title "Level 1: Approach Validation" --body "$(cat .github/PULL_REQUEST_TEMPLATE.md)"
```

## 🔍 Troubleshooting

### Common Issues and Solutions

**Branch Protection Conflicts**
```bash
# Issue: Cannot push directly to main
# Error: "Updates were rejected because the remote contains work that you do not have locally"
# Solution: Always use feature branches and PRs
git checkout -b feature-branch
git push -u origin feature-branch
gh pr create

# Issue: Force push blocked by branch protection
# Error: "Cannot force-push to protected branch"
# Solution: Use regular commits and address issues through PR review
git add . && git commit -m "fix: address review feedback"
git push
```

**Context Sync Conflicts**
```bash
# Issue: Context files have merge conflicts
# Error: "Automatic merge failed; fix conflicts and then commit the result"
# Solution: Use context-sync branch for resolution
git checkout -b context-sync-resolution
# Edit files to resolve conflicts manually
# Remove conflict markers (<<<<<<<, =======, >>>>>>>)
git add context/ && git commit -m "context: resolve merge conflicts between level-1 and level-2"
gh pr create --title "Context Sync: Merge Conflict Resolution"
```

**Failed Validation Gates**
```bash
# Issue: PR validation fails
# Error: "Required status check failed"
# Solution: Fix validation issues before merge
gh pr checks --watch
# Common fixes:
# 1. Branch naming violation
git branch -m level-1-approach-validation
git push origin :old-branch-name
git push -u origin level-1-approach-validation

# 2. Missing PR template usage
# Edit PR description to include ASDD validation checklist

# 3. Context integrity failure
# Update context manifest with required fields
git add context/ && git commit -m "context: fix integrity validation"
```

**Authentication and Permissions Issues**
```bash
# Issue: GitHub CLI not authenticated
# Error: "This command requires you to be logged into github.com"
# Solution: Authenticate with GitHub CLI
gh auth login --web

# Issue: Insufficient permissions to configure branch protection
# Error: "Resource not accessible by integration"
# Solution: Use appropriate permissions or admin access
# Verify repository permissions:
gh api repos/:owner/:repo | jq '.permissions'
```

**Branch Naming and Organization Issues**
```bash
# Issue: Existing branch doesn't follow ASDD convention
# Solution: Rename branch to follow convention
git branch -m old-feature-name level-2-structure-validation
git push origin :old-feature-name
git push -u origin level-2-structure-validation

# Issue: Multiple branches for same level
# Solution: Consolidate or use revision naming
git checkout level-1-approach-v2
git checkout -b level-1-approach-revision-database
# Merge or cherry-pick relevant changes
git cherry-pick level-1-approach-v2
```

**Context File Management Issues**
```bash
# Issue: Context file corrupted or malformed YAML
# Error: "yaml: line X: found unexpected end of stream"
# Solution: Validate and fix YAML syntax
# Use online YAML validator or:
python -c "import yaml; yaml.safe_load(open('context/project-context.yml'))"

# Issue: Missing context during transition
# Solution: Recover from git history
git log --oneline --follow context/project-context.yml
git show commit-hash:context/project-context.yml > context/project-context.yml
git add context/ && git commit -m "context: restore from git history"
```

**Pull Request Template Issues**
```bash
# Issue: PR template not automatically loaded
# Solution: Ensure correct file location and name
mkdir -p .github
# Create or update template file
cat > .github/PULL_REQUEST_TEMPLATE.md << 'EOF'
# ASDD Level Validation
[template content]
EOF

# Issue: Multiple PR templates causing confusion
# Solution: Use specific templates in subdirectory
mkdir -p .github/PULL_REQUEST_TEMPLATE/
mv .github/PULL_REQUEST_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE/asdd-level.md
```

**Workflow Automation Issues**
```bash
# Issue: GitHub Actions workflow fails
# Error: Workflow validation errors
# Solution: Check workflow syntax and permissions
# Validate workflow YAML:
gh api repos/:owner/:repo/actions/workflows

# Issue: ASDD validation script not found
# Solution: Ensure validation scripts are in repository
# Add validation script to repository:
mkdir -p .github/scripts/
cat > .github/scripts/validate-asdd.sh << 'EOF'
#!/bin/bash
# ASDD validation logic
EOF
chmod +x .github/scripts/validate-asdd.sh
```

**Team Coordination Issues**
```bash
# Issue: Multiple team members working on same level
# Solution: Use branch protection and coordination
# Create coordination issue:
gh issue create --title "Level 2 Coordination" --body "Track parallel work on level-2-structure"

# Issue: Lost context during handoffs
# Solution: Use structured handoff process
# Create handoff documentation:
echo "## Handoff Notes" >> docs/handoff-level-1.md
echo "- Current state: approach validated" >> docs/handoff-level-1.md
echo "- Next steps: begin structure definition" >> docs/handoff-level-1.md
git add docs/ && git commit -m "docs: level-1 handoff documentation"
```

**Performance and Scale Issues**
```bash
# Issue: Large context files causing merge conflicts
# Solution: Split context into smaller, focused files
mkdir -p context/levels/
mv context/level-specific-context.yml context/levels/
# Update context sync scripts to handle multiple files

# Issue: Too many branches cluttering repository
# Solution: Regular cleanup of merged branches
# List merged branches:
git branch --merged main | grep -v main
# Delete merged branches:
git branch --merged main | grep -v main | xargs -n 1 git branch -d
```

### Emergency Recovery Procedures

**Complete Context Loss**
```bash
# 1. Stop all work immediately
# 2. Assess scope of loss
git log --oneline --all | grep -E "(level-|context)"

# 3. Recover from last known good state
git log --follow context/
# Find last good commit
git checkout last-good-commit -- context/

# 4. Reconstruct missing context from git history
git log --oneline --grep="level-" | head -20
# Review commit messages for key decisions

# 5. Create recovery tracking
gh issue create --title "EMERGENCY: Context Recovery" --label "emergency"
```

**Repository Corruption**
```bash
# 1. Create backup of current state
cp -r .git .git.backup
cp -r context context.backup

# 2. Re-clone from remote
cd ..
git clone repository-url repository-recovery
cd repository-recovery

# 3. Apply local changes carefully
# Compare with backup and apply selectively

# 4. Rebuild context from commits and documentation
git log --oneline --all | grep -E "(context|level-)"
```

**Branch Protection Misconfiguration**
```bash
# Issue: Cannot merge PRs due to misconfigured protection
# Solution: Fix protection rules via API
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["ASDD Validation"]}' \
  --field required_pull_request_reviews='{"required_approving_reviews":1}'

# Verify configuration:
gh api repos/:owner/:repo/branches/main/protection | jq '.'
```

### Monitoring and Metrics

**Git Workflow Health Metrics**
- Percentage of PRs using ASDD template
- Average time from branch creation to merge
- Frequency of spiral navigation (backward branches)
- Context integrity validation success rate

**Branch Management Metrics**
- Number of active branches per level
- Merge success rate by domain complexity
- Review completion time by domain type
- Emergency procedure usage frequency

## 🎯 Success Indicators

### Level 1 (Initial Implementation)
- [ ] All team members can create ASDD-aligned branches
- [ ] PR template usage >90%
- [ ] Context integrity maintained across merges
- [ ] Domain-calibrated reviews implemented

### Level 2 (Optimization)
- [ ] Automated validation catches 80% of issues
- [ ] Emergency procedures documented and tested
- [ ] Spiral navigation seamlessly handled
- [ ] Integration with existing tools completed

### Level 3 (Mastery)
- [ ] Workflow becomes natural team behavior
- [ ] Context degradation incidents <5%
- [ ] Review assignment automated based on domain
- [ ] Continuous improvement based on metrics

---

## 🔄 Evolution and Feedback

This git workflow integration will evolve based on:
- Team feedback and adoption challenges
- Integration successes and failures
- Pressure-testing under real project constraints
- Continuous improvement based on usage metrics

**Version**: 1.0.3  
**Integration Date**: 2025-07-03  
**Next Review**: After 5 projects using integrated workflow  
**Feedback Channel**: GitHub Issues on template repository  