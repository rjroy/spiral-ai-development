# SAID Context Retention Policy and Archiving Procedures

## Overview

This document defines the retention policy and archiving procedures for SAID context data to maintain optimal performance while preserving critical historical information. The policy supports both monolithic and partitioned context formats.

## Retention Policy

### Core Principles

1. **Active Context Priority**: Current and recent phase data must remain easily accessible
2. **Historical Preservation**: All decisions and validations are preserved, but may be archived
3. **Performance Optimization**: Context size must not impair development velocity
4. **Traceability Maintenance**: All archived data must remain traceable and recoverable

### Retention Rules

#### Decisions
- **Active Retention**: Current phase + previous 2 phases
- **Archive Trigger**: Decisions from phases older than 2 phases completed
- **Permanent Preservation**: All decisions are preserved in archived form
- **Searchability**: Archived decisions kept as plain YAML for grep compatibility

#### Validations
- **Active Retention**: Last 20 validation results
- **Archive Trigger**: When active validations exceed 30 entries
- **Permanent Preservation**: All validations preserved in validation-history.yml
- **Searchability**: Large validation histories (>100KB) are archived as plain YAML

#### Constraints
- **Active Retention**: All constraints remain active (they affect current development)
- **Archive Trigger**: Only when constraint is explicitly resolved or superseded
- **Classification**: Separated into technical vs business constraints for better organization

#### Risks and Unknowns
- **Active Retention**: All active risks and unresolved unknowns
- **Archive Trigger**: When risks are mitigated or unknowns are resolved
- **Cleanup**: Resolved items moved to resolved_unknowns section periodically

#### Phase Progression
- **Active Retention**: Current phase artifacts + last 2 phases
- **Archive Trigger**: When implementation artifacts are no longer referenced
- **Searchability**: Old artifacts archived as plain YAML when phase is 3+ phases old

### Size Thresholds

| File Type | Warning | Critical | Action |
|-----------|---------|----------|---------|
| Individual File | 50KB | 100KB | Archive old content |
| Total Context | 500KB | 1MB | Aggressive archiving |
| Validation History | 150KB | 300KB | Archive old validations |
| Archived Directory | 200KB | 500KB | Review archiving policy |

## Archiving Procedures

### Manual Archiving (Command-Guided)

SAID commands will guide users through archiving when files grow large:

1. **Size-Based Warnings**: Commands warn when context files exceed 100KB
2. **Archiving Suggestions**: Commands suggest which content to archive
3. **Simple File Operations**: All archiving done through basic file moves
4. **Plain YAML Storage**: All archives maintained as searchable YAML files

### User-Driven Archiving Procedures

#### 1. Archive Old Decisions

When SAID commands warn about large context files:

```bash
# Create archive directory
mkdir -p context/archive/

# Manual decision archiving (decisions older than 3 phases)
# Cut old decisions from project-context.yml
# Paste into context/archive/old-decisions.yml

# Keep archives as plain YAML for grep searchability
```

#### 2. Archive Large Validation History

When validation history grows large:

```bash
# Create validation archive
# Cut old validations from project-context.yml
# Paste into context/archive/old-validations.yml

# Keep only recent 20-30 validations in main file
```

#### 3. Organize Archives

```bash
# Verify archive organization
find context/archive -name "*.yml" -exec ls -lh {} \;

# Search archived content
grep -r "decision_id" context/archive/

# List archive contents by date
ls -la context/archive/decisions/
```

### File Organization Procedures

#### Domain File Splitting

When monolithic context files exceed 200KB:

```bash
# 1. Backup original
cp context/project-context.yml context/archive/project-context-backup-$(date +%Y%m%d).yml

# 2. Manually split into domain files
# Cut decisions section -> context/decisions.yml
# Cut validations section -> context/validations.yml
# Cut constraints section -> context/constraints.yml

# 3. Create simple manifest
# Create context/project-manifest.yml with file references

# 4. SAID commands automatically detect and use split format
```

#### Archive Structure Migration

When archive directory becomes large (>10MB):

```bash
# 1. Create timestamped archive (preserving searchability)
tar -cf context/archive/historical-context-$(date +%Y%m%d).tar context/archive/

# 2. Clean up individual archives
rm -rf context/archive/decisions/
rm -rf context/archive/validations/
mkdir -p context/archive/decisions context/archive/validations

# 3. Document archive location
echo "Historical archives: historical-context-YYYYMMDD.tar (uncompressed for grep)" >> context/archive/README.md
```

## Monitoring Procedures

### Built-in Command Monitoring

SAID commands provide automatic size monitoring:

```bash
# Size warnings built into SAID commands
/said-context-sync level-3-specifics

# Commands automatically warn when files exceed size thresholds
# No separate monitoring scripts needed
```

### Alert Thresholds

Set up monitoring alerts:

- **Weekly**: Check total context size
- **Monthly**: Review archiving effectiveness
- **Quarterly**: Validate archive integrity

### Performance Monitoring

Monitor through command usage:

- Command execution time: Note if `/said-context-sync` becomes slow
- File size growth: Commands warn when files exceed thresholds
- Context completeness: Verify all important decisions captured

## Recovery Procedures

### Archive Recovery

To recover archived data:

```bash
# 1. List available archives
ls -la context/archive/

# 2. Archives are already plain YAML - no extraction needed
cat context/archive/decisions/level-1-decisions_*.yml

# 3. Search archived content
grep -r "specific_decision" context/archive/

# 4. Merge with active context if needed
# Use /said-context-sync --full to load complete context including archives
```

### Backup and Restore

#### Create Backup

```bash
# Complete context backup (uncompressed for searchability)
tar -cf backups/context-backup-$(date +%Y%m%d-%H%M%S).tar context/

# Verify backup
tar -tf backups/context-backup-*.tar | head
```

#### Restore from Backup

```bash
# Restore complete context
tar -xf backups/context-backup-YYYYMMDD-HHMMSS.tar

# Verify restoration
/said-context-sync --full current-phase
```

## Automation Integration

### CI/CD Integration

Optional size checking in CI/CD:

```yaml
# .github/workflows/context-check.yml
name: Context Size Check
on: [push, pull_request]

jobs:
  context-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check Context Size
        run: |
          if [ -f context/project-context.yml ]; then
            size=$(stat -c%s context/project-context.yml)
            if [ $size -gt 100000 ]; then
              echo "WARNING: Context file is ${size} bytes (>100KB)"
              echo "Consider archiving old content"
            fi
          fi
```

### Git Hooks

Pre-commit hook for size checking:

```bash
#!/bin/sh
# .git/hooks/pre-commit

# Check context size before commit
if [ -f context/project-context.yml ]; then
  size=$(stat -c%s context/project-context.yml)
  if [ $size -gt 200000 ]; then
    echo "ERROR: Context file is ${size} bytes (>200KB)"
    echo "Please archive old content before committing"
    exit 1
  fi
fi
```

## Best Practices

### For SAID Command Development

1. **Always check context size** before major context updates
2. **Use smart loading** by default in commands
3. **Implement size warnings** in commands that add significant context
4. **Test with large contexts** during command development

### For Project Teams

1. **Regular archiving**: Run archiver monthly
2. **Monitor growth**: Check size reports weekly
3. **Plan migrations**: Migrate to partitioned format early
4. **Document decisions**: Keep decision rationale concise but complete

### For Long-Running Projects

1. **Implement retention schedules**: Automate archiving after major milestones
2. **External storage**: Consider cloud storage for very old archives
3. **Context summarization**: Create executive summaries for major phase completions
4. **Tool evolution**: Update tools as context management needs evolve

## Troubleshooting

### Common Issues

#### Context Loading Slow
```bash
# Check file sizes manually
ls -lh context/project-context.yml

# Archive old content manually
mkdir -p context/archive/
# Move old decisions/validations to archive files

# Use --minimal flag for large files
/said-context-sync --minimal current-phase
```

#### Archive Corruption
```bash
# Test archive integrity (YAML files should be valid)
find context/archive -name "*.yml" -exec yaml -f {} \;

# Restore from backup if needed
tar -xf backups/context-backup-latest.tar
```

#### Missing Context Data
```bash
# Check archive for missing data (grep works directly on YAML)
find context/archive -name "*decision*" | xargs grep "decision_id"

# Restore specific archives if needed (already plain YAML)
cp context/archive/decisions/phase-name-decisions_*.yml context/decisions/archived/
```

## Version History

- **v1.0**: Initial retention policy for monolithic format
- **v2.0**: Enhanced policy supporting partitioned format with automated archiving
- **v2.1**: Added CI/CD integration and monitoring procedures
- **v2.2**: Removed compression for grep compatibility and searchability

---

*This document should be reviewed and updated quarterly as SAID methodology evolves and project needs change.*