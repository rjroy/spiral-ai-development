# Continue TODO Work Prompts

## Basic Continuation
Continue working on the TODO at `[TODO-CONTEXT-PATH]` using the execution log at `[EXECUTION-LOG-PATH]`

## Common Variations

### Resume After Interruption
Resume the interrupted work from where we left off in `[EXECUTION-LOG-PATH]` for the TODO at `[TODO-CONTEXT-PATH]`

### Pick Up From Last Phase  
Pick up from the last phase in the execution log at `[EXECUTION-LOG-PATH]` and continue working on `[TODO-CONTEXT-PATH]`

### Continue With Specific Focus
Continue the TODO at `[TODO-CONTEXT-PATH]` from `[EXECUTION-LOG-PATH]`, focusing on [SPECIFIC-ASPECT]

Examples:
- "focusing on the validation errors we encountered"
- "focusing on the implementation phase"
- "focusing on addressing the discovered constraints"

### Retry With Different Approach
Resume work on `[TODO-CONTEXT-PATH]` from `[EXECUTION-LOG-PATH]` but try a different approach for [PHASE/COMPONENT]

### Continue After Review
Continue the TODO at `[TODO-CONTEXT-PATH]` based on `[EXECUTION-LOG-PATH]`, incorporating this feedback: [FEEDBACK]

## Path Examples
- TODO Context: `context/todo/implement-auth/todo-context.yml`
- Execution Log: `context/todo/implement-auth/execution/execution-log.yml`
- Decomposition TODO: `context/todo/implement-auth/decomposition/jwt-tokens/todo-context.yml`
- Decomposition Log: `context/todo/implement-auth/decomposition/jwt-tokens/execution/execution-log.yml`