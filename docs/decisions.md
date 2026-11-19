# Decisions

What has been decided, by whom. Proposals stay in `docs/founding-note.md` until Barry's reading of a
worked example confirms them.

## 2026-11-19: hypotheses to test, in Barry's words (Barry)

These are Barry's views with his own qualifications kept. They direct the first test and are not
yet decisions.

- On the cause: "this 'curse of knowledge' and accretion, I agree, lies at the core of the problem
  (hypothesis, admittedly)".
- On who writes: "I think having models from all three labs writing into a paper will help, but also
  one should take the 'lead author' role."
- On separating the work from the writing: "the idea of having action agents write 'papers for
  agents' as they go, with evidence ledgers etc., but then have a fresh agent(s) write the actual
  paper once the work is ready, is a great one."
- On the existing drafts: "I suspect that all the current draft papers might benefit from being
  re-written rather than fixed, although I'm not 100% on that, and we might want to work through a
  test case." The test case he named is `rc-dates`.
- Writers available for tests: Astra, Sol and Terra (OpenAI; of Terra, "a small model, but actually
  a good writer"), Fable and Opus (Anthropic), Carbon and Neon (Google).

## 2026-11-19: Barry's writing methods are committed (Barry)

Barry supplied four of his own documents on how to write a paper, one of them written with Jessie
Buettel. They are in `docs/methods/`. On committing them publicly: "commit those: Jessie gives her
imprimatur. It's meant for general helpfulness." The other project named in the agent prompts is
public: "Haze World is all public, yes, so that's fine too."

He also confirmed where the agent version of the method fell short. See the last section of
`docs/methods/README.md`.

## 2026-11-19: the standard is a draft fit for a last author (Barry)

Barry spoke this and the quotations are from the transcript. He works as the leader of a laboratory
whose members are AI agents: "Me as last author." He helps with the early ideas, gives decisions
when they are needed, and at the end reads the draft and returns comments and line edits, "just
like I would with the student or postdoc project". Journals do not yet list AI systems as authors,
so he is the named author and declares in the AI statement that he acted as senior author.

The problem this repository exists to solve is the draft he receives. "Everything that you need to
put in an article is there, but I can't read it. It's just not written for a person." He has "10 or
20 projects that are 90 to 95% done", and the writing is "a mental block for me to even try and
tackle it".

The aim is guidance and skills that let the agents "write a much better draft as their first draft
or as their near final draft that they present to me as the last author". Two constraints: "I also
don't want to reinvent the wheel", so the work builds on published guidance for scientific writing
and on what other scientists have already tried; and the answer should be "enduring", tested across
Claude, Codex and Gemini. The brief and the article "are the two we need to get right".

## 2026-11-19: overused devices are moderated, never banned (Barry)

Barry supplied a table of ten habits of AI prose. `docs/overused-devices.md` restates them in our
own words with examples from our own texts. On whether any is a fault in itself: "All are valid
writing methods, but rendered comical by a recent history of AI overuse (as was the now-famed
em-dash)." And: "nothing banned, but great care must always be made to moderate such stylistic
tricks."

The guiding rule: "everything is written in a careful, deliberative and measured hand, with a
[view] to communicative scientific clarity rather than an inclination towards rhetorical flourish."

On headings that state a finding: "Declarative finding headings are okay, again if used with care
and purpose."

## 2026-11-19: this repository (Barry)

Barry asked Fable to set up a repository for improving "the quality, tone and general communicative
value of the final written artefacts that attach to my science repos (the brief and articles
specifically)". He suggested the name `sci-writer`. Its purpose: "to create documentation as
guidance for new agents, and also be used to develop skills, read and summarise 'how to write' pdfs
that I have, etc." It "might include some checking/parsing code eventually" and "it'll be built by
iteration". Fable created it public from `BWBrook/open-repo-template` and wrote the founding files.
A fresh agent takes the work from here.

## 2026-11-16: the lanes (Barry)

One writer owns the voice; Barry reads first and is the final arbiter; a second model edits for the
reader; the agents that did the science check for truth and flag faults without rewriting. Barry:
"Yes, I agree with your proposal for how you'd run it. It's an excellent framework that keeps the
right lanes." Detail in `docs/founding-note.md`.

## 2026-11-16: audiences (Barry)

The brief is "journalistic (broad audience: anyone who stumbles on the repo)". The article is "for
the semi-specialist (i.e., targeted at palaeobotanists and their ilk, readable by any evolutionary
ecologist or biologist)".

## Confirmed before this repository existed (Barry)

`docs/founding-note.md` records these with their quotations. They are listed here so that the
guidance has one place to cite confirmed rules from.

- **The eight symptoms** of the agents' prose: every sentence defends itself; too many numbers; a
  private dialect; everything has equal weight; no author; nothing to picture; the order of the
  analysis and not of the argument; no enthusiasm. Barry agreed with the first seven and added the
  eighth (16 November 2026).
- **What good looks like**: one question; one argument a reader could repeat; the example before the
  rule; one job per paragraph; few numbers in the prose, with exact values in tables; ordinary words
  and one name for each thing; a stated view; omission. Barry called the list "on target" (16
  November 2026).
- **From his critique of the storyline paragraph** (16 November 2026): a term is not used before it
  is defined; a metaphor does not stand in for a literal statement; a quantity is introduced before
  it is used. The wording of these three rules is Fable's; the critique they rest on is his.
- **Restraint** (16 November 2026): "Short sentences where the conclusions land, but nothing can be
  overdone, or too clever."
- **Findings are stated positively** (10 November 2026): "main messages with a '... are not x'
  negation is bad form."
- **Point first, condition second, number last; one name per thing** (12 November 2026).
- **Caveats are gathered in one short section**, with the detail in a supplement table (15 November
  2026). He also found that the agents obeyed this "to extremis", so the section itself needs a
  limit.
