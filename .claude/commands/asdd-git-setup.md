## Usage

```
/asdd-git-setup [repository-type]
```

## Command Guidelines

### Git Workflow Configuration Expert

**Focus**: Configure repository with ASDD-aligned git workflows and branch protection
**Success criteria**: Repository configured with branch protection, PR templates, and automated validation
**Output**: Fully configured git workflow with ASDD integration

### Repository Configuration Tasks

**1. Branch Protection Setup**
- Configure main branch protection
- Require pull request reviews
- Enforce status checks
- Dismiss stale reviews

**2. PR Template Creation**
- Create ASDD-aligned pull request template
- Include validation checklists for each level
- Add domain complexity assessment
- Include context preservation requirements

**3. GitHub Workflows Setup**
- Create automated validation workflows
- Branch naming validation
- Context integrity checks
- Documentation update verification

**4. Repository Structure**
- Create .github directory structure
- Set up CODEOWNERS for domain-calibrated review
- Configure issue templates
- Create workflow files

### Configuration Steps

**Branch Protection Configuration**:
```bash
# Configure main branch protection
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["ASDD Validation"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_reviews":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

**Repository Structure Creation**:
```
.github/
├── PULL_REQUEST_TEMPLATE.md    # ASDD validation template
├── ISSUE_TEMPLATE/
│   ├── level-validation.md     # ASDD level validation issues
│   └── context-sync.md         # Context synchronization issues
├── workflows/
│   ├── asdd-validation.yml     # Automated ASDD validation
│   └── context-integrity.yml   # Context preservation checks
└── CODEOWNERS                  # Domain-calibrated review assignments
```

### Domain-Calibrated CODEOWNERS

**Template CODEOWNERS File**:
```
# ASDD Domain-Calibrated Code Review
# Simple domains - basic team review
src/utils/                  @team-members
src/components/ui/          @team-members
docs/                       @team-members

# Complex domains - require domain expert + team lead
src/auth/                   @auth-expert @team-lead
src/api/                    @backend-expert @team-lead
src/database/               @db-expert @team-lead

# Extreme domains - require multiple expert reviews
src/payment/                @payment-expert @security-team @compliance-team
src/medical/                @medical-expert @compliance-team @qa-team

# ASDD Framework files - require methodology expert review
.claude/commands/           @asdd-expert @team-lead
context/                    @asdd-expert @team-lead
ASDD/                       @asdd-expert @team-lead
```

### Validation Workflows

**ASDD Validation Workflow**:
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
    
    - name: Validate Branch Naming
      run: |
        BRANCH_NAME="${{ github.head_ref }}"
        if [[ "$BRANCH_NAME" =~ ^(level-[0-4]|prototype-|context-sync-|emergency-) ]]; then
          echo "✓ Branch naming follows ASDD convention"
        else
          echo "✗ Branch naming violation: $BRANCH_NAME"
          echo "Expected: level-{0-4}-{name}, prototype-{name}, context-sync-{name}, or emergency-{name}"
          exit 1
        fi
    
    - name: Validate Context Integrity
      run: |
        if [ -f "context/project-context.yml" ]; then
          echo "✓ Context manifest found"
          # Additional context validation logic here
        else
          echo "✗ Context manifest missing"
          exit 1
        fi
    
    - name: Check PR Template Usage
      run: |
        if grep -q "ASDD Level Validation" <<< "${{ github.event.pull_request.body }}"; then
          echo "✓ ASDD PR template used"
        else
          echo "✗ ASDD PR template not used"
          exit 1
        fi
```

### PR Template

**ASDD Pull Request Template**:
```markdown
# ASDD Level Validation

## Level Information
- [ ] Level: [0-4] - [Vision/Approach/Structure/Specifics/Implementation]
- [ ] Phase: [Prototype/Level/Context-Sync/Emergency]
- [ ] Domain Complexity: [Simple/Complex/Extreme]
- [ ] Previous Level Completed: [Yes/No]

## Validation Checklist

### Context Preservation
- [ ] Context manifest updated with key decisions
- [ ] Rationale documented for major choices
- [ ] Alternatives considered and documented
- [ ] Dependencies and constraints identified
- [ ] Semantic checksum updated

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

## Risk Assessment
- [ ] Technical risks identified and mitigated
- [ ] Integration risks assessed
- [ ] Performance impact evaluated
- [ ] Security implications reviewed

## Post-Merge Actions
- [ ] Context sync completed
- [ ] Next phase branch prepared
- [ ] Team notification completed
- [ ] Documentation updated
```

## Command

You are the Git Workflow Configuration Expert for ASDD v1.0.3.

Your mission: Configure the repository with all necessary git workflow components to support ASDD methodology.

**Process:**
1. **REPOSITORY ASSESSMENT**: Check current repository configuration
2. **BRANCH PROTECTION**: Set up main branch protection with appropriate rules
3. **TEMPLATE CREATION**: Create ASDD-aligned PR and issue templates
4. **WORKFLOW SETUP**: Configure automated validation workflows
5. **CODEOWNERS SETUP**: Create domain-calibrated review assignments
6. **VALIDATION**: Test configuration with sample branch and PR
7. **DOCUMENTATION**: Update project documentation with git workflow guidance

**Configuration Options:**
- **Standard**: Basic ASDD git workflow for most projects
- **Enterprise**: Enhanced workflow with additional compliance and security checks
- **Simple**: Lightweight workflow for small teams or simple domains
- **Custom**: User-specified configuration based on specific requirements

**Outputs:**
- Configured branch protection
- ASDD PR template
- Automated validation workflows
- CODEOWNERS file
- Updated documentation

Configure ASDD git workflow for repository type: {repository-type}