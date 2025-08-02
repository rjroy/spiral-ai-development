# Command Design Principles

Commands should behave like high-performing interns, not bureaucratic processes.

These principles apply to both human-AI collaboration and AI consistency. The primary reader is AI - these files must balance deterministic behavior with contextual adaptability.

## Core Principles

### 1. Adaptive Checkpoints
**Instead of:** "Found the problem." → "I've changed the 3 files to resolve the issue."
**Do this:** "Found 3 files which contain the problem. I'll analyze them and generate a report to discuss a solution."

### 2. Natural Communication
**Instead of:** Rigid templates with sections and subsections
**Do this:** "I see three approaches: quick patch (fast but messy), full refactor (clean but slow), or middle ground. Thoughts?"

### 3. Bounded Initiative
**Instead of:** Asking permission for every import or variable name
**Do this:** Make obvious decisions, show the result: "Added standard error handling - here's what it looks like."

### 4. Transparent Progress
**Instead of:** "Working..." → "Done."
**Do this:** "Using the auth pattern from last week. Hit a snag with error types - adapted them like this."

### 5. Context-Aware Depth
- Simple tasks (renaming variables) → Just do it
- Medium tasks (new feature) → Propose approach, proceed unless stopped
- Complex tasks (architecture) → Always discuss options first

### 6. Bundle Questions
**Instead of:** Four separate checkpoints for four unknowns
**Do this:** "Need clarification on: 1) constraints A & B, 2) success criteria, 3) error handling. I can assume 1 & 3 if you want to focus on criteria."

### 7. Command Clarity vs Rigidity
The command should have enough detail so there are few questions to what the steps needed to complete the task. But not so much that there is no room for innovation. For AI this is the balance of determinism vs token cost.

## Basic Structure

A command should have the following sections:
- **Usage**: List the parameters of the command. This works as combination instruction and header declaration.
- **Required Patterns**: List the common pattern files that should be loaded. These allowed for share information between commands.
- **Purpose**: Brief why this command exists.
- **Main Role**: Defines the main role of the AI for the command. Some commands use multiple roles.
- **Process**: Step-by-step guide to complete the command
- **Key Principles**: A few rules that need to allows be considered while following the command.
- The last section is for validation and varies depending on the needs of the command. Report generators have a **Output Summary** section to describe what to say after the report. Commands which need some back-and-forth with the user have an **Example Flow** to demonstrate collaboration. There are additional variations, but they are all around the theme of consistency in output.