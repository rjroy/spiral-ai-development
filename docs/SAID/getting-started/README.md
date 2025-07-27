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
12. Setup initial context: `/sync-context init`
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
│   ├── project-context.md       # Main context manifest
│   └── ...                      # Task-specific context files
├── .claude/                     # Claude Code integration
|   └── commands/                # SAID Development commands
├── .github/                     # GitHub integration
│   └── workflows/               # Automated validation
├── CLAUDE.md                    # Claude base instructions
└── README.md                    # Project specific overview
```

## Available Commands

### Core Task-Focused Commands
The SAID methodology is implemented through task-focused commands that replace the traditional level structure:

#### Vision & Problem Validation
- `/validate-problem` - Establish clear project purpose and validate the problem space
- `/analyze-risks` - Identify and prioritize technical and project risks

#### Solution Development
- `/analyze-options` - Generate and evaluate technical approach alternatives
- `/sync-decision` - Document chosen approach with rationale
- `/decompose` - Break down work into manageable components at any level:
  - `context/types/project.md` - System-level decomposition
  - `context/types/component.md` - Component-level specifications
  - `context/types/feature.md` - Feature-level implementation
  - `context/types/todo.md` - Granular task decomposition

### Context Management Commands
- `/sync-context` - Maintain context across phases and prevent information loss
- `/plan-next-steps` - Create detailed transition plans with resource estimates

### TODO Workflow Commands
Systematic handling of granular work items:
- `/create-todo` - Create contexts for newly discovered TODOs
- `/work-on-todo` - Execute atomic TODOs with collaboration checkpoints

For detailed guidance, see [TODO Workflow Integration](/docs/SAID/add-ons/todo-workflow-integration.md).

### Git Workflow Guidance
For flexible git workflow suggestions:
- GitHub Flow with descriptive branch naming
- Helpful PR templates and checklists
- Context preservation through meaningful commits
- Domain-aware code review practices

For better examples, see [Git Workflow with SAID](/docs/SAID/philosophy/implementation-guide.md#git-workflow-with-said)

### Common Workflow Patterns

**Vision Validation Workflow**:
```bash
/validate-problem context/project-context.md
/sync-context docs/report/problem-validation.md
/plan-next-steps context/project-context.md
```

**Prototype Workflow**:
```bash
/analyze-risks context/project-context.md
/create-todo docs/reports/risk-assessment.md 'risk 1'
/decompose context/types/todo.md context/todo/pressure-test/todo-context.md
/work-on-todo context/todo/pressure-test/decomposed/phase-1-context.md
```

**Solution Development Workflow**:
```bash
/analyze-options context/project-context.md
/sync-decision context/project-context.md docs/reports/options-analysis.md 'option 1'
/decompose context/types/project.md context/project-context.md
```

**Context Recovery** (when context is lost):
```bash
/sync-context context/project-context.md
/plan-next-steps context/project-context.md
```

**Context Priming Pattern** (for session continuity):
```bash
# Before executing SAID commands, provide brief context:
> Be aware, I've [completed work]. [Current state]. I'm about to [intended action].
AI: [Acknowledgment and readiness confirmation]
> /decompose context/types/project.md context/approach-decision-context.md
```

## Next Steps After **First Steps**

1. **Start with Problem Validation**: Run `/validate-problem` to establish clear project purpose
2. **Test Your Understanding**: Use `/pressure-test` to challenge assumptions
3. **Identify Risks Early**: Run `/analyze-risks` to surface technical and project risks
4. **Explore Solutions**: Use `/analyze-options` to evaluate technical approaches
5. **Document Decisions**: Run `/sync-decision` to capture chosen approach with rationale
6. **Decompose Work**: Use `/decompose` with appropriate context type to break down the work
7. **Maintain Context**: Run `/sync-context` after each significant workflow
8. **Plan Transitions**: Use `/plan-next-steps` before moving to next phase

**Pro Tip**: When under pressure, the framework provides fast-track protocols - combine levels, use proven patterns, but never abandon the context preservation that makes recovery possible.
