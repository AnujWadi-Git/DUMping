# Amazon SDE1 Coding Interview Guide

`amazon_sde1_interview_guide.pdf` covers the 27 problems from the provided playlist
(youtube.com/playlist?list=PL_6hP3Z1GQqYrrF1flETaEpkLAX6M8E7j), one page per problem, dark theme.
Each page has: a one-line problem statement, a pattern-recognition trigger, brute-force approach
+ full code, optimal approach + full code, time/space complexity for both, an edge case, and a
memory hook. It ends with a pattern cheat sheet and a sources page.

**Note on video transcripts:** this session's network policy blocks youtube.com, so no transcripts
could be pulled from the linked playlist. Every explanation is written from general algorithmic
knowledge, not transcribed from any video — stated on the cover page, per-problem, and on the
Sources page. To get real transcripts pulled in, enable broader network access (or allowlist
youtube.com) in the environment's settings and re-run.

## Regenerating the PDF

```bash
pip install reportlab
python3 build.py
```

This writes `amazon_sde1_interview_guide.pdf` in the current directory. `data_problems.py` holds
all 27 problem dicts (title, problem statement, trigger, brute force code+complexity, optimal
code+complexity, edge case, memory hook); `builder.py` lays out one problem per page in a two-column
brute-force/optimal layout; `renderer.py` holds the dark-theme styles and the black-background page
callback; `master_sections.py` holds the cover page, TOC, cheat sheet, and sources page; `build.py`
assembles everything.
