# Test: compose afresh or edit in place? The rc-dates article

Claude Fable 5.2, 19 and 20 November 2026. Barry has not yet read the drafts, so nothing here is a
rule. His question (19 November): "I suspect that all the current draft papers might benefit from
being re-written rather than fixed, although I'm not 100% on that, and we might want to work through
a test case." The test case is the article in
[BWBrook/rc-dates](https://github.com/BWBrook/rc-dates) at commit `890a570`: how the choice of
which radiocarbon dates a site contributes can create or reverse a regional trend.

## What is and is not in this folder

The drafts, the handover pack and the article text are kept in a local folder that is not
committed. rc-dates has five human co-authors and is close to submission, and whether test rewrites
of their article are published is Barry's decision. This folder holds the protocol, the prompts
without the pack, the tools and the numbers.

## Design

One thing was varied: whether the writer **composed** the article from a handover pack without
seeing the existing prose, or **edited** the existing prose in place with the same pack to check
facts against. Everything else was held the same.

- **Writers.** Five models, each in both arms: Astra and Terra (OpenAI, through `codex-delegate`),
  Opus and Fable (Anthropic, as subagents of the Fable session), Neon (Google, through `agy`). One
  run for each of the ten cells.
- **Instructions.** The skill in `skill/sci-writer/` at draft 0.2, given whole, with a short task
  statement (`prompts/compose.md`, `prompts/edit.md`). The stages that need other agents (rival
  one-page papers, cold reader, reader's editor, truth check) were skipped inside the writing run.
- **Scope.** Title, abstract, introduction, results and discussion. The methods were fixed and
  supplied as facts. Word ceilings equal to the current draft's sections, stated as ceilings.
- **The pack.** The guide for agents, the claims ledger (ID, status, claim, value, limit), the
  interpretation specification, the figure captions and the methods, all from rc-dates with claim
  bindings removed; a literature map and a short account in the working agents' voice, both
  extracted from the existing article by Sol (`prompts/litmap.md`, `prompts/account.md`); and a
  note on the journal.
- **Blinding.** The ten drafts and the current article were given codes D01 to D11
  (`tools/split.py`; `results/key.json`).
- **Measures.**
  - `scripts/prose_check.py` from the skill, and `tools/numbers.py`, which lists numbers found
    nowhere in the pack or the article.
  - Two cold readers, Sol and Carbon (Google), each read every text once in the role of an
    archaeologist who uses radiocarbon dates (`prompts/reader.md`).
  - A truth check by Sol against the pack, reporting each fault as wrong, misleading or less
    cautious (`prompts/truth.md`). After it reported twelve faults in the current article, an Opus
    subagent checked those twelve against the rc-dates repository, and Carbon repeated the check on
    four texts with a narrower instruction.
  - A coverage check by Sol: which of the ledger's 29 claims each text states, states in part, or
    leaves out (`prompts/coverage.md`).

## Results

| Arm | Writer | Words | Numerals per 100 words, whole text | Numerals per 100 words, Results | Claims left out entirely (of 29) |
|---|---|---|---|---|---|
| current article | | 2,445 | 4.4 | 9.8 | 2 |
| compose | Astra | 1,410 | 1.1 | 2.2 | 10 |
| compose | Terra | 1,180 | 1.0 | 3.4 | 12 |
| compose | Opus | 2,192 | 1.6 | 3.6 | 7 |
| compose | Fable | 2,259 | 2.1 | 4.6 | 6 |
| compose | Neon | 2,153 | 3.6 | 6.6 | 1 |
| edit | Astra | 2,005 | 1.2 | 2.2 | 5 |
| edit | Terra | 1,750 | 0.8 | 1.9 | 6 |
| edit | Opus | 2,363 | 3.8 | 9.3 | 2 |
| edit | Fable | 2,427 | 3.3 | 6.9 | 2 |
| edit | Neon | 2,354 | 3.9 | 8.7 | 2 |

Words exclude headings and citations. The full tables are in `results/`.

### What the numbers show

1. **The writer mattered as much as the arm.** Astra and Terra cut the numbers in the Results to a
   quarter or a third of the original density whether they composed or edited. Opus, Fable and Neon
   cut them substantially only when composing; their edited Results stayed close to the original.
   Neon changed least in both arms.
2. **Composing left more out.** The composed drafts omit between 1 and 12 of the 29 claims
   entirely, the edited drafts between 2 and 6. This is the selection the process asks for, and it
   is also the cost. Whether the right claims were cut is a judgement about the science. One
   composer's plan, for example, sends the earlier measurement-scatter check that failed its
   criteria to the supplement.
3. **Composers kept to their outlines, and the outlines were generous.** Between 2 and 7 of the
   numbers in each composer's Results were absent from its own outline. But the outlines allowed
   many numbers, and in every composed draft at least half the Results paragraphs carry more than
   two numerals. The restriction in stage 5 of the skill was followed; the outline is where the
   numbers have to be refused.
4. **Editors kept the length.** The edited drafts from Opus, Fable and Neon are within about 100
   words of the original. This does not show that ceilings were treated as targets: the ceilings
   were set equal to the original's sections, so an editor who cuts little lands on them.
5. **The model readers did not separate the texts.** Sol rated ease of reading 4 or 5 out of 7 for
   all eleven and interest 6 for all eleven. Carbon gave the current article its lowest ease (3)
   and its highest count of terms it had to guess (11), and the other ten were close together. This
   agrees with the earlier trial and with the published evidence: a model's read finds places to
   look and does not rank drafts.

### The truth check did not measure what it was meant to

The first truth check (Sol, against the pack) reported 12 faults in the current article and
between 0 and 10 in the drafts, with fewer in the composed draft than in the edited draft for all
five writers. That comparison cannot be relied on, and an earlier version of this page was wrong to
present it as a result.

- An Opus subagent checked each of the 12 flags on the current article against the rc-dates
  repository itself. Nine statements are supported by the repository's own results files. One is a
  statement about the cited literature. Two are imprecise wording. **None is wrong.** The checker
  had reported statements as faults because the reduced pack did not contain them.
- A second check of four texts by Carbon, told to report only contradictions of the pack, found
  none in any of them, including the current article.
- So the first checker's counts mostly measure how far a text goes beyond the pack. A composer can
  only write what the pack holds, which is why the composed drafts scored lower. The counts say
  little about truth.

What survives from the checks:

- **One sentence in the current article is worth correcting**, and three editors carried it into
  their drafts: the sentence opening "Across the other rules" in section 3.2 generalises a result
  that holds for all dates and for random retention to rules where it fails. The composers, who
  never saw the sentence, did not reproduce it. This is the only verified case in the test of an
  edit inheriting a fault.
- **Two composed drafts cite Fig. 3 for the result with two random dates per site.** The caption
  says the figure shows one random date per site. The writers had captions and no figures.
- **The pack was too thin to check against.** It held the claims ledger, and the article states
  results that are in the repository's results files and not in the ledger. A truth check needs the
  evidence files or a fuller ledger.

Other flags on the composed drafts (for example, that "if age guided the choice, the retained date
is an extreme" overlooks rules that pick a middle date) are the first checker's opinion and have not
been verified.

### What the composers said the pack lacked

All five reported the same two gaps: the working agents' expectations and surprises ("not
recorded"), and the comparison with recent papers in the journal. Several added: no tables and no
index of the supplement, so they could not say where an omitted value could be found; captions
without the figures; claims that do not say whether "every" means every replicate or every
scenario; and nothing relating the tested trend strengths to those in real archives.

## Limits of this test

- One article, one run per cell, and no repeat to show how much two runs of the same cell differ.
- The cross-lab stages of the process were not run, so this tests the writing stages only.
- The coverage check is one model's reading and has not been verified. The truth check failed as
  a measure, as described above.
- Sol wrote two of the pack's files, ran the first truth check and the coverage check, and shares a
  lab with two of the writers.
- The literature map and the working agents' account were extracted from the existing article, so
  the composers were not fully independent of it.
- Every reader was a model. The measure that matters is Barry's reading.
- The blinded copy of Fable's composed draft predates a seven-word change the writer made a minute
  later.

## What it suggests (proposals)

- The test does not yet answer whether to compose or edit. Composing gave shorter texts with fewer
  numbers for three of the five writers and left more results out; for the other two, editing did
  as well. Whether any of it reads better is for Barry's blind reading of four openings to say.
- A truth check must be run against the evidence, or against a ledger that holds everything the
  article states. Checked against a thin pack, it reports true statements as faults.
- The cut list is the part of the plan that most needs the last author's eye, because it is where
  the writer decides which results the paper will not report in its main text.
- The pack needs the figures themselves, an index of tables and supplement sections, and for each
  claim the unit that "every" refers to.
- The outline needs a firmer hand on numbers in the Results than draft 0.2 of the skill gave it.
- The lead author should be chosen by a short trial. The writers differed more than the labs did.
