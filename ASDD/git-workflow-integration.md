# Git Workflow Integration with ASDD v1.0.3

_Flexible guidance and suggestions for integrating git workflows with AI collaboration patterns_

---

## 🎯 Overview

This document provides flexible guidance for integrating git workflows with the AI Spec-Driven Development (ASDD) methodology. These are suggestions and best practices that teams can adapt to their specific needs, not rigid requirements. The focus is on supporting collaboration and quality through thoughtful workflow design.

## 🔧 Repository Setup Suggestions

### Initial Repository Configuration

**1. Branch Protection Considerations**

Teams may want to consider branch protection to support collaborative review:

```bash
# Example: Configure main branch protection via GitHub CLI
# Note: Adjust these settings based on your team's needs
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":[]}' \
  --field enforce_admins=false \  # Consider your team's workflow needs
  --field required_pull_request_reviews='{"required_approving_reviews":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

**Key Considerations**:
- `enforce_admins`: Set to `false` if admins need flexibility for urgent fixes
- `required_approving_reviews`: Adjust based on team size and domain complexity
- Status checks: Configure based on your CI/CD pipeline

**2. Suggested Branch Naming Conventions**

Consistent naming helps team coordination. Here's a suggested pattern aligned with ASDD phases:

```
main
├── feature/{descriptive-name}     # Standard GitHub Flow
├── level-{n}-{description}        # ASDD phase-aligned (optional)
├── prototype-{risk-name}          # For throwaway experiments
└── hotfix-{issue-description}     # For urgent fixes
```

**Naming Guidelines**:
- Use descriptive names that convey intent
- Include ticket/issue numbers when applicable
- Keep names concise but meaningful
- Consider prefixes that help with sorting and filtering

**3. Suggested Repository Structure**

```
project/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md    # Optional: PR checklist template
│   └── workflows/                  # Optional: CI/CD workflows
├── context/                        # ASDD context preservation
├── docs/                          # Project documentation
└── .claude/                       # Claude command customizations
```

**Note**: Adapt this structure to your project's needs. Not all elements are necessary for every project.

## 🌊 Suggested Git Workflow Patterns

### GitHub Flow with ASDD Naming Suggestions

We recommend using GitHub Flow - a simple, flexible branching model where you:
1. Create a branch from main
2. Make changes and commit
3. Open a pull request
4. Review and discuss
5. Merge to main

**Example: Working on Different ASDD Phases**

```bash
# For prototyping high-risk features
git checkout -b prototype-auth-integration
# Experiment freely - this branch may be throwaway
git add . && git commit -m "prototype: test OAuth integration approach"
gh pr create --draft --title "[Prototype] OAuth Integration Test"

# For feature development
git checkout -b feature/user-authentication
# Clear commits with good messages
git add . && git commit -m "feat: add JWT token validation"
gh pr create --title "Add user authentication system"

# For documenting project vision (if using ASDD levels)
git checkout -b docs/level-0-vision
git add . && git commit -m "docs: define project vision and success metrics"
gh pr create --title "Document project vision and goals"
```

**Commit Message Suggestions**:
- Use conventional commits (feat:, fix:, docs:, etc.)
- Reference issue numbers when applicable
- Keep messages clear and descriptive
- Focus on the "why" not just the "what"

### Context Preservation Best Practices

Preserve important decisions and context through:

**1. Context Files in Repository**
```yaml
# context/project-context.yml
context_manifest:
  key_decisions:
    - decision: "Chose PostgreSQL over MongoDB"
      rationale: "Need ACID compliance for financial data"
      date: "2025-07-01"
      alternatives_considered: ["MongoDB", "DynamoDB"]
```

**2. Meaningful Commit Messages**
```bash
# Include context in commits
git commit -m "feat: add user auth - JWT chosen for stateless architecture"

# Reference decisions in PR descriptions
gh pr create --body "Implements auth system as decided in context/decisions/auth.md"
```

**3. Git History for Audit Trail**
```bash
# Find when decisions were made
git log --oneline -- context/
# Search for specific topics
git log --grep="authentication" --oneline
# View file history
git log --follow context/project-context.yml
```

## 🤝 Thoughtful Code Review Practices

### Domain Complexity Considerations

Consider matching review requirements to code complexity:

**Simple Domains** (utilities, UI components):
- Any team member can review
- Focus on code style and basic functionality
- Quick turnaround expected

**Complex Domains** (auth, data processing):
- Consider involving domain experts
- Review architecture and security implications
- Allow time for thorough review

**Extreme Domains** (payments, healthcare, trading):
- Multiple expert reviews recommended
- Consider compliance requirements
- Document review decisions

**Optional: Using CODEOWNERS**
If your team finds it helpful, GitHub's CODEOWNERS file can suggest reviewers:

```yaml
# .github/CODEOWNERS (example)
# This is optional - adapt to your team's structure
*.js        @frontend-team
*.py        @backend-team
/docs/      @documentation-team

# Sensitive areas might need specific reviewers
/src/auth/  @security-team
/src/payment/ @payment-team @security-team
```

### Pull Request Templates

**Suggested PR Checklist Template**

Consider using a PR template to encourage thoughtful review. Here's an example that teams can adapt:

`.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Description
Brief description of changes and why they're needed.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other: [specify]

## Review Checklist

**Consider these review points:**
- [ ] Tests added/updated as needed
- [ ] Documentation updated if interfaces changed
- [ ] Major decisions documented (consider adding to context/)
- [ ] Security implications considered
- [ ] Performance impact assessed for large-scale changes

## Domain Complexity
Is this change in a complex domain that needs special review?
- [ ] No - standard review is fine
- [ ] Yes - please suggest appropriate reviewers

## Additional Notes
Any context that would help reviewers?

---
*Tip: Adapt this template to your team's needs. Remove items that don't apply.*
```

**Why Use Checklists?**
- Encourage thoughtful review without being prescriptive
- Remind developers of important considerations
- Can be adapted per project needs
- Not meant to be blindly checked - each item should prompt thinking

## 🔄 Quality Assurance Approaches

### Manual Review Checklists Over Automation

We recommend thoughtful manual review over rigid automated enforcement. Here's why:

1. **Flexibility**: Every project has unique needs
2. **Thoughtfulness**: Checklists prompt thinking, not blind compliance
3. **Adaptability**: Teams can adjust practices as they learn
4. **Trust**: Developers are trusted to make good decisions

### Suggested Review Checklist for PRs

**Before Merging, Consider:**

```markdown
## Pre-Merge Checklist

### Code Quality
- [ ] Code follows team style guidelines
- [ ] No obvious bugs or security issues
- [ ] Performance implications considered
- [ ] Error handling is appropriate

### Testing
- [ ] New functionality has tests
- [ ] Existing tests still pass
- [ ] Edge cases considered
- [ ] Manual testing completed where needed

### Documentation
- [ ] Code is self-documenting or has comments where needed
- [ ] API changes are documented
- [ ] Complex decisions are explained
- [ ] README updated if needed

### Context Preservation (for significant changes)
- [ ] Major decisions added to context files
- [ ] Trade-offs documented
- [ ] Future maintainers will understand why
```

### Optional: Automated Checks

If your team wants some automation, focus on objective checks:

```yaml
# .github/workflows/ci.yml (example)
name: CI
on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Run tests
      run: npm test
    - name: Check lint
      run: npm run lint
```

**Note**: Keep automation focused on objective quality (tests, lint) not process compliance.

## 📊 Workflow Examples

### Standard Feature Development

**Example: Implementing User Authentication**

```bash
# 1. Create feature branch
git checkout main && git pull
git checkout -b feature/user-authentication

# 2. Develop feature with clear commits
git add src/auth
git commit -m "feat: add JWT token generation"

git add tests/
git commit -m "test: add auth service unit tests"

# 3. Document important decisions
echo "Chose JWT for stateless auth..." >> context/decisions/auth.md
git add context/
git commit -m "docs: document authentication approach decision"

# 4. Create PR for review
gh pr create --title "Add user authentication" \
  --body "Implements JWT-based authentication as discussed in #42"

# 5. Address feedback and merge
git add . && git commit -m "fix: address PR feedback on token expiry"
gh pr merge --squash
```

### Handling Design Changes

**Example: Updating Approach Based on New Information**

```bash
# 1. Create branch for updates
git checkout -b refactor/update-database-approach

# 2. Make changes and document why
git add . && git commit -m "refactor: switch to PostgreSQL for better JSON support

After testing MongoDB, we found PostgreSQL's JSONB type better
suited our semi-structured data needs while maintaining ACID."

# 3. Update context with decision
echo "Changed from MongoDB to PostgreSQL..." >> context/decisions/database.md
git add context/ && git commit -m "docs: document database change rationale"

# 4. Create PR with clear explanation
gh pr create --title "Switch database to PostgreSQL" \
  --body "Updates database choice based on prototype findings. See context/decisions/database.md"
```

### Handling Urgent Changes

**When Time is Critical**

```bash
# For critical fixes
git checkout -b hotfix/security-vulnerability

# Make focused fix
git add . && git commit -m "fix: patch XSS vulnerability in user input"

# Create PR with urgency noted
gh pr create --title "[URGENT] Security: Fix XSS vulnerability" \
  --body "Critical security fix. Minimal change to sanitize user input."

# After merge, create follow-up issue
gh issue create --title "Follow-up: Add comprehensive XSS tests" \
  --body "The urgent fix addressed the immediate issue. We should add comprehensive tests."
```

**Key Points for Urgent Changes**:
- Keep changes minimal and focused
- Document what was done and why
- Create follow-up issues for comprehensive fixes
- Don't skip code review unless absolutely necessary

## 🛠️ Working with ASDD Commands

### Suggested Git Integration Patterns

If using ASDD commands, consider these git workflow patterns:

**When Starting a New ASDD Level:**
```bash
# Create a descriptive branch
git checkout -b feature/define-project-vision  # More descriptive than "level-0"

# Use clear commit messages
git add . && git commit -m "docs: define initial project vision and goals"

# Reference ASDD level in PR if helpful
gh pr create --title "Define project vision (ASDD Level 0)" \
  --body "Initial project vision as part of ASDD discovery process"
```

**Key Suggestions:**
- Use branch names that describe the work, not just the process
- Keep commits focused and well-described
- Reference ASDD phases in PRs only when it adds clarity
- Preserve important decisions in context files

## 🔍 Common Git Workflow Tips

### Working with Protected Branches

If your team uses branch protection:

```bash
# Can't push to main? That's by design! Create a feature branch:
git checkout -b feature/my-new-feature
git push -u origin feature/my-new-feature
gh pr create

# Need to update your PR? Just push normally:
git add . && git commit -m "address review feedback"
git push  # No force push needed
```

### Handling Merge Conflicts

**For Context Files:**
```bash
# Pull latest changes
git pull origin main

# If conflicts occur in context files:
# 1. Open the conflicted file
# 2. Look for conflict markers: <<<<<<<, =======, >>>>>>>
# 3. Decide which changes to keep (often you want both)
# 4. Remove the conflict markers
# 5. Stage and commit
git add context/
git commit -m "merge: resolve context file conflicts"
```

**Tip**: For YAML files, ensure the result is still valid YAML after merging.

### PR Best Practices

```bash
# Check your PR status
gh pr checks  # See CI status
gh pr view    # See PR details and comments

# Update PR description if needed
gh pr edit

# Common PR improvements:
# - Add more context to the description
# - Reference related issues
# - Add screenshots for UI changes
# - Summarize the "why" not just the "what"
```

### GitHub CLI Setup

**First Time Setup:**
```bash
# Authenticate with GitHub
gh auth login

# Check your auth status
gh auth status

# Set your preferred editor
gh config set editor "code --wait"  # or vim, nano, etc.
```

**Permissions Tips:**
```bash
# Check your permissions on a repo
gh api repos/:owner/:repo | jq '.permissions'

# Can't configure branch protection? You might need admin access
# Ask your repository admin to set it up
```

### Working with Context Files

**YAML Validation Tips:**
```bash
# Check if your YAML is valid
python -c "import yaml; yaml.safe_load(open('context/project-context.yml'))"
# Or use an online YAML validator

# Recover a file from git history if needed
git log --oneline --follow context/project-context.yml
git show <commit-hash>:context/project-context.yml > context/project-context.yml
```

**PR Template Location:**
```bash
# GitHub looks for PR templates here:
.github/PULL_REQUEST_TEMPLATE.md
# Or in a subdirectory for multiple templates:
.github/PULL_REQUEST_TEMPLATE/feature.md
.github/PULL_REQUEST_TEMPLATE/bugfix.md
```

### Team Coordination Tips

**Working in Parallel:**
```bash
# Communicate about who's working on what
gh issue create --title "Working on auth feature" \
  --body "I'll be implementing the authentication system this week"

# Use draft PRs for work in progress
gh pr create --draft --title "WIP: Authentication system"

# Keep branches small and focused to reduce conflicts
```

**Branch Cleanup:**
```bash
# See what branches have been merged
git branch --merged main

# Clean up old branches (locally)
git branch -d old-feature-branch

# Clean up on remote
git push origin --delete old-feature-branch
```

### Recovery Tips

**If Something Goes Wrong:**

```bash
# Lost a file? Check git history
git log --oneline --follow path/to/file
git show <commit>:path/to/file > recovered-file

# Messed up a merge? Start over
git merge --abort  # If still in merge
git reset --hard origin/main  # Nuclear option - loses local changes!

# Need to find when something changed?
git log -S "search term" --oneline  # Search file contents
git blame path/to/file  # See who changed each line
```

**Backup Before Big Changes:**
```bash
# Create a backup branch
git branch backup-before-refactor

# Or tag the current state
git tag -a "before-major-change" -m "Backup before refactoring auth"
```

## 🎯 Signs of Healthy Git Workflows

### What Good Looks Like

**Clear Communication:**
- PRs have descriptive titles and context
- Commit messages explain the "why"
- Important decisions are documented
- Team members can understand changes months later

**Smooth Collaboration:**
- Reviews happen promptly
- Feedback is constructive
- Conflicts are rare and easily resolved
- Everyone knows how to contribute

**Maintained Quality:**
- Tests pass consistently
- Code follows team standards
- Documentation stays updated
- Technical debt is tracked

### Continuous Improvement

Consider periodically asking:
- What's working well with our workflow?
- What friction points do we encounter?
- Are our branch names helping or confusing?
- Do our PR templates add value or feel like busywork?

Adjust practices based on what you learn. No workflow is perfect for every team.

---

## 🔄 Adapting These Suggestions

This document provides flexible guidance, not rigid rules. Every team is different, and what works for one may not work for another.

**Key Principles:**
- Start simple and add complexity only as needed
- Focus on practices that reduce friction, not add it
- Trust developers to make good decisions
- Adapt based on your team's experience

**Remember:** The best workflow is one that:
- Your team actually uses
- Helps rather than hinders
- Evolves with your needs
- Supports quality without bureaucracy

---

*This document offers suggestions based on common patterns. Adapt freely to your team's needs.*

**Version**: 1.0.3  
**Last Updated**: 2025-07-03  
**Philosophy**: Flexible guidance over rigid enforcement  