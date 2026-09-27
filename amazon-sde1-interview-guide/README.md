# Amazon SDE1 Coding Interview Guide

`amazon_sde1_interview_guide.pdf` covers 73 problems, one page per problem, dark theme:
- 27 from the provided playlist (youtube.com/playlist?list=PL_6hP3Z1GQqYrrF1flETaEpkLAX6M8E7j) —
  `data_problems.py`, with real video titles/channels noted per page.
- 46 carried over from the original problem list given before the playlist link — `data_extra.py`,
  clearly marked "Not in the linked YouTube playlist" per page (no video association at all).
- 8 problems that appeared in both lists (e.g. Maximum Subarray, Group Anagrams, Rotting Oranges)
  are included once, using the playlist version.

Each page follows the 9-step Amazon talk track, labeled 1-9 on the page: restate + a clarifying
question, brute force approach + full code, its complexity, the bottleneck, the optimization + why
it works, optimal code (narrated), a test on the given example plus one edge case, other edge cases
called out, and final complexity — plus a memory hook. It ends with a pattern cheat sheet and a
sources page.

**Note on video transcripts:** this session's network policy blocks youtube.com, and Claude in
Chrome isn't connected in this cloud session either, so no transcripts could be pulled from the
linked playlist. Every explanation is written from general algorithmic knowledge, not transcribed
from any video — stated on the cover page, per-problem, and on the Sources page.

## Regenerating the PDF

```bash
pip install reportlab
python3 build.py
```

This writes `amazon_sde1_interview_guide.pdf` in the current directory.

- `data_problems.py` — the 27 playlist problems (base fields).
- `data_supplement.py` — the 9-step-talk-track fields (clarify, bottleneck, test, other_edges) for
  those 27, merged onto `data_problems.PROBLEMS` in `build.py`.
- `data_extra.py` — the other 46 problems, fully self-contained (all fields inline, no supplement
  needed).
- `builder.py` — lays out one problem per page, steps 1-9 labeled, brute-force/optimal code side by
  side in two columns.
- `renderer.py` — dark-theme styles and the black-background page callback.
- `master_sections.py` — cover page, table of contents, pattern cheat sheet, sources page.
- `build.py` — merges the supplement into the playlist problems, concatenates with the extra 46,
  and assembles the full PDF.
