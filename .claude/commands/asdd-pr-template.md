## Usage

```
/asdd-pr-template <level> <domain-complexity> [template-type]
```

## Command Guidelines

### PR Template Generator

**Focus**: Generate pull request templates aligned with ASDD validation requirements
**Success criteria**: PR template that enforces proper validation gates for specific level and domain
**Output**: Customized PR template with appropriate validation checklists and domain-specific requirements

### Template Types

**1. Level Completion Template**
- For standard level completion and progression
- Includes full ASDD validation checklist
- Domain-calibrated review requirements
- Context preservation verification

**2. Spiral Navigation Template**
- For backward navigation and level revision
- Emphasizes revision rationale and impact assessment
- Cross-level dependency analysis
- Updated context reconciliation

**3. Emergency Template**
- For high-pressure situations requiring rapid delivery
- Minimal validation requirements
- Cleanup tracking requirements
- Risk acceptance documentation

**4. Context Sync Template**
- For dedicated context synchronization
- Context integrity verification
- Conflict resolution documentation
- Cross-phase context alignment

### Domain-Specific Validation

**Simple Domain Requirements**:
- Basic integration testing
- Code style compliance
- Standard review by team members
- Automated validation sufficient

**Complex Domain Requirements**:
- Architectural review by domain expert
- Integration complexity assessment
- Performance impact evaluation
- Domain-specific validation criteria

**Extreme Domain Requirements**:
- Multiple expert reviews required
- Compliance and regulatory checks
- Security impact assessment
- Extensive documentation requirements

### Level-Specific Templates

**Level 0: Vision Clarity Template**:
```markdown
# Level 0: Vision Clarity Completion

## Vision Validation
- [ ] Core purpose stated in one clear sentence
- [ ] Primary users identified (max 3 types)
- [ ] Success metrics are measurable and meaningful
- [ ] Critical constraints documented
- [ ] Domain complexity assessed

## Context Foundation
- [ ] Initial context manifest created
- [ ] Semantic checksum established
- [ ] Explicit unknowns documented with defer strategy
- [ ] Vision conflicts resolved

## Stakeholder Alignment
- [ ] Problem analysis validated by stakeholders
- [ ] User types confirmed by domain experts
- [ ] Success metrics agreed upon by product team
- [ ] Constraints validated by technical team

## Transition Readiness
- [ ] Level 1 prerequisites identified
- [ ] Approach exploration scope defined
- [ ] Team roles and responsibilities clarified
- [ ] Next level branch prepared
```

**Level 1: Approach Viability Template**:
```markdown
# Level 1: Approach Viability Completion

## Technical Approach Validation
- [ ] Core technical approach proven viable
- [ ] Key technologies identified and validated
- [ ] Integration points mapped and assessed
- [ ] Architectural risks evaluated and mitigated

## Technology Stack Verification
- [ ] Technology choices align with constraints
- [ ] Team expertise assessed for chosen stack
- [ ] Long-term maintenance implications considered
- [ ] Alternative approaches documented with rationale

## Risk Assessment
- [ ] Technical risks identified and mitigation planned
- [ ] Integration complexity evaluated
- [ ] Performance feasibility validated
- [ ] Security implications assessed

## Context Updates
- [ ] Approach decisions added to context manifest
- [ ] Technology rationale documented
- [ ] Risk assessments recorded
- [ ] Dependency mapping updated

## Domain Calibration
- [ ] **Simple Domain**: Basic technical review completed
- [ ] **Complex Domain**: Architecture review by domain expert
- [ ] **Extreme Domain**: Multiple expert validation required
```

### Dynamic Template Generation

**Template Customization Logic**:
```yaml
template_rules:
  level_requirements:
    level-0:
      - vision_clarity_validation
      - stakeholder_alignment
      - context_foundation
    level-1:
      - technical_approach_validation
      - technology_stack_verification
      - risk_assessment
    level-2:
      - system_boundaries_definition
      - component_interfaces_design
      - integration_architecture
    level-3:
      - implementation_specifications
      - detailed_design_completion
      - development_readiness
    level-4:
      - working_implementation
      - production_readiness
      - deployment_validation

  domain_requirements:
    simple:
      - basic_integration_testing
      - code_style_compliance
      - team_member_review
    complex:
      - domain_expert_review
      - architectural_assessment
      - performance_evaluation
    extreme:
      - multiple_expert_reviews
      - compliance_verification
      - security_assessment
      - regulatory_approval

  template_types:
    completion:
      - full_validation_checklist
      - progression_readiness
      - next_level_preparation
    revision:
      - revision_rationale
      - impact_assessment
      - dependency_analysis
    emergency:
      - minimal_validation
      - cleanup_tracking
      - risk_acceptance
    context-sync:
      - context_integrity
      - conflict_resolution
      - cross_phase_alignment
```

### Generated Template Examples

**Level 2 Complex Domain Completion Template**:
```markdown
# Level 2: System Structure Completion (Complex Domain)

## System Boundaries Definition
- [ ] Clear component boundaries established
- [ ] Interface contracts defined and documented
- [ ] Data flow between components mapped
- [ ] Service boundaries aligned with business domains

## Component Design Validation
- [ ] Each component has single clear responsibility
- [ ] Dependencies are explicit and minimal
- [ ] Interfaces support bounded replaceability
- [ ] Integration patterns follow established standards

## Complex Domain Requirements
- [ ] Domain expert architectural review completed
- [ ] Integration complexity assessed by senior engineer
- [ ] Performance implications evaluated
- [ ] Security boundaries validated by security team

## Context Preservation
- [ ] System design decisions documented with rationale
- [ ] Alternative approaches considered and recorded
- [ ] Technology choices updated in context manifest
- [ ] Constraint impacts assessed and documented

## Bounded Replaceability Assessment
- [ ] Component replacement cost documented
- [ ] Interface stability evaluated
- [ ] Behavioral contracts defined through tests
- [ ] Integration testing strategy established

## Transition to Level 3
- [ ] Implementation specifications can be derived
- [ ] Development team understands architecture
- [ ] Technical dependencies identified and planned
- [ ] Level 3 branch prepared with architecture foundation
```

**Emergency Template Example**:
```markdown
# Emergency Implementation (Bypass Normal Validation)

## Emergency Justification
- [ ] Critical business impact documented
- [ ] Normal validation timeline risk assessed
- [ ] Stakeholder approval for emergency process obtained
- [ ] Cleanup plan established with timeline

## Minimal Validation Requirements
- [ ] Basic functionality verified
- [ ] Security vulnerabilities checked (cannot be bypassed)
- [ ] Integration points tested
- [ ] Rollback plan documented

## Risk Acceptance
- [ ] Technical risks explicitly accepted by {stakeholder}
- [ ] Documentation debt acknowledged
- [ ] Testing debt recorded with remediation plan
- [ ] Performance impact assessed and accepted

## Cleanup Tracking
- [ ] Post-emergency documentation task created
- [ ] Additional testing requirements identified
- [ ] Code review debt scheduled
- [ ] Process improvement retrospective planned

## Emergency-Specific Validation
- [ ] Solution addresses critical issue
- [ ] No alternative rapid solutions available
- [ ] Risk/benefit analysis clearly justifies emergency process
- [ ] Team understands emergency nature and cleanup requirements
```

### PR Template Customization

**Dynamic Content Generation**:
- Level-specific validation checklists
- Domain-appropriate review requirements
- Context preservation requirements
- Transition readiness checks
- Risk assessment criteria
- Cleanup tracking (for emergency templates)

**Template Variables**:
- `{level}`: ASDD level (0-4)
- `{domain-complexity}`: Simple/Complex/Extreme
- `{template-type}`: completion/revision/emergency/context-sync
- `{previous-level}`: Previous level for progression validation
- `{next-level}`: Next level for preparation requirements

## Command

You are the PR Template Generator for ASDD v1.0.3.

Your mission: Generate customized pull request templates that enforce appropriate validation gates based on ASDD level and domain complexity.

**Process:**
1. **LEVEL ANALYSIS**: Determine specific validation requirements for target level
2. **DOMAIN ASSESSMENT**: Apply domain-specific validation criteria
3. **TEMPLATE SELECTION**: Choose appropriate template type for situation
4. **CUSTOMIZATION**: Generate template with relevant checklists and requirements
5. **VALIDATION LOGIC**: Include appropriate validation gates and review assignments
6. **CONTEXT INTEGRATION**: Ensure context preservation requirements included
7. **TRANSITION PLANNING**: Add next-level preparation requirements

**Template Types:**
- **completion**: Standard level completion with full validation
- **revision**: Spiral navigation with revision rationale
- **emergency**: Rapid delivery with cleanup tracking
- **context-sync**: Context synchronization and conflict resolution

**Domain Complexity Levels:**
- **simple**: Basic validation, team review sufficient
- **complex**: Domain expert review required, architectural assessment
- **extreme**: Multiple expert reviews, compliance verification

**Outputs:**
- Customized PR template with appropriate validation checklists
- Domain-specific review requirements
- Context preservation verification
- Transition readiness checks
- Level-appropriate validation gates

Generate PR template for {level} completion with {domain-complexity} domain requirements using {template-type} template.