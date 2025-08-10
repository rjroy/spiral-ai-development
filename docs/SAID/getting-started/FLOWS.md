## **1. Review / Analyze / Decide**

```
/analyze <focus> <input> <roles>
/sync-context <analyze-output>   OR    /sync-decision <analyze-output> <option ID>
```

**Purpose**
Continuously sharpen understanding and resolve uncertainties at the *current level* of the spiral.

**When to run**

* At project start (PRD → first technical approach)
* After major discoveries, requirements changes, or external events
* Before committing to the next decomposition step (forces sanity check)

**Tips to make it stick**

* **Focus** should be explicit: `problems`, `risks`, `solutions`, `opportunities`.
* Always feed *current context* as `<input>` (e.g., `docs/design/HIGH-LEVEL-DESIGN.md`) to avoid drift.
* **Roles** ensure multi-perspective thinking (`architect`, `developer`, `user`, `ops`). Even one unusual role (e.g., `security-auditor`) can surface hidden risks.
* Use `/sync-decision` sparingly — only when you’re locking a path forward. Otherwise, `/sync-context` keeps options open.

**Done right, this loop is your “decision hygiene.”** Skipping it too often risks committing to bad decomposition.

---

## **2. Decompose**

```
/decompose <layer> <input>
/decompose <next-layer> <output-1>
...
/decompose <next-layer> <output-n>
```

**Purpose**
Turn big goals into progressively smaller, self-contained pieces until each can be worked on independently or one-shot generated.

**When to run**

* Right after locking a decision in the previous loop.
* Whenever the current layer has more than \~3–5 “unknowns” or dependencies.

**Tips to make it stick**

* Define **layer boundaries** up front:

  * `project` → the whole deliverable
  * `component` → major subsystems / services
  * `feature` → specific user-facing or functional pieces
  * `todo` → atomic work items
* Always feed each `/decompose` the *output* of the last decomposition. This keeps spirals clean instead of rehashing the whole project.
* Watch for *over-decomposition*. If you hit a level where each item can be implemented in a single work session without guessing, stop.

**Guideline**
If the **One-Shot Readiness Check** (clear APIs, dependencies resolved, naming stable) passes, move to “Work.”

---

## **3. Work**

```
/work-on-todo <decomposed-output-layer-N>
/sync-context <decomposed-output-layer-N>
```

**Purpose**
Generate and refine real artifacts — code, docs, configs — that fulfill the design at the current spiral depth.

**When to run**

* Once a todo is fully understood and one-shot ready.
* Often in parallel if multiple contributors are using the same synced context.

**Tips to make it stick**

* Use `/work-on-todo` with **the most specific context possible** (ideally just the todo item + relevant design doc).
* Immediately `/sync-context` after a work session — stale todos are a prime source of drift.
* If you hit a blocker, feed the blocker back into **Review/Analyze/Decide** loop before continuing.

---

## **Support Commands**

* **`/create-todo`**

  * Best right after decomposition, to translate abstract “feature” descriptions into clearly worded, action-ready tasks.
  * Avoid mixing multiple layers in one todo list.
* **`/plan-next-steps`**

  * Run at natural pause points to recap progress, recommend next focus areas, and ensure you’re not missing obvious dependencies.
  * Works as a bridge between spirals — e.g., wrapping one feature’s work and planning its integration into the broader project.
