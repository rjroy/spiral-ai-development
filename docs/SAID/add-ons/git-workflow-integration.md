# Git Workflow Integration with SAID

_Flexible guidance and suggestions for integrating git workflows with AI collaboration patterns_

---

## 🎯 Overview

This document provides flexible guidance for integrating git workflows with the Spiral AI Development (SAID) methodology. These are suggestions and best practices that teams can adapt, modify, or ignore based on their specific context and constraints. The goal is to support SAID thinking, not enforce particular tools or processes.

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

Consistent naming helps team coordination. Here's a suggested pattern aligned with SAID phases:

```
main
├── feature/{descriptive-name}     # Standard GitHub Flow (recommended)
├── level-{n}/{description}        # SAID phase-aligned (recommended)
├── prototype/{experiment}         # For throwaway experiments
├── hotfix/{issue-description}     # For urgent fixes
```

**Naming Guidelines**:
- Use descriptive names that convey intent
- Include ticket/issue numbers when applicable
- Keep names concise but meaningful
- Consider prefixes that help with sorting and filtering

**3. Suggested Repository Structure**

Focus on the essentials that support SAID thinking:

```
project/
├── context/                       # SAID context management (core requirement)
├── docs/                          # Project documentation
├── .claude/                       # Claude commands (if using Claude Code)
├── .github/workflows              # GitHub CI/CD integration (if using GitHub)
└── [your existing project structure]
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

**Example: Working on Different SAID Phases**

```bash
# For prototyping high-risk features
git checkout -b prototype/auth-integration
# Experiment freely - this branch may be throwaway
git add . && git commit -m "prototype: test OAuth integration approach"
gh pr create --draft --title "[Prototype] OAuth Integration Test"

# For feature development
git checkout -b feature/user-authentication
# Clear commits with good messages
git add . && git commit -m "feat: add JWT token validation"
gh pr create --title "Add user authentication system"

# For documenting project vision (if using SAID levels)
git checkout -b level-0/user-analysis
git add . && git commit -m "Level 0: record results of user analysis"
gh pr create --title "Follow on level 0 task to analysis user edge cases"
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

## 🛠️ Working with ASDD Commands

### Suggested Git Integration Patterns

If using SAID commands, consider these git workflow patterns:

**When Starting a New SAID Level:**
```bash
# Create a descriptive branch
git checkout -b level-0/vision-review # More descriptive than "level-0"

# Use clear commit messages
git add . && git commit -m "docs: review and analysis vision and goals"

# Reference SAID level in PR if helpful
gh pr create --title "Refine project vision (SAID Level 0)" \
  --body "Initial project vision as part of SAID discovery process"
```

**Key Suggestions:**
- Use branch names that describe the work, not just the process
- Keep commits focused and well-described
- Reference SAID phases in PRs only when it adds clarity
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