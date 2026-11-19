#!/usr/bin/env python3
"""Split writers' outputs into parts, assign blind codes, and write the key."""
import json, random, re, sys, pathlib
T = pathlib.Path(sys.argv[1])
drafts = T / "out" / "drafts"
blind = T / "out" / "blind"; blind.mkdir(exist_ok=True)
parts_dir = T / "out" / "parts"; parts_dir.mkdir(exist_ok=True)
items = [("original", "original", (T / "src" / "original-sections.md").read_text())]
problems = []
for f in sorted(drafts.glob("*-compose.md")) + sorted(drafts.glob("*-edit.md")):
    model, arm = f.stem.rsplit("-", 1)
    text = f.read_text()
    parts = {}
    for m in re.finditer(r"(?m)^=== ([A-Z -]+) ===\s*$", text):
        parts[m.group(1).strip()] = m.end()
    names = sorted(parts, key=parts.get)
    seg = {}
    for i, n in enumerate(names):
        end = text.rfind("===", 0, parts[names[i + 1]]) if i + 1 < len(names) else len(text)
        if i + 1 < len(names):
            end = text.rfind("\n", 0, text.rfind("=== " + names[i + 1])) 
        seg[n] = text[parts[n]:end].strip()
    if "DRAFT" not in seg or len(seg["DRAFT"].split()) < 800:
        problems.append(f.name); continue
    for n, s in seg.items():
        (parts_dir / f"{model}-{arm}-{n.lower().replace(' ', '-')}.md").write_text(s + "\n")
    items.append((model, arm, seg["DRAFT"]))
random.seed(20261119)
codes = [f"D{i:02d}" for i in range(1, len(items) + 1)]
random.shuffle(codes)
key = {}
for code, (model, arm, text) in zip(codes, items):
    (blind / f"{code}.md").write_text(text.strip() + "\n")
    key[code] = {"model": model, "arm": arm}
(T / "out" / "key.json").write_text(json.dumps(dict(sorted(key.items())), indent=1))
print("drafts:", len(items), "problems:", problems)
