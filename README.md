# sci-writer

> **Status:** developed in the open as a working record. This is work in progress: contents may change, and nothing here is peer-reviewed unless stated.

AI agents can now do sound science and write it up accurately. The write-ups are hard for a person to
enjoy: every sentence carries its own defence, the numbers crowd out the argument, and the reader
must learn a private vocabulary first. This repository works on that problem. It holds guidance,
skills and worked examples that help agents write science a person wants to read, with the accuracy
kept.

It serves the research repositories of Barry W. Brook, each of which produces a journal article, a
two-page brief for any interested reader, and a guide for agents. The article and the brief are the
subject here.

## Where to start

- [`docs/founding-note.md`](docs/founding-note.md): the problem, the diagnosis, what has been agreed,
  what has been tried and what is open.
- [`docs/decisions.md`](docs/decisions.md): what has been decided, and by whom.
- [`docs/methods/`](docs/methods/): Barry's methods for writing a paper, as he gave them to his
  students and to agents.
- [`docs/overused-devices.md`](docs/overused-devices.md): ten devices that AI writers overuse, with
  examples from our own texts.
- [`examples/silurian-brief/`](examples/silurian-brief/): the first worked example, a brief before and
  after rewriting.
- [`AGENTS.md`](AGENTS.md): how agents work in this repository.

The repository is at its founding stage and will be built by iteration.

## How this work is done

Developed by Barry W. Brook with AI collaborators. Claude Fable 5.2 (Anthropic) wrote the founding
files on 19 November 2026 from a conversation with Barry in the `silurian_plants` repository. The
example brief in `examples/silurian-brief/before.md` was written by Claude Opus 5.5 (Anthropic) and
OpenAI Codex; the rewrite beside it is Fable's. The statement in `docs/correspondence/` is from Terra
(OpenAI). The documents in `docs/methods/` are by Barry W. Brook, one with Jessie Buettel, and predate
this repository. Fable also wrote `docs/overused-devices.md`. Fable ran and scored the cold reads in
`examples/silurian-brief/cold-reads/` on 19 November 2026; the readers were Sol (OpenAI
`gpt-6.2-sol`) and Gemini (Google, through `agy` 1.5.12).

## Citation

See [`CITATION.cff`](CITATION.cff). Releases of paper-grade milestones carry a
Zenodo DOI.

## Licence

Code is released under the [MIT Licence](LICENSE). Text, figures and data created for this project are released under [CC BY-SA 4.0](LICENSE-CONTENT). Third-party material keeps its own terms where stated.
