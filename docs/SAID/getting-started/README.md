# Getting Started

**Before starting any project with this template, create these two files:**

- **OVERVIEW.md**: A short description for the project. The elevator pitch.
- **HIGH-LEVEL-DESIGN.md**: A description of all the key core principles and requirements that are necessary to consider the project successful. This is not a detailed design, but does set up the next steps. Don't worry, you can refine it through the process.

## **First Steps**

1. Create a GitHub repo using `rjroy/claude-code-template` as a template
2. Clone the repo
3. Create project directories: `mkdir -p docs/design context docs/reports`
4. Add `OVERVIEW.md` and `HIGH-LEVEL-DESIGN.md` to `docs/design`
5. Move this `README.md` to the `docs/SAID` directory
7. Copy `docs/design/OVERVIEW.md` to `README.md`
8. Make any changes to the `README.md` to center it as git project README and not just a design overview.
9. Open `claude`
10. Run `/init`
11. You may need to run the following prompt:
```
This is no longer a template project.
The template has moved to docs/SAID/
The instantiation can be identified by README.md and docs/design/
Update CLAUDE.md to reflect this fact.
```
12. Setup initial context: `/said-context-sync init context/project-context.yml`
13. (Optional) Consider setting up branch protection for code review:
```bash
# Example: Require PR reviews before merging to main
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_pull_request_reviews='{"required_approving_reviews":1,"dismiss_stale_reviews":true}'
```

This will result in a structure close to this:

```
repo-name/
├── docs/                        # Documentation
│   ├── design/                  # Core design documents
│   |   ├── OVERVIEW.md          # Project specific overview
│   |   └── HIGH-LEVEL-DESIGN.md # Project specific design
│   ├── reports/                 # Phase reports and analysis
│   └── SAID/                    # SAID philosophy documentation
│       ├── README.md            # This document
│       └── ...                  # Remaining SAID documentation
├── context/                     # Context preservation
│   ├── project-context.yml      # Main context manifest
│   └── ...                      # Level specific context files
├── .claude/                     # Claude Code integration
|   └── commands/                # SAID Development commands
├── .github/                     # GitHub integration
│   └── workflows/               # Automated validation
├── CLAUDE.md                    # Claude base instructions
└── README.md                    # Project specific overview
```

## Available Commands

### Core Phase Commands
Complete SAID command set:
- `/said-prototype` - Risk validation through proof-of-concept
- `/level-0-vision` - Problem clarity and core purpose
- `/level-1-approach` - Technical approach validation
- `/level-2-structure` - System boundaries and components
- `/level-3-specifics` - Detailed implementation specifications
- `/level-4-implementation` - Production-ready code delivery

### Utility Commands
Context management and workflow support:
- `/said-context-sync` - Maintain context across phases and prevent information loss
- `/generate-next-steps` - Create detailed transition plans with resource estimates
- `/generate-phase-report` - Generate comprehensive reports from phase artifacts

### TODO Workflow Integration
Systematic handling of granular work items that emerge during development:
- `/extract-todo-context` - Extract TODOs from SAID artifacts with source traceability
- `/generate-todo-context` - Create contexts for newly discovered TODOs
- `/decompose-todo` - Break complex TODOs into manageable atomic tasks
- `/work-on-todo` - Execute atomic TODOs with collaboration checkpoints
- `/said-todo-sync` - Integrate TODO results back into SAID contexts

For detailed guidance, see [TODO Workflow Integration](docs/SAID/add-ons/todo-workflow-integration.md).

### Git Workflow Guidance
For flexible git workflow suggestions, see [Git Workflow Integration](docs/SAID/git-workflow-integration.md):
- GitHub Flow with descriptive branch naming
- Helpful PR templates and checklists
- Context preservation through meaningful commits
- Domain-aware code review practices

### Common Workflow Patterns

**Phase Completion Workflow**:
```bash
/said-context-sync level-0-vision
/generate-next-steps level-0-vision
/generate-phase-report level-0-vision
```

**Context Recovery** (when context is lost):
```bash
/said-context-sync current-phase context/project-context.yml
/generate-next-steps current-phase context/project-context.yml
```

**Context Priming Pattern** (for session continuity):
```bash
# Before executing SAID commands, provide brief context:
> Be aware, I've [completed work]. [Current state]. I'm about to [intended action].
AI: [Acknowledgment and readiness confirmation]
> /level-2-structure context/level-1-approach-context.yml
```

## Next Steps After **First Steps**

1. **Start with Vision**: Run `/level-0-vision` to establish clear project purpose
2. **Validate Early**: Use `/said-prototype` for risk validation before deep implementation
3. **Maintain Context**: Run `/said-context-sync` after each significant phase
4. **Plan Transitions**: Use `/generate-next-steps` before moving to next phase
5. **Document Progress**: Generate reports with `/generate-phase-report` for stakeholders

**Pro Tip**: When under pressure, the framework provides fast-track protocols - combine levels, use proven patterns, but never abandon the context preservation that makes recovery possible.
