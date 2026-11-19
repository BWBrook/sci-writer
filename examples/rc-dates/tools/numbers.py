#!/usr/bin/env python3
"""List numbers in a draft that occur nowhere in the pack or the original article."""
import re, sys, pathlib, json
T = pathlib.Path(sys.argv[1])
def nums(text):
    text = re.sub(r"\[@[^\]]*\]", "", text)
    text = re.sub(r"\b(Fig(ure)?s?\.?|Table|Section|Supplementary [A-Za-z]+\.?)\s+S?\d[\w.]*(\s*(and|–|-)\s*S?\d[\w.]*)?", "", text)
    out = set()
    for m in re.findall(r"(?<![A-Za-z\d.])\d[\d,]*(?:\.\d+)?", text):
        out.add(m.replace(",", "").rstrip("."))
    return out
source = ""
for f in list((T / "pack").glob("*")) + [T / "src" / "main.md"]:
    source += f.read_text() + "\n"
src = nums(source)
small = {str(i) for i in range(0, 13)}
res = {}
for f in sorted((T / "out" / "blind").glob("D*.md")):
    d = nums(f.read_text())
    res[f.stem] = sorted(d - src - small, key=lambda x: float(x))
print(json.dumps(res, indent=1))
