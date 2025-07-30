# Context Integration Patterns

## Content Classification and Analysis

### Automatic Classification Indicators

#### Decision Indicators
Words/phrases that signal decisions were made:
- "decided", "chose", "selected", "approach taken"
- "rationale", "because", "reason"
- "went with", "opted for", "strategy"

#### Lesson Indicators  
Words/phrases that signal learnings:
- "learned", "discovered", "found that"
- "mistake", "issue", "problem"
- "insight", "research found", "investigation revealed"
- "turned out", "actually", "realized"

#### Architecture Indicators
Words/phrases that signal structural information:
- "component", "interface", "structure"
- "constraint", "requirement", "specification"
- "design", "pattern", "integration"
- "system", "service", "module"

#### Question Indicators
Words/phrases that signal open questions:
- "unclear", "need to research", "open question"
- "unresolved", "pending decision", "requires investigation"
- "need to determine", "TBD", "to be decided"
- "unknown", "depends on", "waiting for"

### Content Extraction Strategy

#### Smart Summarization
- Extract key points, not entire sections
- Focus on decisions and their rationale
- Capture context that explains why something matters
- Preserve technical details that affect future decisions

#### Source Traceability
- Always include reference to original file
- Note section/context where information was found
- Include timestamp if available
- Maintain chain of reasoning across files

## Target File Mapping

### context/project-context.md
**Contains:** Vision, architecture, high-level constraints
**From source:** Architecture indicators, requirements, system design
**Integration:** Add to relevant sections, update architecture diagrams

### context/project/decisions-made.md  
**Contains:** Key decisions with rationale and impact
**From source:** Decision indicators with reasoning
**Integration:** Chronological with source references

### context/project/lessons-learned.md
**Contains:** Research insights, mistakes, discoveries  
**From source:** Lesson indicators, investigation results
**Integration:** Categorized by domain/topic area

### context/project/open-questions.md
**Contains:** Unresolved questions requiring investigation
**From source:** Question indicators, dependencies, unknowns
**Integration:** Prioritized by impact and urgency

## Integration Rules

### Preserve Existing Content
- Never overwrite without explicit conflicts
- Add new information to appropriate sections
- Maintain chronological order for decisions
- Keep cross-references intact

### Handle Conflicts
- Flag when new info contradicts existing
- Present both versions with sources
- Ask user to resolve only when necessary
- Default to more recent information when dates available

### Maintain Format Consistency
- Use standard headers and structure
- Include source references in consistent format
- Apply same categorization across files
- Keep summaries concise but complete