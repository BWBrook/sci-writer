Thank you for taking this on. Do not edit any file. Do not use the web.

You are a working scientist on the study described in `pack/` (read `pack/agent-guide.md`, `pack/claims.csv`, `pack/estimands.md`, `pack/methods.md` and `pack/figures.md`). A writer has produced the draft article in `out/blind/CODE.md` (title, abstract, introduction, results, discussion; the Methods are fixed and omitted). Check it for truth. You are not judging style.

For every sentence in the draft that states a result or describes what the study did:
1. Find the claim in `claims.csv` or the passage in the pack it rests on. Report any number that is not in the pack, or that is attached to the wrong quantity, rule, proportion of sites or strength of trend.
2. Compare the sentence with the claim on five points: what is asserted; how certain it is said to be; how it relates to the evidence (observed in data, simulated, inferred); its role in the argument; and its qualifications and scope.
3. Check the draft against each "not allowed" phrasing in `estimands.md` and each trap in section 5 of the agent guide.

Report each fault with: a short quotation of the sentence; the claim ID or pack passage; what differs; and its severity, which must be one of
- `wrong`: the sentence states something the evidence contradicts or does not contain;
- `misleading`: a reader in the field would probably take away something false;
- `less_cautious`: true as far as it goes, but stated with less qualification than the ledger; a careful reader is not misled.
Do not report matters of style, and do not ask for a qualification to be restored unless its absence makes the sentence wrong or misleading. If the draft omits a result entirely, that is not a fault. Be strict about `wrong` and `misleading`: for each, say in one sentence what the false belief would be. You have permission to return an empty list.

Also give `headline_ok`: whether the abstract's statements of the main findings are all supported (true or false).
