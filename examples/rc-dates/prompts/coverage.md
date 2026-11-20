Thank you for taking this on. Do not edit any file. Do not use the web.

`pack/claims.csv` lists the claims of a study (IDs C01 onward). `out/blind/` holds eleven versions of the article's abstract, introduction, results and discussion, named D01.md to D11.md. For each version, decide for every claim in the ledger whether the version states it. We want to know what each version leaves out, so be literal.

For each version return one item with:
- `code`: D01 to D11;
- `stated`: the claim IDs whose substance the version states, with or without the exact numbers (a rounded number or a statement in words counts);
- `partial`: claim IDs that are mentioned but with a material part missing (say which part in `notes`);
- `absent`: claim IDs not stated at all;
- `notes`: at most 60 words on the most consequential omissions for a specialist reader judging the paper, or "none".

Every claim ID in the ledger must appear in exactly one of the three lists for each version. There are 11 versions.
