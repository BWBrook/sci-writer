# Example: the F3 brief from `silurian_plants`

The first worked example. The subject is study F3 of
[BWBrook/silurian_plants](https://github.com/BWBrook/silurian_plants): what missing fossils can say
about the age of land plants.

| File | What it is | Source |
|---|---|---|
| `before.md` | The brief as the working agents wrote it (Claude Opus 5.5 and OpenAI Codex). It still carries its claim bindings, such as `[428.8]{.C27}`. | `studies/f3/manuscript/text/brief.md` at commit `5665163`, 13 November 2026 |
| `draft-1.md` | Fable's rewrite for a general reader, written after Barry's critique of the storyline paragraph (see `docs/founding-note.md`). | Written 16 November 2026 from `text/main.md` at `220887a`; uncommitted in that repository |
| `samples-article.md` | Two short passages Fable wrote for the article, before the critique. | Conversation of 16 November 2026 |
| `cold-reads/` | Reports from two models that read the storyline paragraph and `draft-1.md` with no knowledge of the project, scored against Barry's critique. | Run 19 November 2026 |

## Status

- Barry has not yet given his reading of `draft-1.md`.
- The numbers in `draft-1.md` have not been checked against the claims ledger. One of its passages
  rested on a claim (C62) that was provisional when it was written.
- `draft-1.md` runs about 1,250 words, some 350 over the two-page limit. `before.md` fits the limit
  and omits several findings that the study reached after 13 November.
- `before.md` is out of date on the science as well as different in voice, so the pair is not a
  clean comparison of style alone.

## What to look for

`before.md` uses "molecular clock" with a definition and then lists results by number, each carrying
its own conditions. Its fourth finding, "One find can move the limit by 20 million years", is the
sentence Terra picked out as one that makes a reader want to know more.

`draft-1.md` defines each term where it appears, describes the plant, and explains the central
statistic through a doctors' rule. The cost is length.
