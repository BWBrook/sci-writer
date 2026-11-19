# The expanding abstract: prompts to agents

Barry W. Brook. The prompts he pasted to an agent, in order, to take a drafted paper through the expanding-abstract steps in the `terra_prisca` project. Reproduced as supplied on 19 November 2026.

```text
Excellent. This will be an iterative and highly structured process, which we'll do in modules. The first step will be to commission two independent external reviews of the work to date, from models not involved in the development (Fable 5.2 from Anthropic and GPT-6 Pro from OpenAI). They won't see each other's reviews, and will clone the repo to a local checkout but won't write to the repo or push PRs. How would you like to prompt them for this task, so that you get the most out of this stage of the process (focusing, obviously on the novel Haze World work, within the context of the broader programme of work encompassed by the terra_prisca initiative. In essence, this is a bit like your "cover letter" to the reviewers.

Right, next step. Before I turn to the draft MS, I’d like to work through some questions first, on presentation and message, if that’s okay, one at a time.

What’s the main message in 25 words or less?

Who cares about this result? (Please keep your responses concise at this stage.)

What’s the target journal of the article? (Where would you *most* like to see it in press?)

Okay, next is a task. Ask a subagent to cross-compare the current article’s format, layout, structure, narrative style, section breakdown, number and form of display items etc., to 5 other recent relevant works from that journal, and report back on incongruities or other contrasting issues.

Okay, next is a task. PNAS is our first target: agreed. Bold but possible. Ask a subagent to cross-compare the format, layout, structure, narrative style, section breakdown, number and form of display items etc., to 5 recent relevant works from PNAS, and report back on the implications it has on how we'd go about drafting our paper.

Excellent. Make sure that cross-check is saved for reference: we'll be using that for revision. Looks to have been a very helpful exercise already! Okay, a few more things, if you're ready to continue?

First, if you now think ApJS is a better first fit, I'd suggest you get a subagent to do the same comparative pass on that journal?

Let's defer that decision until we dig a little deeper, and consult with Codex too. We should continue with the questions for now, leaving that data product vs analysis decision for later. But I presume you are still of the view that ApJS is a better fit than AJ, after re-configuring?

We'd just re-arrange the narrative so that the product is pitched as the main goal and the calibration test is support. It's no issue.

Okay, I'd like next to work through some steps to "reconstruct" the paper from first principles. I often do this with students after a first draft, so don't take it as a direct criticism or desire to scrap everything! But it is a proven method.
Step 1: Answer the Key Questions (the working abstract)
This sets the context: what you plan to do, why are you doing it, and what gap it fills in the literature (what is the long-standing question?). This working abstract won’t be something you submit for the paper – but it provides the critical context for drafting the paper. It will be a section that you can keep on referring back to as you progress through each step, to keep the main message and research questions firmly in your mind. 
The working abstract needs to contain brief answers to the following (~25 words per answer):
Why are you doing this? [context and knowledge gap that you are filling – why is this paper needed?]
What are your aims/research questions? [should be one core, and maybe multiple sub-goals]
What are the key hypotheses that underpin your aims/research questions? [try to avoid ‘silly’ null hypotheses, they should be a priori predictions that are grounded in theory.]
What did you do, or how do you plan to do it? [methodology: what type of analyses?]
What did you find? [core results – say something useful – no filler statements]
What do these results mean? [interpretation in context]
What is it good for [application] and how does it apply to a broad readership? How can it be generalised? [e.g., how is the case study useful when translated to other systems?]
You can do this within a markdown working draft (new subfolder) rather than in chat.

Next, use those working draft notes you've just done to write an actual single-paragraph abstract of <150 words (we can enlarge it later, up to the Proc B limit of 200, but keep it tight for now).

Now let's revisit and document the main message, likely distilling all the above (but 25 words or less: 26 is one too many). You might have multiple lines of evidence in your paper, but you should have one main message. If you can’t think of just one, you are either not focussing enough, or you have more than one paper to write.

That's not clear to a new reader: too much wood for trees. Don't assume anything of your reader. 

Better. Oh, and something to keep in mind throughout this revision process: narrative text loaded with uncertainties and/or caveats is generally bad form, and misses the point of them! Indeed, you really overuse negations within (or immediately following) positive statements throughout. Constraints, assumptions and limitations are better packaged up in a specific paragraph or section rather than being injected repeatedly throughout the text. This is a general writing problem that plagues RL-pilled AIs. I understand the value of caveating, but it must be communicated effectively so its not distracting...
Next, display Items: What results are most important to show? Should they be a figure (possibly multi-panel) or a table, or in the supplementary information? Do you need context items? [e.g., schematic to support methods]. How many tables and how many figures can the paper realistically support before buckling under the weight of "over-display"?

That's good, much more rational. It's always hard to do this on a first draft, which is why these reconstructions are so valuable. Lock that it: you'll discuss all this with Codex later (and me on my eventual full read) later anyway, so this is all draft for now. Let me know when you're ready for step 2. (all of the above are actually sub-components of step 1).

Step 2: The One-Page Paper
All journals impose word limits, be it 8 000, 5 000, or even 3 000 words of main text. The point is, you can never write everything you might want, no matter what the circumstance. So why not start the process with even stricter constraints? It is just a different mindset, not a radical change of strategy. Think ‘concise’!
The first task (challenge!) is to write the paper in a single page, ~600 words; about twice that of a typical abstract. A scientific poster is an example of this style, but at this stage you don’t need its figures/tables. If your results are not complete, you can still write up what you have: this approach is inherently modular.
This one-page paper should be essentially understandable as a full MS. All that is needed, but nothing else.
The material you have assembled in step 0/1 will be essential to creating this extended abstract. Work it over, repeatedly, if necessary, until you are completely happy with it. I suggest that after this is drafted, it's probably worth you iterating with Codex on the reconstructed paper steps 1, 2 and our other discussions on venue etc., before we move to step 3.
I'd start a new thread for this on the Board (new discussion, not a new section), and give Codex a bit more context on what we're doing. That'll give more of a clean area for the reconstruction.

Step 3: Expansion Stages
a. First Expansion: Section Abstracts
Next, write 4 × 300-word abstracts (concise but complete summary of the section) of all the key points you will cover in each of the Introduction, Methods, Results and Discussion (or whatever section-format the target journal calls for, if different to IMRaD). No more than 300 words. If you can’t fit all that you think you want to say within each section in 300 words, then keep trying until you can. Be ultra strict!
Note: There's no strong need for me to intervene at these stages of the reconstructions, it's the Socratic reflection (and collaboration with Codex) that matters more at this stage: I come in on the final drafts.

b. Second Expansion: Paragraph Abstracts
Okay, you have created a tight summary of each section. Now it’s time to create the paragraph structure.
First, think carefully about what paragraph framework is required to cover all the material of each section abstract. It should deliver a coherent narrative flow, with each paragraph focusing on a single key message.
Next, for each required paragraph in the section, write single-sentence summary of it. After this, check again that the ordering is right, and that all the material from the section abstract has been covered.
Lastly, for each paragraph, write it as an abstracted version, of 3–4 short, sharp sentences. No more! 
Ideally, add []-enclosed comments to each of these paragraph abstracts, to signpost the references you will cite therein. This ensures that you are incorporating the relevant context and domain knowledge.

c. Third Expansion: Full Drafting
Now you have a tight, complete paper drafted. The structure and flow should all be there, and it ought to make total sense to you. In a way, it’s complete, but it will be lacking the additional details required for a scientific paper. This is the stage that you add that flesh to the bones. But do it judiciously. Don’t overwrite!*
*Overwriting involves using more words than is necessary, leading to redundancy, filler statements, and overly flowery language. This dilutes the message's impact by obscuring key points with superfluous detail. My observation is that most people continue to overwrite. This both wastes the reader’s precious time and risks frustrating co-authors or pre-submission colleagues (if relevant) who have to plough through and edit the resulting prose.

Go ahead and do/resolve the "not done yet" items, as best you can (in the spirit that we're still drafting, and Codex will cross-check), before we move to step 4!

Step 4: Final Detailing
With the full draft is completed, go back over it to do things like adding references, specific formatting, creating display-item legends etc. Give it another careful read and a hard edit, to cut verbiage. Be concise! Think of step 3 as building a solid house. Step 4 is the painting and decorating, to make it ready for sale. 
Two reminders: 
i) Strategic repetition of your main message is key. This means saying the same thing in multiple places using different words (be clever and your readers won’t be aware that you’re doing this).
ii) After you're done on step 4, do another pass over the text, focusing specifically on context, clarity, your target audience, and a general audience: no re-structures at this stage, just textual edits with a steady, measured hand. Simplicity and plain language favoured over florid, but not at the expense of narrative engagement. It's a balancing act!

Before I review the article. Have you updated the brief, to align with the reconstructed MS, and following the same principles as in step 4 in terms of polish and clarity? If not, it'd be a good time to do that now.

One more challenge I'd now put to you for the 2-page brief (and indeed this will be of broader benefit). Many journals these days invite a "graphical abstract" to accompany a submission. These are often not compulsory, but are usually valuable. Given the purpose of the 2-page brief (to communicate the essentials of the main paper to a more general audience who is time poor and are not sure if they're sufficiently interested to read the whole paper...), I suggest that we should include a graphical abstract within it (occupying maybe 1/2 a page, leaving 1.5 pages for the rest). You have fine skills in devising, designing and tweaking SVG (and Codex is there to help and critique), or you can pick a better format that suits. It's up to you, but take your time to make the graphical abstract as interesting AND visually elegant AND communicative (without being overly wordy) as possible, and then trim the rest of the brief to keep to 2 pages total.


```
