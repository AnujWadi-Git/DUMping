# Amazon SDE1 Coding Interview Master Guide

`amazon_sde1_interview_guide.pdf` is the finished study guide: 54 problems from the requested
playlist, organized by pattern, each following the full 9-step Amazon interview talk track
(restate, clarify, brute force, complexity, bottleneck, optimize, code while narrating, dry run,
edge case, final complexity), plus interviewer push-back Q&A, common mistakes, a stuck-recovery
script, pattern recognition cues, a memory hook, a 30-second recap, and a full talk-track dialogue.
It ends with a Pattern Cheat Sheet, a universal "how to talk in the interview" page, a 24-hour
crash review, and a sources page.

**Note on sources:** the original request described a YouTube playlist by problem titles only,
with no playlist URL or individual video links included, so no transcripts could be retrieved.
Every explanation is written from first principles / general algorithmic knowledge, not
transcribed from any video. This is stated explicitly on the cover page, per-problem, and on the
final Sources page.

## Regenerating the PDF

```bash
pip install reportlab
python3 build.py
```

This writes `amazon_sde1_interview_guide.pdf` in the current directory. The content lives in the
`data_*.py` files (one per pattern section, each a list of problem dicts); `builder.py` and
`renderer.py` handle layout, and `master_sections.py` holds the cover page, TOC, cheat sheet, and
other front/back matter. `build.py` assembles everything in pattern order.
