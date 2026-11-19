#!/usr/bin/env python3
"""Count, per paragraph of a Markdown draft, the things a reader tires of.

The output is a list of places to look. No count is a target or a score.
Standard library only.  Usage: prose_check.py draft.md [more.md ...] [--json] [--top N]
"""
import argparse
import json
import re
import sys

WATCH = ["quiet", "quietly", "silence", "silent", "-shaped", "landscape", "delve", "crucial",
         "notably", "importantly", "robust", "nuanced", "underscore", "underscores", "highlight",
         "highlights", "pivotal", "striking", "strikingly"]
HEDGES = ["may", "might", "could", "possibly", "potentially", "perhaps", "suggest", "suggests",
          "suggesting", "appear", "appears", "seem", "seems", "likely", "plausibly", "arguably"]
NEG = re.compile(r"\b(not|no|never|neither|nor|cannot|without)\b|n't\b", re.I)
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[“\"(])")


def clean(text):
    text = re.sub(r"(?s)^---\n.*?\n---\n", "", text)                 # front matter
    text = re.sub(r"(?s)```.*?```", "", text)                        # code
    text = re.sub(r"(?s)\$\$.*?\$\$", " EQN ", text)                 # display maths
    text = re.sub(r"\$[^$\n]*\$", " MATH ", text)                    # inline maths
    text = re.sub(r"\[([^\]@]*)\]\{\.[^}]*\}", r"\1", text)         # claim bindings
    text = re.sub(r"\[@[^\]]*\]", "", text)                          # citations
    text = re.sub(r"<[^>]+>", "", text)                              # html
    return text


def numerals(par):
    par = re.sub(r"\b(Fig(ure)?s?\.?|Table|Section|Supplementary [A-Za-z]+\.?)\s+S?\d[\w.]*", "", par)
    return re.findall(r"(?<![A-Za-z])[-−+]?\d[\d,]*(?:\.\d+)?(?:[–-]\d[\d,]*(?:\.\d+)?)?%?", par)


def analyse(path):
    raw = open(path, encoding="utf-8").read()
    paras, section = [], ""
    for block in re.split(r"\n\s*\n", clean(raw)):
        block = block.strip()
        if not block:
            continue
        if block.startswith("#"):
            section = block.lstrip("# ").strip()
            continue
        if block.startswith(("|", "- ", "* ", ">", "![", "<")) or len(WORD.findall(block)) < 12:
            continue
        words = WORD.findall(block)
        low = [w.lower() for w in words]
        sents = [s for s in SENT.split(block) if s.strip()]
        slen = [len(WORD.findall(s)) for s in sents]
        paras.append({
            "section": section,
            "start": " ".join(block.split()[:8]),
            "words": len(words),
            "sentences": len(sents),
            "longest_sentence": max(slen) if slen else 0,
            "numerals": len(numerals(block)),
            "negations": len(NEG.findall(block)),
            "hedges": sum(low.count(h) for h in HEDGES),
            "parentheses": block.count("("),
            "watch": sorted({w for w in WATCH if (w in low or (w.startswith("-") and w in block.lower()))}),
        })
    n = len(paras) or 1
    words = sum(p["words"] for p in paras)
    sents = sum(p["sentences"] for p in paras) or 1
    tot = lambda k: sum(p[k] for p in paras)
    summary = {
        "file": path, "paragraphs": len(paras), "words": words,
        "words_per_sentence": round(words / sents, 1),
        "numerals": tot("numerals"),
        "numerals_per_100_words": round(100 * tot("numerals") / (words or 1), 2),
        "paragraphs_over_2_numerals": sum(p["numerals"] > 2 for p in paras),
        "share_paragraphs_over_2_numerals": round(sum(p["numerals"] > 2 for p in paras) / n, 2),
        "negations_per_100_words": round(100 * tot("negations") / (words or 1), 2),
        "hedges_per_100_words": round(100 * tot("hedges") / (words or 1), 2),
        "parentheses_per_100_words": round(100 * tot("parentheses") / (words or 1), 2),
        "sentences_over_35_words": sum(p["longest_sentence"] > 35 for p in paras),
        "watch_words": sorted({w for p in paras for w in p["watch"]}),
    }
    return summary, paras


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=5, help="paragraphs to list per file")
    a = ap.parse_args()
    out = []
    for f in a.files:
        s, paras = analyse(f)
        worst = sorted(paras, key=lambda p: (p["numerals"], p["negations"] + p["hedges"]), reverse=True)[:a.top]
        out.append({"summary": s, "look_at": worst})
    if a.json:
        json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return
    for o in out:
        s = o["summary"]
        print(f"== {s['file']}")
        for k, v in s.items():
            if k != "file":
                print(f"  {k}: {v}")
        print("  paragraphs to look at (most numerals first):")
        for p in o["look_at"]:
            print(f"    [{p['section'][:30]}] \"{p['start']}…\" words={p['words']} numerals={p['numerals']} "
                  f"negations={p['negations']} hedges={p['hedges']} longest_sentence={p['longest_sentence']}")
    print("These are places to look. No count is a target.")


if __name__ == "__main__":
    main()
