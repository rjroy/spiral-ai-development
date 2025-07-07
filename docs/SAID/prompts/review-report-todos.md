# Review Report TODOs

Review the report at `<REPORT-PATH>` and verify which TODO items can be marked as complete.

## Verification Process

For each TODO item (- [ ]):
1. **Identify the specific deliverable** - What exact artifact or outcome was promised?
2. **Locate concrete evidence** - Find the actual file, code, or documentation
3. **Verify completeness** - Confirm the deliverable fully meets the stated requirement
4. **Only mark done if certain** - When you have direct evidence of completion

## Verification Requirements

**DO NOT mark a TODO as done (- [x]) unless you can:**
- Point to the specific file/artifact that fulfills it
- Confirm the implementation matches the requirement
- Verify any success criteria mentioned are met

**Examples of insufficient evidence:**
- "This looks like it should be done"
- "The framework probably handles this"
- "This is a common feature that's likely implemented"
- "Based on other files, this seems complete"

**Examples of sufficient evidence:**
- "Found the implementation in `src/auth/jwt.ts` lines 45-78"
- "Verified the test passes in `tests/auth.test.ts`"
- "Documentation exists in `docs/API.md` section 3.2"
- "Configuration is properly set in `config/auth.yml`"

## Output Format

For each TODO reviewed, provide:
```
TODO: [Description]
Status: [ ] Not Done | [x] Done
Evidence: [Specific file:line or explanation why not done]
```

Take your time. Be conservative. It's better to leave items unchecked than to incorrectly mark them complete.