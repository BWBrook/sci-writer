# sci-writer: agent guidance

This repository holds guidance, skills and worked examples that help AI agents write science for
people: text that is accurate and that a person enjoys reading. Read `docs/founding-note.md` first.
It states the problem, what has been agreed, what has been tried and what is open. Then read
`docs/decisions.md`.

Stage: founding (19 November 2026). The contents will be built by iteration with Barry. Nothing here
is settled except what `docs/decisions.md` records as decided.

## Scope

Each of Barry's research repositories produces three documents from one evidence base: a journal
article, a brief of at most two A4 pages for any interested reader, and a guide for agents. This
repository concerns the first two. The agent guide already serves its readers.

The science stays in its own repository. Here we keep what transfers between projects: the rules,
the process, the examples that show them, and any code that checks a text against them.

## Layout

- `docs/founding-note.md`: the starting point. Keep it as the record of where the work began.
- `docs/decisions.md`: what has been decided, by whom, with Barry's words quoted and dated.
- `docs/correspondence/`: statements from other agents that bear on the work.
- `examples/<name>/`: worked examples. Each has a `README.md` giving the source, the commit it came
  from, and its status.
- `library/`: Barry's reference texts on writing. Git-ignored except its `README.md`, because the
  texts are copyrighted. Commit your own summaries of them under `docs/`, never the texts.

## Conventions

- **Barry's reading is the evidence.** A rule enters the guidance when a worked example shows it
  and Barry's reaction to that example confirms it. Until then it is a proposal, and the text says
  so. Quote his words with their date.
- **Show the rule working.** Pair each rule with a before and an after taken from real text.
- **This repository follows its own rules.** Its prose is plain, literal and defines its terms.
  British spelling.
- **Sources are read, not remembered.** A statement about how an author writes comes from a text
  read in the task. Mark anything recalled from memory as such.
- **No copyrighted text is committed.** Summaries and short attributed quotations only.
- **No personal data.** Never commit or send Barry's email address or anyone's personal details.
- Record which AI systems did what in the README's "How this work is done" section.
- Commit to `main` when the work reaches a coherent state, and push. Scan first:
  `GIT_CONFIG_GLOBAL=/dev/null gitleaks protect --staged`.
