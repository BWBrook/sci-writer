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
    cautious (`prompts/truth.md`).
  - A coverage check by Sol: which of the ledger's 29 claims each text states, states in part, or
    leaves out (`prompts/coverage.md`).

## Results

| Arm | Writer | Words | Numerals per 100 words | Truth check: wrong + misleading | Claims left out entirely (of 29) |
|---|---|---|---|---|---|
| current article | | 2,445 | 4.4 | 10 + 2 | 2 |
| compose | Astra | 1,410 | 1.1 | 0 + 0 | 10 |
| compose | Terra | 1,180 | 1.0 | 1 + 1 | 12 |
| compose | Opus | 2,192 | 1.6 | 1 + 0 | 7 |
| compose | Fable | 2,259 | 2.1 | 2 + 3 | 6 |
| compose | Neon | 2,153 | 3.6 | 5 + 4 | 1 |
| edit | Astra | 2,005 | 1.2 | 1 + 2 | 5 |
| edit | Terra | 1,750 | 0.8 | 2 + 3 | 6 |
| edit | Opus | 2,363 | 3.8 | 3 + 2 | 2 |
| edit | Fable | 2,427 | 3.3 | 5 + 2 | 2 |
| edit | Neon | 2,354 | 3.9 | 8 + 2 | 2 |

Words exclude headings and citations. The full tables are in `results/`.

### What the numbers show

1. **Composing produced fewer reported faults than editing for every one of the five writers**
   (0 against 3, 2 against 5, 1 against 5, 5 against 7, 9 against 10). The current article had 12.
   Most of the faults reported against the current article and the edited drafts are statements
   that the pack does not contain, such as two percentages describing the AustArch compilation. A
   composer can only write what the pack holds, so the composed drafts could not carry them. The
   result therefore says two things: composing kept the text inside the ledger, and the ledger is
   narrower than the article it is supposed to underwrite.
2. **Composing left more out.** The composed drafts omit between 1 and 12 of the 29 claims
   entirely, the edited drafts between 2 and 6. This is the selection the process asks for, and it
   is also the cost. Whether the right claims were cut is a judgement about the science. Astra's
   plan, for example, sends the earlier measurement-scatter check that failed its criteria to the
   supplement.
3. **The writer mattered as much as the arm.** Astra and Terra cut the numbers to about a quarter
   of the original density whether they composed or edited. Opus and Fable cut them substantially
   only when composing. Neon changed little in either arm, and its composed abstract is as crowded
   as the original's.
4. **The numbers did not come back at the last expansion.** Each composer's one-page paper had a
   higher density of numerals than its full draft (`results/one-page.tsv`): Astra 1.5 then 1.1,
   Terra 1.8 then 1.0, Opus 2.0 then 1.6, Fable 2.2 then 2.1, Neon 4.4 then 3.6. Barry had seen the
   opposite when he ran his method by hand, and the restriction in stage 5 of the skill was written
   to prevent it. One test cannot show that the restriction was the cause.
5. **Editors kept the length.** Opus and Fable, told that the limits were ceilings, returned
   edited sections within a few words of every ceiling (Opus: 249 of 250, 599 of 600, 827 of 830,
   818 of 820).
6. **The model readers did not separate the texts.** Sol rated ease of reading 4 or 5 out of 7 for
   all eleven and interest 6 for all eleven. Carbon gave the current article its lowest ease (3)
   and its highest count of terms it had to guess (11), and the other ten were close together. This
   agrees with the earlier trial and with the published evidence: a model's read finds places to
   look and does not rank drafts.

### Real faults the truth check found in composed drafts

- Two drafts cite Fig. 3 for the result with two random dates per site; the figure shows one.
  The writers had captions and no figures.
- Two drafts say that if age guided the choice, the retained date is an extreme. The study tested
  the oldest and the youngest; an age-based rule could also pick a date in the middle.
- One draft turns a ten-fold ratio of densities at the two ends of the period into "ten times more
  events at one end".

### What the composers said the pack lacked

All five reported the same two gaps: the working agents' expectations and surprises ("not
recorded"), and the comparison with recent papers in the journal. Several added: no tables and no
index of the supplement, so they could not say where an omitted value could be found; captions
without the figures; claims that do not say whether "every" means every replicate or every
scenario; and nothing relating the tested trend strengths to those in real archives.

## Limits of this test

- One article, one run per cell, and no repeat to show how much two runs of the same cell differ.
- The cross-lab stages of the process were not run, so this tests the writing stages only.
- The truth check and the coverage check are one model's reading. The truth check was blind to
  arm and writer; its count for the current article shows how strict it is.
- The literature map and the working agents' account were extracted from the existing article, so
  the composers were not fully independent of it.
- Every reader was a model. The measure that matters is Barry's reading.
- The blinded copy of Fable's composed draft predates a seven-word change the writer made a minute
  later.

## What it suggests (proposals)

- For rescuing an existing draft, compose from a pack. The evidence so far is the fault counts and
  the lengths; Barry's blind reading of four openings will say whether the prose is better.
- The ledger must hold everything the article may state. The first job in a rescue is to find the
  statements in the old article that the ledger lacks and either add them with evidence or drop
  them.
- The cut list is the part of the plan that most needs the last author's eye, because it is where
  the writer decides which results the paper will not report in its main text.
- The pack needs the figures themselves, an index of tables and supplement sections, and for each
  claim the unit that "every" refers to.
- Word ceilings should be given as the journal's limit with a statement that the expected length is
  well below it, or left out for editors.
- The lead author should be chosen by trial for each lab. On this evidence Astra followed the
  skill most closely and Neon least.
