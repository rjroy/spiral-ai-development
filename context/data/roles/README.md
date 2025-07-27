# Risk Assessment Roles

This directory contains role definitions used by the `/assess-risks` command to provide domain-specific risk assessment perspectives.

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

## Role Discovery

The `/assess-risks` command automatically discovers all `.md` files in this directory. No registration or configuration is needed - simply add a new role file and it becomes available.

## Using Roles

Roles can be used in two ways:

1. **Automatic detection**: The command analyzes input for keywords matching role expertise
2. **Explicit selection**: Use `--roles=role-name1,role-name2` to specify roles

Example:
```
/assess-risks "Mobile app with TypeScript backend" --roles=mobile-native-client-architect,typescript-service-architect
```