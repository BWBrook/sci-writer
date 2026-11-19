# Cold reads of the storyline paragraph and of `draft-1.md`

Claude Fable 5.2, 19 November 2026. A first trial of the test proposed in open question 4 of
`docs/founding-note.md`: give a text once to a model that knows nothing of the project and ask what
it understood.

Two readers each read two texts, in a directory outside this repository and with no access to it:
Sol (OpenAI `gpt-6.2-sol`, medium effort, through `codex-delegate`) and Gemini (through `agy -p`).
The prompts are `prompt-storyline.md` and `prompt-draft-1.md`. The replies are reproduced as
returned. Barry has not read these results, so nothing here is a rule.

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
made it. They marked those phrases only because a quantity was missing.

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

Gemini found a fault of substance. The heading "the missing fossils exclude only about two million
years" reads backwards against the drug example beneath it. With no reactions in 300 patients the
trial excludes rates above 3 in 300. With no older finds, the same arithmetic excludes earlier
histories longer than about two million years; it allows two million years and excludes the rest.
Sol stumbled at the same sentence. This needs the writer and the truth-checkers.

The readers disagreed on the one finding to keep: Sol chose the comparison of Sweden and Libya,
Gemini the tenfold difference in how often early plants were found.

## What the trial suggests (proposals)

- A cold read finds failures of comprehension and of structure cheaply, and found one fault of
  substance. It is worth running on every draft before Barry reads it.
- A cold read does not find faults of taste. Those still need Barry's reading, or examples of it.
- A cold reader asks for more than a brief can hold. Its report is a list of places to look, and
  the writer decides what to do at each.
- Which finding a brief keeps is not settled by asking readers.
