# Stakeholder Roles

This directory contains role definitions used by SAID commands (like `/analyze` ) to provide domain-specific perspectives and expertise.

## Adding New Roles

To add a new role, create a markdown file in this directory following the naming convention: `{role-name}.md`

### Role File Structure

Each role file must contain two main sections:

```markdown
# Role Title

## Who They Are

**Identity**: Brief description of the role's professional identity and experience level

**Expertise**:
- List of specific technical or domain expertise areas
- Skills and knowledge domains
- Areas of specialization

**Perspective**: Description of how this role approaches problems and what they prioritize

## What They Look For

### [Risk Category 1]
- Specific risks this role would identify
- Patterns they watch for
- Domain-specific concerns

### [Risk Category 2]
- Additional risk patterns
- Industry-specific issues
- Technology-specific concerns

### Early Warning Indicators
- Metrics or signals this role monitors
- Specific warning signs they recognize
- Domain-specific indicators of emerging issues
```

## Available Roles

- **business-analyst** - Business perspective, market analysis, stakeholder needs
- **client-architect** - Web, mobile, desktop application architecture
- **mobile-native-client-architect** - Native mobile development expertise
- **operations-engineer** - Infrastructure, deployment, monitoring
- **service-architect** - Backend services, APIs, distributed systems
- **solution-architect** - Alternative implementations (MCPs, spreadsheets, automation, prompts)

## Role Discovery

SAID commands automatically discover all `.md` files in this directory. No registration or configuration is needed - simply add a new role file and it becomes available.

## Using Roles

Roles can be used in two ways:

1. **Automatic detection**: Commands analyze input for keywords matching role expertise
2. **Explicit selection**: Use `--roles=role-name1,role-name2` to specify roles

Example:
```
/analyze "Mobile app with Node.js backend" --roles=mobile-native-client-architect,service-architect
```