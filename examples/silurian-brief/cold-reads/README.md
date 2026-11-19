# Cold reads of the storyline paragraph and of `draft-1.md`

Claude Fable 5.2, 19 November 2026. A first trial of the test proposed in open question 4 of
`docs/founding-note.md`: give a text once to a model that knows nothing of the project and ask what
it understood.

Two readers each read two texts: Sol (OpenAI `gpt-6.2-sol`, medium effort, through
`codex-delegate`) and Gemini (through `agy -p`, version 1.5.12, on its default model, which was not
recorded). The prompts are `prompt-storyline.md` and `prompt-draft-1.md`. The replies are reproduced
as returned. The readers ran in an empty directory outside this repository and were told to use no
files and no web search; whether they obeyed was not verified. Both also load Barry's global
instructions for agents, which include his preference for literal phrases over metaphor, so they
were not fully naive readers. Barry has not read these results, so nothing here is a rule.

## Storyline paragraph: the readers against Barry's nine points

Barry's critique of 16 November is the only marked text we have. The table asks whether a cold
reader finds what he found.

| Barry's phrase | Sol | Gemini | Same objection as Barry? |
|---|---|---|---|
| "Clocks" | yes | yes | yes |
| "living land plants" | yes | no | partly: Sol asked which ancestor, not why "living" |
| "how missing fossils are read" | yes | yes | partly: both called it unclear, neither called it a metaphor |
| "The silence" | yes | yes | no: both asked how long the gap is |
| "vascular-plant" | yes | yes | yes |
| "worth about three finds" | yes | yes | yes |
| "long quiet stretch" | yes | yes | no: both asked when and how long |
| "ends fast" | yes | no | no: Sol asked how fast, not for "quickly" |
| "full rate" | yes | yes | yes |

Sol marked all nine phrases and Gemini seven. Where Barry's objection was that the reader cannot
tell what is meant, the readers agreed with him. Where his objection was to the register (a sound
metaphor for a physical absence, a word the models overuse, "fast" for "quickly"), neither reader
made it. They marked "silence", "quiet" and "fast" only because a quantity was missing. Gemini did
call a different phrase, "how much the missing fossils can bear", an opaque metaphor.

The readers also marked phrases Barry did not: 8 more from Sol and 4 from Gemini. Several ask for a
number or a date ("how long", "how close"). A writer who satisfied every such request would restore
the crowding of numbers that the founding note lists as a symptom.

## `draft-1.md`: what both readers reported

- **The end answers a different question from the one the start asks.** The brief opens on the
  ancestor of all living land plants and its range of 515 to 450 million years. "What it means"
  gives two accounts of vascular plants and never returns to that range.
- **The oldest possible age goes by five names**: "oldest possible age", "oldest limit", "the
  limit", "second limit", "published limit". The way finds are counted goes by three to five.
- **Undefined terms remain**: "cysts", "three-rayed scar", "basin", "beds", "late Silurian", "plant
  body".
- **The Libyan paragraph does not connect to the limit it tests.** The limit is introduced through
  spores found in Sweden and tested through spores missing in Libya.
- **Both would cut** the paragraph on the wider *Cooksonia* group, the second set of ranges from the
  cautious count, and the finding on the late Silurian rate. Gemini counted more than twenty numbers
  in the rule-of-three passage and wanted to stop reading there.

Gemini found a fault in a heading. "The missing fossils exclude only about two million years" reads
backwards against the drug example beneath it. With no reactions in 300 patients the trial excludes
rates above 3 in 300. With no older finds, the same arithmetic excludes earlier histories longer
than about two million years; it allows two million years and excludes the rest. Sol stumbled at
the same heading in both of its reads. The fault is in the wording of the heading. The paragraph
under it and its limit of 428.8 agree with the drug example.

In the control read below, Sol also recomputed one figure. The draft says that with 24 independent
discoveries "the limit falls almost exactly on the published 431.2". From the draft's own numbers
Sol obtained about 430.8. Fable's check agrees: 426.7 + 3 x 33.23 / 24 = 430.85. The truth-checkers
should say whether "almost exactly" stands.

The readers disagreed on the one finding to keep: Sol chose the comparison of Sweden and Libya,
Gemini the tenfold difference in how often early plants were found.

## Control: the same prompt on text already repaired

Sol flagged 17 phrases in a storyline of about 125 words. To see whether that count means anything,
Sol read 439 words of `draft-1.md` under the same prompt (`prompt-control.md`, `control-sol.md`):
"The question" and the first two paragraphs of the rule-of-three finding, which Fable had written
to meet Barry's critique. Sol flagged 21 phrases.

Per 100 words the flags fell from about 14 to about 5. The count stayed near twenty. A reader told
to list every unclear phrase lists about that many whatever it is given, so the number of flags is
not a score. None of Barry's nine phrases recurs in the control, because the draft had removed them.

## What the trial suggests (proposals)

- A cold read finds failures of comprehension and of structure cheaply. Here it also found a heading
  that says the reverse of its paragraph and a figure that does not follow from the numbers beside
  it. One trial on one text supports trying it again, and no more than that.
- The questions about the whole text (state the argument; does the end answer the start; what would
  you cut) gave clearer results than the list of unclear phrases.
- A cold read does not find faults of taste. Those still need Barry's reading, or examples of it.
- A cold reader asks for more than a brief can hold. Its report is a list of places to look, and
  the writer decides what to do at each.
- Which finding a brief keeps is not settled by asking readers.
