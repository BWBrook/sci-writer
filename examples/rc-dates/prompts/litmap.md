Thank you for taking this on. Do not edit any file. Do not use the web.

Context: `src/main.md` is a draft scientific article. We are testing whether a fresh writer who has never seen its prose can compose a better article from a handover pack. The pack already holds the claims, methods and figure captions. It lacks one thing a writer needs for the Introduction and Discussion: what the existing literature says and how this study relates to it. Your job is to extract that as neutral notes.

Read `src/main.md` and `src/cited-refs.tsv` (citation key, first author, year, title, journal). Write a literature map in Markdown with these parts:

1. `## Field background`: 8 to 15 terse notes, each a fact about the field that the article relies on (what the method is, what it is used for, known biases, existing remedies). After each note give the citation keys that support it, as `[@key; @key]`.
2. `## What was already known about the mechanism`: notes on prior work that this study builds on or parallels, with keys.
3. `## What this study adds, as the article frames it`: 3 to 6 notes, no keys needed.
4. `## Recommendations the article makes`: terse notes with keys where cited.
5. `## Citation keys by use`: a table of every key in `src/cited-refs.tsv` (there are 45) with first author, year, and a phrase of at most twelve words saying what it is cited for.

Rules: write notes, not prose. Do not copy any sentence or distinctive phrase from the article; restate each fact in plain, flat wording of your own. Do not add facts that are not in the article. Do not report the article's results or numbers (the writer has those in the claims ledger). If a citation's purpose is unclear from the article, write `unclear`. All 45 keys must appear in the table.
