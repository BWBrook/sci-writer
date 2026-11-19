# Library

Reference texts on scientific writing, and other people's attempts to make AI agents write science
well. Everything in this folder except this file is git-ignored and stays on the local disk. That
holds for the openly licensed texts too, so that one rule covers the folder (Barry, 19 November
2026: "Keep these four all uncommitted", of the copies he supplied).

When an agent reads one, it writes a summary under `docs/` in its own words: what the text advises,
which advice bears on the problem in `docs/founding-note.md`, and where it disagrees with what the
repository has already adopted. Quote sparingly and attribute each quotation.

This index lists what the folder held on 19 November 2026, so that another machine can rebuild it.
Nothing listed has been read or summarised yet. "Supplied" means Barry provided the copy.

## `guides/`: advice for human authors

| File | Work | Identifier | Terms |
|---|---|---|---|
| `gopen-swan-1990-science-of-scientific-writing.pdf` | Gopen and Swan 1990, "The Science of Scientific Writing", *American Scientist* 78: 550–558 | JSTOR 29774235 | Copyright Sigma Xi. Supplied. |
| `whitesides-2004-writing-a-paper.pdf` | Whitesides 2004, "Whitesides' Group: Writing a Paper", *Advanced Materials* | 10.1002/adma.200400767 | Copyright Wiley. Supplied. |
| `pinker-curse-of-knowledge-aps-observer-report.txt` | A report in the APS *Observer*, 30 July 2015, on Steven Pinker's account of the curse of knowledge. A report about Pinker, not his own text. | psychologicalscience.org/observer | Copyright APS. Supplied. |
| `pierce-2017-curse-of-knowledge-plmw-slides.pdf` | Benjamin C. Pierce, "The Curse of Knowledge", slides for PLMW 2017 (47 pages). By Pierce, not Pinker. | none | Copyright the author. Supplied. |
| `mensh-kording-2017-ten-simple-rules-structuring-papers.{md,xml}` | Mensh and Kording 2017, *PLOS Computational Biology* | 10.1371/journal.pcbi.1005619 | CC BY 4.0 |
| `zhang-2014-ten-simple-rules-writing-research-papers.{md,xml}` | Zhang 2014, *PLOS Computational Biology* | 10.1371/journal.pcbi.1003453 | CC BY 4.0 |
| `nature-summary-paragraph.pdf` | "How to construct a Nature summary paragraph" | nature.com/documents/nature-summary-paragraph.pdf | Copyright Springer Nature |

## `evidence/`: studies of whether writing or AI revision changes what readers do

| File | Work | Identifier | Terms |
|---|---|---|---|
| `hillier-2016-narrative-style-citation-frequency.{md,xml}` | Hillier, Kelly and Klinger 2016, *PLOS ONE* | 10.1371/journal.pone.0167983 | CC BY 4.0 |
| `weinberger-2015-ten-simple-empirical-rules-writing-science.{md,xml}` | Weinberger, Evans and Allesina 2015, *PLOS Computational Biology* | 10.1371/journal.pcbi.1004205 | CC BY 4.0 |
| `ryba-2021-better-writing-reader-confidence.pdf` | Ryba, Doubleday, Dry, Semmler and Connell 2021, *Frontiers in Psychology* | 10.3389/fpsyg.2021.714321 | CC BY 4.0 |
| `feld-lines-ross-2023-writing-matters-iza16571.pdf` | Feld, Lines and Ross, "Writing Matters", IZA Discussion Paper 16571 | iza.org/en/publications/dp/16571 | Copyright the authors |
| `apres-2026-agentic-paper-revision.pdf` | Zhao and colleagues, "APRES: An Agentic Paper Revision and Evaluation System" | arXiv:2603.03142 | See arXiv record |
| `process-oriented-evaluation-2026.pdf` | Da Silva and colleagues, "Process-Oriented Evaluation of AI-Assisted Scientific Writing", COLM 2026 | arXiv:2606.15583 | See arXiv record |
| `beyond-fluency-2026-claim-preservation.pdf` | Centonze, "Beyond Fluency", WASP workshop 2026 | aclanthology.org/2026.wasp-1.15 | ACL Anthology |
| `reliable-metrics-scientific-revision-2025.pdf` | "Identifying Reliable Evaluation Metrics for Scientific Text Revision", ACL 2025 | aclanthology.org/2025.acl-long.335 | ACL Anthology |
| `xtragpt-2026.pdf` | "XtraGPT", ACL 2026 | aclanthology.org/2026.acl-long.47 | ACL Anthology |
| `papermentor-2026.pdf` | "PaperMentor", ACL 2026 demonstrations | aclanthology.org/2026.acl-demo.39 | ACL Anthology |

## `skills/`: other people's agent skills, cloned at the commit shown

| Folder | Repository | Commit | Licence |
|---|---|---|---|
| `SNL-UCSB_paper-writing-skill` | github.com/SNL-UCSB/paper-writing-skill | `66f53c0` | MIT |
| `dvdsosa_scientific-writing-skills` | github.com/dvdsosa/scientific-writing-skills | `2eb42c9` | MIT |
| `HairuFan_research-writing-rhetorical-skill` | github.com/HairuFan/research-writing-rhetorical-skill | `2454afa` | Apache-2.0 |
| `FonaTech_Academic_Writing_Skills` | github.com/FonaTech/Academic_Writing_Skills | `086d3a5` | MIT |
| `K-Dense-AI_scientific-writing/SKILL.md` | github.com/K-Dense-AI/scientific-agent-skills, `skills/scientific-writing/SKILL.md`, fetched 19 November 2026 | main | MIT |

## Other files

- `prior-work-survey-sol-2026-11-19.json` and `prior-work-survey-prompt.md`: the survey by Sol
  (OpenAI `gpt-6.2-sol`) that found most of the above, with its prompt. Its descriptions of the
  sources are Sol's and are unverified beyond the links.

## Wanted and not yet held

- Ryba, Doubleday and Connell 2019, "How can we boost the impact of publications? Try better
  writing", *PNAS*, 10.1073/pnas.1819937116. Free to read in PubMed Central (PMC6329950); the site
  refused an automated download.
- "What AI editing changes in scientific abstracts, and what remains when the AI is asked to sound
  human", *Research Integrity and Peer Review* 2026, 10.1186/s41073-026-00269-0 (CC BY-NC-ND). The
  site refused an automated download.
- Gopen's later articles in *American Scientist*: "Getting the Point Across" (2022,
  10.1511/2022.110.6.346) and "Writing to Facilitate Reading" (2023, 10.1511/2023.111.1.28). The
  site was returning errors on 19 November.
- Schimel 2012, *Writing Science* (Oxford University Press); Pinker 2014, *The Sense of Style*; West
  and Turnbull 2023, *Scientific Papers Made Easy* (Oxford University Press); Sword 2012, *Stylish
  Academic Writing*. Books, copyrighted.
- Sand-Jensen 2007, "How to write consistently boring scientific literature", *Oikos*,
  10.1111/j.2007.0030-1299.15674.x.
