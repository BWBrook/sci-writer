# Neon on the first draft of the skill

Neon (Google `gemini-4-neon-high`, through `agy` 1.5.12), 19 November 2026. Same request as to Astra. Reproduced as returned.

---

Your core design is right: separating analyst from writer and enforcing plan, one-page paper, and outline matters more than sentence rules. Your suspicion about stage 5 is also right: the expansion audit will be filled in mechanically. A model easily justifies every clause it just wrote as "needed by reader 1 to believe."

### 1. Quietly ignored
- **The expansion audit.** Models rarely delete fresh prose during self-audit; they write post-hoc justifications instead.
- **Venue study (stage 2).** Without five real papers in the pack, the writer will invent generic journal conventions.
- **Word limits and subjective tests.** Models cannot count words reliably during generation and default to formal academic prose as context fills, ignoring "read aloud to a colleague."
- **Fine sentence rules in `prose.md`.** With 30+ rules in context alongside the pack and outline, local rules (topic/stress position, subject-verb distance, `"this"` plus noun) fail during drafting unless checked in a separate editing pass.

### 2. Obeyed too literally
- **"Point first, condition second, number last" and "one or two numbers per paragraph."** Produces monotonous three-part paragraphs and vague Results ("markedly higher") that force readers into tables for basic effect sizes.
- **Overused-devices list.** Despite "none is banned," models treat listed patterns as bans. Avoiding "denial before the claim" or "wrong reading" removes real hypothesis-testing contrast and makes prose flat.
- **Non-empty cut list.** Models put trivial claims there to satisfy the rule while leaving real clutter in the text.
- **Section abstracts (stage 4).** Up to 1,500 words of draft prose that stage 5 expands rather than trims, restoring excess length.

### 3. Missing at writing time
- **One before/after example.** A 150-word cluttered agent paragraph rewritten in Barry's target style sets tone, caveat placement, and number density better than twenty abstract rules.
- **Section-specific rules.** Methods cannot follow "point first, 1–2 numbers," and Results needs rules for explaining figures without describing every panel.
- **Citations during drafting.** Stage 7 delays references until the end, which breaks Introduction and Discussion because citations structure those arguments.
- **Per-paragraph word targets** in the outline.

### 4. Contradictions and unmade choices
- **Unused role.** `readers.md` defines "Co-author from another lab (before any prose)," but `SKILL.md` never calls it.
- **Limitations conflict.** Stage 6 sends caution requests to the limitations passage, while `prose.md` caps its length, with no rule for what wins when truth-checking flags multiple caveats.
- **Redundant stages.** Plan, 600-word paper, 1,500-word section abstracts, paragraph outline, and draft repeat the argument four times before drafting.
- **External references.** Links to `docs/process.md`, `docs/decisions.md`, and `docs/overused-devices.md` leave unclear whether those files are required.

### 5. What to cut
- **The expansion audit** (replace with a cut pass).
- **Section abstracts in stage 4** (the one-page paper already covers this).
- **Provenance tags** (`[B]`, `[S]`, `[P]`, draft status, `docs/` links). Move them to a maintainer README; non-instructional text dilutes compliance.
- **Half of `prose.md`**, including "How these rules go wrong," which repeats earlier points.

### 6. Four highest-impact changes
1. **Restrict numbers and caveats in stage 5, and replace the audit with a cut pass.**
   > "5. **Draft and cut.** Write from the outline alone; consult the pack only to verify a fact already scheduled on that paragraph's line. Add no number or caveat absent from the outline (edit the outline first if one is essential). Match each paragraph's word target. Then run a separate cut pass: shorten the draft by 15–20% by removing redundant qualifiers, empty openings, and repeated context while keeping every scheduled claim."
2. **Replace stage 4 section abstracts with paragraph budgets.**
   > "4. **Outline.** Set each section's word limit. Write one line per paragraph: `[target words] Point sentence | claims: ... | display: ... | allowed numbers: ... | caveat (if any): ...`."
3. **Move citations to stage 5** (leave only claim-ID bindings and legends for stage 7), and either drop the co-author role or place it at stage 3.
4. **Add one 150-word before/after example and a Methods/Results exception to `prose.md`** (Methods prioritises exact chronological procedure over the 1–2 number cap; Results states the pattern first, then points to figures or tables for exact values).
