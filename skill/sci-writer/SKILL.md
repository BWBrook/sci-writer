---
name: sci-writer
description: Write or rewrite a scientific article and its two-page brief so that a person can read them in one sitting, with the science kept exact. Use when a research repository has results and a claims ledger and needs its article or brief drafted, when an accurate draft is hard to read and must be rescued, or when asked to act as lead author, reader's editor, cold reader or truth-checker on such a draft. Draft 0.3, under test; not yet confirmed by Barry.
---

# sci-writer: an article and a brief that a person can read

The standard is the draft a good postdoc hands to the last author: he reads it in one sitting and
his comments are about the science. The usual failure is a draft in which everything needed is
present and nobody can read it. It has two causes. A writer who knows the project hears its
shorthand as plain language. And a paper written while the results arrive, then patched after each
review, follows the order of the work and defends every sentence.

Write everything "in a careful, deliberative and measured hand, with a [view] to communicative
scientific clarity rather than an inclination towards rhetorical flourish" (Barry W. Brook).

This is draft 0.3. The reasons, sources and what Barry has confirmed are in `docs/process.md` of
`BWBrook/sci-writer`; you do not need that file to follow this one.

## First, find your role

- **You did the analysis.** You are a working agent. Do not write the article or the brief.
  Assemble the handover pack (`references/templates.md`), answer the lead author's questions, and
  later check the draft for truth. Report faults and leave the wording to the lead author.
- **You did none of the analysis and have been asked to write.** You are the lead author. Follow
  the stages below. Every sentence of the article and brief is yours.
- **You have been handed a text to read, or a pack to write a rival one-page paper from.** Use the
  matching instructions in `references/readers.md`.

If you are asked to write a paper whose analysis you did, say so and ask for a fresh writer.

## The stages for the lead author

Keep each stage's output; later stages and reviewers need it. Templates are in
`references/templates.md`.

1. **Read the pack and list what it lacks.** Do not read an earlier draft's prose for the sections
   you will write.
2. **Plan.** Write down: the readers, as two or three described people with what each knows and
   does not know; the main message in 25 words or fewer; the working abstract; the display items
   the paper can carry; the claims you will leave out of the main text and where each goes; and the
   vocabulary. Take the journal's requirements from the pack. Choose the cuts that remove the most
   clutter: a cut list of trivia has missed its purpose. The cut list decides which results the
   paper will not report in its main text, so give a reason for each cut and put the list where the
   last author will see it.
3. **One-page paper.** About 600 words that could stand as the whole paper. If co-authors from
   other labs have written their own from the same pack, read theirs after writing yours and
   before going on. Have a reader from another lab read yours cold (`references/readers.md`).
   Repair any mismatch with the plan now.
4. **Outline.** Go through the one-page paper and mark each place where it asks the reader to take
   a step on trust. Those are the places to expand. For each paragraph of the full paper write one
   line: its target length; the question the reader has at that point; the point that answers it;
   its claims and display item; the numbers its prose may carry; and a condition, only if the point
   would mislead without it. Be sparing with numbers here, above all in the Results: this line is
   where a number is refused, and a Results paragraph that lists four values has become a table. Read the points in order: they should make the argument by themselves.
5. **Draft, then cut.** Write each paragraph from its outline line, following
   `references/prose.md`. Go to the pack only to verify a fact the line already schedules. Add no
   number and no qualification that is not on the line; if one proves essential, change the outline
   first. Put citations in as you write and leave claim bindings until stage 7. Stop a paragraph
   once the reader can follow the inference. Then, as a separate pass, reread each paragraph against
   its line and remove what the line did not ask for.
6. **Review.** Run `scripts/prose_check.py` and look at the paragraphs it lists. Send the draft to
   a cold reader and a reader's editor from other labs, and to the working agents for the truth
   check. Repair faults of fact and likely misreadings, inside each section's length. Repeat the
   cold read after repairs.
7. **Finish.** Add bindings and legends. Rewrite the abstract from the finished text. Write the
   brief from the one-page paper for the brief's own readers. Have the truth check run again on the
   abstract, the legends and the brief, which were written after the first check. Build. Hand over
   with the plan, so that the last author can see what was intended.

## Qualifications

Keep a comparison and the uncertainty needed to interpret it together. State a condition beside a
finding wherever that finding would mislead a reader who saw it alone, and state it once. If a
secondary finding takes too long to state accurately, move the finding and its condition out
together. Everything else goes to one short limitations passage, with detail in the supplement.

## Rescuing an existing draft

Treat the old draft as a source of facts and nothing else: build the pack from the repository, then
follow the stages. Before writing, list the statements in the old draft that the ledger does not
hold, and have the working agents add each with its evidence or drop it. If you are told to edit in
place, apply `references/prose.md` and stage 6 to the existing text.

## Limits are means

A limit of 25 or 600 words exists to force a choice. Meeting it by packing more into each sentence
defeats it: after any stage with a limit, check that the text has fewer ideas, numbers and terms,
and not only fewer words. A ceiling is the most the journal allows, and a good draft is usually
well under it. No count from the script is a target, and no device named in `references/prose.md` is
banned.

## What to hand back

The plan, the one-page paper, the outline, the draft, and a list of anything the pack lacked.
