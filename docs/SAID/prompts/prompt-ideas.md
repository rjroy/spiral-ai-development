# Prompt Ideas

## Context & Documentation Maintenance

1. Context Archaeology - When context files are corrupted or missing
    > "Reconstruct the project context from existing artifacts in [DIRECTORY]. Look for decision traces in git history, code comments, and documentation to rebuild the context manifest."

2. Command Calibration - When existing commands don't fit the current situation
    > "Review the [COMMAND-NAME] command and suggest modifications for [SPECIFIC-SITUATION]. Preserve the core structure but adapt validation criteria and outputs."

3. Documentation Audit - When documentation may be stale
    > "Audit the documentation in [DOC-PATH] against the current codebase. Identify outdated information, missing sections, and inconsistencies with implementation."

## Philosophy Application

4. Domain Complexity Assessment - When unsure about AI/human boundaries
    > "Assess the domain complexity of [SYSTEM/COMPONENT] and recommend appropriate AI collaboration boundaries. Consider regulatory requirements, technical constraints, and expertise needed."

5. Bounded Replaceability Analysis - When evaluating component design
    > "Analyze [COMPONENT] for bounded replaceability. Document interface contracts, hidden behaviors, replacement cost, and what someone would need to rebuild it compatibly."

6. Pressure Protocol Selection - When under timeline pressure
    > "Given [TIMELINE-CONSTRAINTS] and [QUALITY-REQUIREMENTS], recommend which pressure adaptation protocol to use and what can be safely deferred."

## Quality Assurance & Validation

7. Assumption Archaeology - When questioning inherited assumptions
    > "Identify and validate the core assumptions underlying [COMPONENT/DECISION]. Find evidence for each assumption or flag it for verification."

8. Integration Boundary Testing - When components interact unexpectedly
    > "Test the integration boundaries between [COMPONENT-A] and [COMPONENT-B]. Identify coupling points, failure modes, and interface contract violations."

9. Context Integrity Check - When context may have drifted
    > "Verify context integrity by checking if current implementation matches the semantic checksum in [CONTEXT-FILE]. Flag discrepancies and suggest corrections."

## Collaboration Edge Cases

10. Confidence Calibration - When AI confidence doesn't match domain complexity
    > "Calibrate confidence levels for [DECISIONS/RECOMMENDATIONS] against domain complexity. Identify where AI confidence exceeds appropriate boundaries."

11. Decision Authority Clarification - When ownership is ambiguous
    > "Clarify decision authority for [SPECIFIC-DECISION] based on domain complexity and collaboration boundaries. Recommend who should own this decision and why."

12. Collaboration Drift Recovery - When collaboration patterns break down
    > "Diagnose collaboration drift in [SITUATION] and recommend boundary reset. Identify what caused the drift and how to prevent recurrence."

## Rapid Assessment

13. Quick Architecture Review - When you need fast architectural insights
    > "Provide a rapid architecture assessment of [SYSTEM] focusing on major structural issues, coupling problems, and replaceability concerns. Prioritize findings by impact."

14. Technical Debt Triage - When debt is accumulating
    > "Triage technical debt in [CODEBASE/COMPONENT]. Categorize by impact, effort to fix, and relationship to bounded replaceability principles."

15. Requirements Reality Check - When requirements seem problematic
    > "Reality-check [REQUIREMENTS] against [CONSTRAINTS]. Identify conflicts, missing information, and implementation feasibility issues."

## Legacy & Integration

16. Legacy Integration Strategy - When working with existing systems
    > "Develop integration strategy for [LEGACY-SYSTEM] with [NEW-COMPONENT]. Focus on interface boundaries, data migration, and failure isolation."

17. Code Archaeology - When understanding undocumented code
    > "Perform code archaeology on [CODEBASE/COMPONENT]. Extract implicit behaviors, hidden dependencies, and business rules that should be documented."

## Communication & Explanation

18. Decision Explanation - When you need to explain complex decisions
    > "Explain [DECISION] to [AUDIENCE] focusing on rationale, alternatives considered, and trade-offs. Include risks and mitigation strategies."

19. Stakeholder Translation - When technical details need business context
    > "Translate [TECHNICAL-FINDINGS] for [BUSINESS-STAKEHOLDERS]. Focus on business impact, risks, and required decisions."

## Troubleshooting & Recovery

20. Process Recovery - When SAID workflow breaks down
    > "Diagnose why [SAID-PROCESS] broke down and recommend recovery steps. Identify what can be salvaged and what needs restart."

21. Context Reconstruction - When starting mid-project
    > "Reconstruct project context from [EXISTING-ARTIFACTS]. Build understanding of decisions, constraints, and current state without prior context."
