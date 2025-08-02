# Expert System for SAID Commands

This directory contains expert definitions that can be loaded by SAID commands to provide specialized domain knowledge.

## Overview

Experts are modular knowledge domains that augment the base roles in SAID commands with specialized expertise. They enable commands like `/work-on-todo` to adapt their behavior based on the technical requirements of a task.

## Usage

### Explicit Loading
```bash
/work-on-todo context/todo/redesign-ui/todo-context.md --expert=ux
/work-on-todo context/todo/optimize-crypto/todo-context.md --expert=crypto
```

### Auto-Detection
Commands may automatically detect when specialized expertise is needed based on:
- Keywords in the TODO context
- File types being worked with
- Technology stack indicators
- Explicit requirements in success criteria

## Available Experts

| Expert | Domain | Key Areas |
|--------|--------|-----------|
| `ux` | UX Design | Accessibility, information architecture, design systems, WCAG compliance |
| `rust` | Rust Development | Memory safety, performance, systems programming, async patterns |
| `crypto` | Cryptography | Security protocols, key management, compliance, threat modeling |
| `typescript` | TypeScript | Type system, build tools, frameworks, testing strategies |

## Expert File Structure

Each expert file should include:

### 1. Domain Expertise
A brief introduction describing the expert's background and areas of expertise.

### 2. Specialized Knowledge
Core principles, decision criteria, and best practices specific to the domain.

### 3. Tools & Frameworks
Commonly used tools, libraries, and frameworks in the domain.

### 4. Common Pitfalls
Mistakes to avoid and anti-patterns specific to the domain.

### 5. Guidelines & Standards
Industry standards, compliance requirements, and best practices.

## Creating New Experts

To add a new expert:

1. Create a new file: `.agent/experts/{domain}.md`
2. Follow the structure used in existing expert files
3. Focus on practical, actionable expertise
4. Include decision criteria for common scenarios
5. Add domain-specific best practices and pitfalls

### Template Structure
```markdown
# [Domain] Expert

## Domain Expertise
[Background and areas of expertise]

## Specialized Knowledge
### [Domain] Principles
[Core principles and concepts]

### Decision Criteria
[How to make decisions in this domain]

### Best Practices
[Recommended approaches and patterns]

### Tools & Ecosystem
[Common tools and frameworks]

### Common Pitfalls to Avoid
[Anti-patterns and mistakes]

### Compliance & Standards
[Relevant standards and requirements]
```

## Integration with Commands

Currently integrated with:
- `/work-on-todo` - Loads expertise for task execution

Future commands may also leverage the expert system for specialized analysis, decision-making, and implementation guidance.

## Philosophy

The expert system follows these principles:

1. **Augmentation, not replacement**: Experts enhance base roles, not replace them
2. **Practical focus**: Emphasize actionable knowledge over theory
3. **Decision support**: Help users make informed choices
4. **Domain specificity**: Deep knowledge in focused areas
5. **Composability**: Experts combine with base roles seamlessly

## Maintenance

Expert files should be updated when:
- New best practices emerge in the domain
- Tools and frameworks evolve
- Standards and compliance requirements change
- Common pitfalls are discovered
- User feedback suggests improvements

Keep experts focused and practical - they should help execute tasks, not provide academic knowledge.