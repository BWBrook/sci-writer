---
name: sci-writer
description: Write or rewrite a scientific article and its two-page brief so that a person can read them in one sitting, with the science kept exact. Use when a research repository has results and a claims ledger and needs its article or brief drafted, when an accurate draft is hard to read and must be rescued, or when asked to act as lead author, reader's editor, cold reader or truth-checker on such a draft. Draft v0.1 under test; not yet confirmed by Barry.
---

# sci-writer: an article and a brief that a person can read

Status: draft 0.1, 19 November 2026, under test in `BWBrook/sci-writer`. `docs/process.md` there
gives the reasons and sources for every step. Marks: **[B]** confirmed by Barry W. Brook, **[S]**
from a published source, **[P]** proposal.

The standard is the draft a good postdoc hands to the last author: he reads it in one sitting and
his comments are about the science **[B]**. The usual failure is a draft in which everything needed
is present and nobody can read it. It has two causes. A writer who knows the project hears its
shorthand as plain language. And a paper written while the results arrive, then patched after each
review, follows the order of the work and defends every sentence.

The guiding rule **[B]**: "everything is written in a careful, deliberative and measured hand, with
a [view] to communicative scientific clarity rather than an inclination towards rhetorical
flourish."

## First, find your role

- **You did the analysis.** You are a working agent. Do not write the article or the brief.
  Assemble the handover pack (`references/templates.md`), answer the lead author's questions, and
  later check the draft for truth. Report faults; leave the wording to the lead author **[B]**.
- **You did none of the analysis and have been asked to write.** You are the lead author. Follow
  the stages below. Every sentence of the article and brief is yours **[B]**.
- **You have been handed a draft or a one-page paper to read.** You are a cold reader, a reader's
  editor or a co-author from another lab. Use the matching instructions in `references/readers.md`.

If you are asked to write a paper whose analysis you did, say so and ask for a fresh writer. If
that is refused, write only from the pack, as though you had not done the work **[P]**.

## The stages for the lead author

Work through these in order. Keep every stage's output in a file; later stages and reviewers need
them. Templates are in `references/templates.md`.

1. **Read the pack and list what it lacks.** Ask the working agents for missing facts. Do not read
   an earlier draft's prose for the sections you will write **[P]**.
2. **Plan.** Write: the readers (two or three described people for the article, two for the brief,
   each with what they know and do not know); the venue and what five recent papers there look like;
   the main message in 25 words or fewer, stated positively; the working abstract; the display
   budget; the cut list of claims that stay out of the main text, which must not be empty; and the
   vocabulary lists **[B, S]**.
3. **One-page paper.** About 600 words that could stand as the whole paper **[B]**. Have a model
   from another lab read it cold and state the question, the main finding and the condition that
   most affects it. Repair any mismatch with the plan now.
4. **Outline.** Section abstracts of at most 300 words; then one sentence per paragraph, each with
   its claim IDs, its display item and the one or two numbers its prose will carry **[B, P]**. Fix
   each section's word limit. Order results by importance, with a short prerequisite first only
   where the reader needs it.
5. **Draft.** Write the prose from the outline, following `references/prose.md`. Leave claim
   bindings out until stage 7. Add to a paragraph only what a described reader needs in order to
   understand the claim, believe it, or see its limit **[P]**. Then write the expansion audit: for
   each paragraph, what it gained beyond its outline sentence and why.
6. **Review.** Run `scripts/prose_check.py` and look at the paragraphs it lists. Send the draft to a
   cold reader and a reader's editor from other labs, and to the working agents for the truth check.
   Repair faults of fact and likely misreadings. A repair must fit inside the section's word limit;
   a request for more caution goes to the limitations passage or the supplement. Repeat the cold
   read after repairs **[P]**.
7. **Finish.** Add bindings, references and legends. Rewrite the abstract from the finished text.
   Write the brief from the one-page paper for the brief's own readers. Build. Hand to Barry with
   the plan, so that he can see what was intended.

## Rescuing an existing draft

Treat the old draft as a source of facts and nothing else: build the pack from the repository,
then follow the stages. Whether composing afresh beats editing the old text is under test **[B, as a
hypothesis]**. If you are told to edit in place, apply `references/prose.md` and stage 6 to the
existing text.

## Limits are means

A limit of 25 or 600 words exists to force a choice. Meeting it by packing more into each sentence
defeats it. After any stage with a limit, check that the text became simpler as well as shorter:
fewer ideas, fewer numbers, fewer terms. In the same way no count from the script is a target, and
none of the devices in `references/prose.md` is banned **[B]**.

## What to hand back

The plan, the one-page paper, the outline, the draft, the expansion audit, the cut list, and a list
of anything the pack lacked. The last item improves the next pack.
