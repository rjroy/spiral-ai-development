# Smart Context Management for SAID Methodology

## Overview

As SAID projects progress through multiple phases, the `project-context.yml` file grows significantly. The Shelf Judge project demonstrates this with a 1,685-line context file (~170KB) that continues expanding with each decision, validation, and phase progression. This document outlines a command-driven approach to context management that maintains performance and usability while preserving comprehensive context tracking.

## Problem Statement

### Current Issues
1. **Size Growth**: Context files grow unbounded as projects progress
2. **Performance Impact**: Large YAML files slow parsing and command execution
3. **Context Window Consumption**: Full context inclusion exhausts available tokens
4. **Information Density**: Finding specific information becomes increasingly difficult
5. **Memory Pressure**: Commands loading full context may hit memory limits

### Growth Patterns
Each phase typically adds:
- 5-10 new decisions (10-15 lines each)
- 3-5 validations (8-10 lines each)
- 2-4 constraints (5-7 lines each)
- Multiple artifact references
- Unknown resolutions and new unknowns

## Proposed Solution: Smart Command-Driven Context Management

### Core Approach

**Problem**: Adding Python utilities to a template project contradicts the principle of keeping templates simple and focused.

**Solution**: Refactor existing SAID command logic to handle context size intelligently without external scripts.

### File Organization Strategy

**Phase 1: Smart Loading (No File Changes)**
- SAID commands check file size before loading
- Use minimal loading for large files (>100KB)
- Warn users when files approach limits

**Phase 2: Manual Archiving (100KB-200KB)**
```
context/
├── project-context.yml           # Main context file
└── archive/                      # Manual archive when needed
    ├── old-decisions.yml
    └── old-validations.yml
```

**Phase 3: Domain Splitting (200KB+)**
```
context/
├── project-manifest.yml          # Project identity + file index
├── decisions.yml                 # All decisions
├── validations.yml               # All validations  
├── constraints.yml               # All constraints
└── archive/                      # Old content
    └── project-context-v1.yml
```

### Core Files

#### 1. Project Manifest (`project-manifest.yml`)
```yaml
context_manifest:
  version: "2.0.0"  # Indicates partitioned structure
  format: "partitioned"
  
  project_identity:
    name: "Project Name"
    purpose: "Core purpose"
    primary_users: "User description"
    success_metrics: []
    fundamental_constraints: []
  
  partitions:
    decisions:
      active: "decisions/active-decisions.yml"
      archived: "decisions/archived/"
    validations:
      active: "validations/active-validations.yml"
      history: "validations/validation-history.yml"
    constraints: "constraints/"
    phase_progression: "phase-progression.yml"
    risks_unknowns: "risks-and-unknowns.yml"
  
  metadata:
    total_decisions: 49
    total_validations: 46
    total_constraints: 37
    last_updated: "2025-07-07"
    size_bytes: 12450  # Manifest size only
```

#### 2. Active Decisions (`decisions/active-decisions.yml`)
Contains only decisions from current and previous phase:
```yaml
active_decisions:
  phase_scope: ["level-3-specifics", "level-2-structure"]
  decision_count: 12
  
  decisions:
    - decision_id: "D044"
      decision: "Recent decision text"
      rationale: "Why this was chosen"
      # ... other fields
```

#### 3. Phase Progression (`phase-progression.yml`)
Tracks phase movement and artifacts:
```yaml
phase_progression:
  current_phase: "level-3-specifics"
  completed_phases: []
  methodology: "SAID v1.0.6"
  
  phase_artifacts:
    level-3-specifics:
      started: "2025-07-05"
      artifacts: []
      key_decisions: ["D044", "D045", "D046"]
```

### Implementation Strategy

#### Phase 1: Command Logic Refactoring (0.5 hours)
1. Update `said-context-sync` with size checking logic
2. Add loading strategies (default/minimal/full)
3. Add size warnings and archiving suggestions
4. No external scripts or utilities needed

#### Phase 2: User-Driven Archiving (when needed)
1. Users manually create `context/archive/` directory  
2. Move old decisions/validations to archive files
3. Commands continue working with smaller main file
4. All work done through file moves, no scripts

#### Phase 3: Domain File Splitting (when 200KB+)
1. Users manually split large context file into domain files
2. Create simple manifest file with file references
3. Update commands to load multiple files
4. Simple file operations, no migration scripts

### Smart Loading Patterns

#### Default Loading (Minimal)
- Project manifest
- Active decisions (current + previous phase)
- Active validations
- Current risks and unknowns

#### Extended Loading (`--related`)
- Everything in default
- Related historical decisions
- Validation history for active items
- All constraints

#### Full Loading (`--full`)
- Complete context reconstruction
- All partitions loaded
- Used for comprehensive reports

### Archiving Strategy

#### Automatic Archiving Triggers
1. **Phase Completion**: Archive decisions 2+ phases old
2. **Size Threshold**: Archive when partition exceeds 50KB
3. **Time-Based**: Archive items older than 90 days

#### Archive Format
```yaml
archived_decisions:
  archive_date: "2025-07-07"
  phase_range: ["level-0-vision", "level-1-approach"]
  summary: "Initial architecture and approach decisions"
  decision_count: 15
  
  decisions:
    - decision_id: "D001"
      summary: "Two-track evaluation system"
      # Full decision preserved
```

## Implementation Plan

### Completed: Command Logic Refactoring (0.5 hours) ✅
1. ✅ Updated `said-context-sync` with size checking logic
2. ✅ Added loading strategies (default/minimal/full)  
3. ✅ Added size warnings and archiving suggestions
4. ✅ Removed Python script dependencies

### User Actions (when context files grow large):
1. **Manual archiving**: Create archive/ directory and move old content
2. **Domain splitting**: Split single file into decisions.yml, validations.yml, constraints.yml
3. **Simple operations**: All management through basic file operations, no scripts needed

### Future Command Updates (as needed):
1. Update other SAID commands with same size-aware logic
2. Add manifest support for domain-split files
3. Maintain backward compatibility with monolithic format

## Benefits

1. **Simplicity**: No external scripts or utilities to maintain
2. **Template Appropriate**: Keeps the template project focused on methodology
3. **Performance**: Smart loading reduces context window usage
4. **Scalability**: Handles growing context files through simple file organization
5. **User Control**: Users decide when and how to organize their context
6. **Backward Compatible**: Works with existing monolithic context files

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|---------|------------|
| Manual errors during archiving | MEDIUM | Clear instructions, backup recommendations |
| Command compatibility | LOW | Backward compatibility maintained |
| User confusion about when to archive | LOW | Clear size warnings in commands |
| File organization inconsistency | LOW | Simple, documented patterns |

## Success Criteria

1. **Simplicity**: No scripts or utilities added to template project  
2. **Performance**: Commands handle large context files gracefully
3. **Compatibility**: All SAID commands work with existing context files
4. **User Guidance**: Clear warnings when files need archiving
5. **Maintainability**: Simple file organization that users can manage

## Future Enhancements

1. **Additional Commands**: Apply same size-aware logic to other SAID commands
2. **Manifest Support**: Enhanced support for domain-split files
3. **Archive Commands**: Optional commands to help with archiving (if needed)
4. **Context Search**: Built-in search across archive files
5. **Size Monitoring**: Automatic size reporting in commands

## Conclusion

Smart context management addresses the scalability challenges of SAID methodology while keeping the template project simple and focused. By refactoring command logic instead of adding external utilities, we maintain the template's core purpose while solving real performance issues.