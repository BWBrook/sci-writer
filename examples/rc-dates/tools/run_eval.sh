#!/usr/bin/env bash
# Resumable: skips any output that already exists and is not empty.
# Blind cold reads (Sol, Carbon) and truth checks (Sol) for every text in out/blind/.
set -u
T="$1"; E="$2"; mkdir -p "$E" "$T/out/reads" "$T/out/truth"
cd "$E"
n=0
for f in "$T"/out/blind/D*.md; do
  c=$(basename "$f" .md)
  { cat "$T/prompts/reader.md"; echo; cat "$f"; } > "$T/out/reads/$c.prompt.md"
  [ -s "$T/out/reads/$c.sol.md" ] || ~/.claude/bin/codex-delegate -m sol -e medium -C "$E" -f "$T/out/reads/$c.prompt.md" -o "$T/out/reads/$c.sol.md" --label "sciw-read-$c" > "$T/out/reads/$c.sol.log" 2>&1 &
  [ -s "$T/out/reads/$c.carbon.md" ] || ( timeout 900 bash -lc "cd $E && agy -p \"\$(cat $T/out/reads/$c.prompt.md)\" --model gemini-4-carbon-high" > "$T/out/reads/$c.carbon.md" 2> "$T/out/reads/$c.carbon.err" ) &
  sed "s/CODE/$c/g" "$T/prompts/truth.md" > "$T/out/truth/$c.prompt.md"
  [ -s "$T/out/truth/$c.json" ] || ~/.claude/bin/codex-delegate -m sol -C "$T" -f "$T/out/truth/$c.prompt.md" --schema "$T/prompts/truth.schema.json" --count '.items|length' -o "$T/out/truth/$c.json" --label "sciw-truth-$c" > "$T/out/truth/$c.log" 2>&1 &
  n=$((n+1)); if [ $((n % 4)) -eq 0 ]; then wait; fi
done
wait
echo done
