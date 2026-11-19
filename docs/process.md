# How a paper is written here

Claude Fable 5.2, 19 November 2026. Version 0.2, a proposal. Barry has read none of it. It combines
his methods (`docs/methods/`), his decisions (`docs/decisions.md`), the published guidance and
evidence (`docs/sources/`) and the first trial (`examples/silurian-brief/cold-reads/`). Each rule
below is marked:

- **[B]** confirmed by Barry, with the entry in `docs/decisions.md`;
- **[S]** taken from a source in `docs/sources/`;
- **[P]** Fable's proposal, untested.

The skill in `skill/sci-writer/` is the same process written as instructions for an agent.

## What the process is for

The standard is the draft a good postdoc hands to the last author **[B]**. Barry should be able to
read it in one sitting and spend his comments on the science.

Three causes of the present drafts are treated here as hypotheses.

1. **The writer knows too much.** A writer who holds the whole project hears its shorthand as plain
   language (Pinker 2014, chapter 3 **[S]**; Barry's critique of the storyline paragraph **[B]**).
   Pinker's remedy is a real reader, because imagining one does not correct the bias.
2. **The paper accretes.** Text is written as results arrive and patched after each review, so it
   follows the order of the work and carries a safeguard for every past objection. Barry agreed
   that this and the first cause lie "at the core of the problem (hypothesis, admittedly)" **[B]**.
3. **Expansion is selection.** Barry's own method failed with agents at the last step, where a good
   short version became a full draft and the numbers and caveats returned **[B]**. Sol's reading of
   the sources adds that this step is a decision about which evidence, definitions and
   qualifications the reader needs, so the remedy is partly structural **[S]**.

## Who does what

**The working agents** did the science. They keep the claims ledger, the interpretation
specification and the guide for agents, and they assemble the handover pack (stage 0). They do not
write the article or the brief. After the draft exists they check it for truth and report faults
without rewording them **[B]**.

**The lead author** is one agent that did none of the analysis and starts with an empty context
**[B, as a hypothesis]**. It writes every sentence of the article and the brief, and it decides the
wording when others disagree **[B]**.

**Co-authors from the other two labs** contribute where no voice yet exists and where a second
reader is needed **[P]**:

- before any prose, each writes its own main message and one-page paper from the same pack, and the
  lead author reads all three before settling its own;
- after the draft, one acts as reader's editor and one as cold reader.

They do not write paragraphs into the lead author's draft. This is how the proposal reconciles two
of Barry's statements: "There's only one writer there, and two types of editor" (16 November) and "I
think having models from all three labs writing into a paper will help, but also one should take the
'lead author' role" (19 November). The other reading, in which different labs write different
sections, has not been tried and would be a separate test.

**Barry** is the last author **[B]**. He reads the finished draft. The process offers him one
earlier look, which he may decline: the main message and the one-page paper, about two minutes of
reading, before any section is written **[P]**. Whitesides agrees an outline with each student
before text is written, on the ground that a disagreement found in the full draft costs far more
**[S]**. The 16 November lanes had Barry read first for voice. That suits the period in which this
guidance is being calibrated against his reading; for a routine paper the proposal is that he reads
last **[P]**.

## The stages

Each stage produces a small artefact that can be checked before the next begins. The sizes are
Barry's **[B]**; the checks are proposals unless marked.

| Stage | Who | Output | Limit | Check before going on |
|---|---|---|---|---|
| 0. Handover | working agents | the pack (below) | none | the lead author lists what it could not find |
| 1. Plan | lead author; co-authors in parallel | readers, venue, main message, working abstract, display budget, cut list, vocabulary | message 25 words; seven answers of about 25 words | the three labs' messages are compared |
| 2. One-page paper | lead author; co-authors in parallel | the whole paper on one page | about 600 words | cold read; Barry's optional look |
| 3. Outline | lead author | one line per paragraph: the reader's question, the point, its claims, display and permitted numbers | a target length for each paragraph | the points read in order make the argument |
| 4. Draft, then cut | lead author | article, without claim bindings | the journal's limit, set per section at stage 3 | script; each paragraph reread against its outline line |
| 5. Review | co-authors, working agents | flags only | one round, then a second only for faults of fact | cold read repeated after repairs |
| 6. Finish | lead author | bindings, references, abstract rewritten, brief | brief two pages | build; Barry reads |

### Stage 0: the handover pack

The pack is what the fresh writer works from. It is also the specification for the "paper for
agents" that the working agents keep as they go **[B, as a hypothesis]**.

- the guide for agents and the claims ledger, each claim with its limit;
- the interpretation specification, with the phrasings that are not allowed;
- the candidate display items with captions;
- the methods as facts;
- a literature map: what the field already knows, what this study adds, and what each reference is
  cited for;
- the working agents' own account, in a few plain paragraphs: which three results matter most, what
  they expected, what surprised them, and what they think it means **[P]**. The founding note lists
  "no author" and "no enthusiasm" among the symptoms; a writer who did not do the work can only
  convey a view that someone has told it.

For an existing draft the pack is assembled from the repository, and the old prose is used only to
extract facts (the literature map, the methods). Whether the lead author should then compose afresh
or edit the old text is the question of the first test (`examples/rc-dates/`).

### Stage 1: the plan

- **Readers [S, P].** Two or three described people for the article and two for the brief, each
  with what they already know and what they do not. Brown, Pressland and Rogers ask for three named
  people the writer knows. An agent cannot know anyone, so the descriptions are written down and
  later become the instructions for the cold readers.
- **Venue [B].** The target journal, and a comparison with five recent papers from it: sections,
  length, display items, how the abstract and the first paragraph are built. A delegate does this.
- **Main message [B].** Twenty-five words or fewer, stated positively.
- **Working abstract [B].** Barry's seven questions at about 25 words each. It is a planning
  document; the abstract for publication is rewritten at stage 6 (Whitesides and the Bates guide
  write it last **[S]**, and both orders are used here for different purposes).
- **Display budget [B].** How many figures and tables the paper can carry, and which.
- **Cut list [S, P].** The claims that will not appear in the main text, each with where it goes
  (supplement, guide for agents). Brown and colleagues treat leftovers as the sign that selection
  happened. The list must not be empty.
- **Vocabulary [B, S].** One name for each thing. Three lists: terms the readers already own, which
  need no definition (Pinker **[S]**); terms the paper must teach, each with the plain sentence that
  will introduce it; and project terms that stay out of the prose. For each quantity: what is
  counted, and against what.

### Stage 2: the one-page paper

About 600 words that a reader could take as the whole paper **[B]**. The check is a cold read by a
model from another lab that has seen nothing else. It is asked for the question, the main finding,
and the condition that most affects how the finding should be taken **[S: Ryba 2021]**. Its answers
are compared with the plan. A mismatch is repaired here, where it costs a paragraph.

### Stage 3: the outline

The lead author goes through the one-page paper and marks each place where it asks the reader to
take a step on trust. Those places are where the paper expands **[S: Astra's critique]**. Each
paragraph of the full paper then gets one line: a target length, the question the reader has at that
point, the point that answers it, its claims and display item, the numbers its prose may carry, and
a condition only where the point would mislead without one. The word limit for each section is
fixed here.

Barry's method has a step between the one-page paper and the paragraphs: four section abstracts of
300 words **[B]**. Version 0.2 leaves it out. Astra and Neon both judged that for an agent the
section abstracts are a further 1,200 words of prose that the next step enlarges, and that the
outline loses the reason each paragraph follows the last. This departs from a method Barry
confirmed, on the ground that he also confirmed where that method failed with agents. It is a
proposal for the test and his to reverse.

Results are ordered by importance **[B: "you are not composing Boléro"; S: Whitesides]**. Where a
reader needs a control or a method to interpret the main result, that comes first and is kept short
**[S: Mensh and Kording]**.

### Stage 4: the draft, then the cut

The lead author writes each paragraph from its outline line, without claim bindings; `[428.8]{.C27}`
is added at stage 6 **[P]**. A sentence built around a bound number tends to be a sentence about the
number. Citations go in during drafting, because they carry the argument of the introduction and
the discussion **[S: Neon's critique]**.

The rule for expansion **[P]**: a paragraph may carry only the numbers and the condition on its
outline line. If another proves essential, the outline is changed first. The writer stops a
paragraph once the reader can follow the inference. A separate pass then rereads each paragraph
against its line and removes what the line did not ask for.

Version 0.1 had the writer justify each addition in an "expansion audit". Both critics said a model
would fill it in after the fact and delete nothing, so it was replaced by the restriction above and
the cut pass.

Qualifications **[B, S]**: a comparison and the uncertainty needed to interpret it stay together. A
condition is stated beside a finding wherever the finding would mislead a reader who saw it alone,
and stated once. If a secondary finding takes too long to state accurately, the finding and its
condition leave the main text together **[S: Astra's critique]**. The others go to one short
limitations passage, and their detail to a supplement table. A hedge is replaced by the condition or
the size of the uncertainty where that is known (Pinker **[S]**).

The sentence-level rules, with one worked example, are in `skill/sci-writer/references/prose.md`.

### Stage 5: review

Four checks, in this order **[P]**.

1. **Script.** `skill/sci-writer/scripts/prose_check.py` counts numerals, negations, hedges and
   watched words per paragraph and lists the densest paragraphs. Its output is a list of places to
   look. No count is a target.
2. **Cold read.** A model from another lab, given only the draft, answers the whole-text questions,
   including how the authors got from what they measured to what they concluded and where the
   reader had to supply a step **[S: Astra's critique]**. A reader can recover the question and the
   headline from an abstract alone, so this question is the one that tests the body.
3. **Reader's editor.** A model from another lab marks where it lost the thread, where the text is
   flat and where it tries too hard **[B]**. It may suggest wording; the lead author decides.
4. **Truth check.** The working agents compare each sentence that states a result with the ledger
   and the interpretation specification. For each changed claim they check five things: the
   proposition, the certainty, the relation to evidence, the role in the argument, and the
   qualifications (Centonze 2026 **[S]**). They report faults and do not reword **[B]**.

Rules that keep the review from rebuilding the old draft **[P]**:

- A repair must fit inside the section's word limit. A repair that adds a qualification displaces
  something or goes to the limitations passage.
- A reviewer's request is classed as a fault of fact, a likely misreading, or a wish for more
  caution. Only the first two change the main text.
- After repairs the cold read is repeated, because edits that improve single sentences can damage
  the coherence of the whole (Da Silva and colleagues 2026 **[S]**).
- One round. A second round is for faults of fact only.

### Stage 6: finish

Bindings and legends are added; the abstract is rewritten from the finished text; the build is run.
The truth check runs again on the abstract, the legends and the brief, which are written after the
first check **[S: Astra's critique]**. The brief is written from the one-page paper for its own readers, and is not a
shortened article **[P]**. Then Barry reads.

## Where the sources disagree, and what this process does

| Question | One view | Another | Here |
|---|---|---|---|
| Where does the answer go? | Raised first, answered last (founding note) | Given early and repeated (Brown; Pinker; Pierce) | Given early, and returned to at the end **[P]**. This changes one line of the founding note's list and needs Barry's word. |
| When is the abstract written? | First, as a plan (Brown; Barry) | Last (Whitesides; Bates) | Both: a working abstract first, the published abstract last |
| What opens a unit? | The point (Barry) | Familiar material, with the new at the end (Gopen and Swan; Pinker) | A paragraph opens with its point. Within a sentence the familiar comes first and the new last. |
| Order of results | Most important first (Whitesides; Barry) | What the reader must know first (Mensh and Kording) | Importance, with a short prerequisite where needed |
| Must every term be defined? | Yes (founding note) | Only those the audience lacks (Pinker) | By audience, using the vocabulary lists |
| Hedges | Remove them (Pinker; Ryba's accessible versions) | Removing one can change the claim (Centonze) | Replace with the condition; the truth check decides |
| Repetition of the message | In four places (Brown; Barry) | A device that agents overdo (`docs/overused-devices.md`) | Title, abstract, opening of the discussion, close; different words; no comment on itself |
| Headings that state findings | Preferred (Whitesides; Mensh and Kording) | With care (Barry) | Allowed where the section has one finding |

## How we will know it works

Sol's reading of the evidence found that this project had been leaning too hard on one idea: a model
reading cold cannot establish that a human reader would follow or enjoy a text. A cold read locates
faults. It does not rank drafts. A study of revision metrics found that model judges agreed with
people's preferences 56% of the time overall, and least when both versions were acceptable **[S:
Jourdan 2025]**. Our own trial found that two readers missed Barry's objections of taste on
"silence", "quiet" and "fast".

Three outcomes are therefore kept apart **[S, P]**:

- **Comprehension**: a reader's answers to the whole-text questions, scored against the plan.
- **Fidelity**: the truth check, with every number traced to the ledger.
- **Wanting to read on**: Barry's reading, and for the brief a reader from its intended audience.
  Useful records are whether he finished, where he stopped, and whether his comments were about the
  science or the prose.

Two results in the library are randomised experiments on people: Ryba and colleagues 2021, on
abstracts, and Feld, Lines and Ross, on edited economics papers. Both tested packages of changes
(structure first, then sentences), and neither isolates a single rule. The rest of the advice here
rests on experience and on Barry's reading.

## What the other labs' critique changed

Before any test, Fable sent draft 0.1 of the skill to Astra (OpenAI) and Neon (Google) and asked
what a model would ignore, what it would obey too literally, and what to change. Their replies are
in `docs/correspondence/`. They agreed with each other on the main points, and draft 0.2 adopts
these:

- the expansion audit is replaced by a restriction and a cut pass;
- the outline records why the reader needs each paragraph, and the section abstracts are dropped;
- the skill carries one worked example of an outline line and the paragraph written from it;
- the marks **[B]**, **[S]** and **[P]** are kept in this document and removed from the copy the
  writer reads, where they diluted the instructions;
- the journal's requirements come to the writer in the pack; the writer does not look them up;
- "state findings positively" now carries a warning against turning a failure to detect a
  difference into a statement of equality;
- the rule on numbers allows a paragraph to have none, and treats an estimate with its interval as
  one;
- Methods and Results have their own short rules.

One suggestion was not adopted. Neon proposed a cut pass that shortens the draft by 15 to 20 per
cent. A percentage is the kind of target that agents meet mechanically, so the cut pass is defined
by the outline line.

## Not yet settled

The eight open questions in `docs/founding-note.md` remain open. This document answers the first in
draft (a skill plus this explanation) and proposes tests for the fourth, seventh and eighth.
