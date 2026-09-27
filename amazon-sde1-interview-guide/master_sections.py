from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from reportlab.lib import colors
from renderer import (
    S_COVER_TITLE, S_COVER_SUB, S_TITLE, S_META, S_BODY, S_SMALL, S_TOC,
    ORANGE, MUTED, FG, CYAN, CODE_BG, CODE_BORDER, h, body, small
)


def cover_page():
    flow = []
    flow.append(Spacer(1, 1.7 * inch))
    flow.append(Paragraph("Amazon SDE1", S_COVER_TITLE))
    flow.append(Paragraph("Coding Interview Guide", S_COVER_TITLE))
    flow.append(Spacer(1, 10))
    flow.append(HRFlowable(width="55%", thickness=1.5, color=ORANGE, spaceAfter=14))
    flow.append(Paragraph(
        "73 problems: the 27 from your playlist, plus the 46 from the original list before the playlist "
        "link was shared. One page each. Brute force code AND optimal code, side by side.",
        S_COVER_SUB))
    flow.append(Spacer(1, 24))
    flow.append(Paragraph(
        "<b>A note on video transcripts:</b> this session's network policy blocks youtube.com, and Claude "
        "in Chrome isn't connected in this cloud session either, so no transcripts could be pulled from the "
        "linked playlist. Every explanation below is written from general algorithmic knowledge, not "
        "transcribed from any video — see the per-problem note under each title, and the Sources page "
        "at the end. The 46 problems from the original (pre-playlist) list have no associated video at "
        "all, and their notes say so plainly.",
        S_SMALL))
    flow.append(PageBreak())
    return flow


def toc_page(problems):
    flow = []
    flow.append(Paragraph("Table of Contents", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceBefore=4, spaceAfter=8))
    rows = []
    for i, p in enumerate(problems, 1):
        rows.append([str(i), p["title"], f'#{p["lc_num"]}', p["pattern"]])
    t = Table([["#", "Problem", "LC", "Pattern"]] + rows, colWidths=[0.3*inch, 2.6*inch, 0.5*inch, 2.7*inch])
    t.setStyle(TableStyle([
        ("TEXTCOLOR", (0,0), (-1,-1), FG),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("TEXTCOLOR", (0,0), (-1,0), ORANGE),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("LINEBELOW", (0,0), (-1,0), 0.75, ORANGE),
        ("LINEBELOW", (0,1), (-1,-1), 0.25, CODE_BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    flow.append(t)
    flow.append(PageBreak())
    return flow


def cheat_sheet_page():
    flow = []
    flow.append(Paragraph("Pattern Cheat Sheet", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceBefore=4, spaceAfter=8))
    rows = [
        ["Interview clue", "Pattern"],
        ["Need a pair/complement fast", "Hash Map (Two Sum, Contains Duplicate)"],
        ["Same letters/counts grouped", "Hash Map canonical key (Group Anagrams)"],
        ["Product/sum except self, no division", "Prefix * Suffix products"],
        ["# subarrays summing to k, negatives allowed", "Prefix Sum + Hash Map"],
        ["Palindrome check, O(1) space", "Two Pointers from both ends"],
        ["Maximize area/container between two points", "Two Pointers, move the shorter side"],
        ["Longest substring with a constraint", "Sliding Window"],
        ["Matching brackets / most-recent-first", "Stack"],
        ["Next greater/warmer element to the right", "Monotonic Stack"],
        ["Design O(1) getMin alongside a stack", "Auxiliary min-stack"],
        ["Implement stack with queues (or vice versa)", "Two-structure rotation trick"],
        ["Tree depth / recursive tree property", "DFS Recursion"],
        ["Process a tree/grid level by level", "BFS with queue-size snapshot"],
        ["Deep copy a graph/structure with cycles", "DFS/BFS + Hash Map (orig -> clone)"],
        ["Can all tasks finish given dependencies", "Cycle detection / Topological Sort"],
        ["Sorted array + search", "Binary Search"],
        ["Rotated sorted array", "Binary Search vs. right boundary"],
        ["O(1) get/put + evict least-recently-used", "Hash Map + Doubly Linked List"],
        ["Pick randomly with weighted probability", "Prefix Sum + Binary Search"],
        ["Multiple sources spreading simultaneously", "Multi-Source BFS"],
        ["Max sum of a contiguous subarray", "Kadane's Algorithm (DP)"],
        ["Top K frequent, bound on frequency", "Bucket Sort by frequency"],
    ]
    t = Table(rows, colWidths=[3.5*inch, 3.0*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), ORANGE),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("TEXTCOLOR", (0,1), (-1,-1), FG),
        ("FONTSIZE", (0,0), (-1,-1), 8.5),
        ("GRID", (0,0), (-1,-1), 0.4, CODE_BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    flow.append(t)
    flow.append(PageBreak())
    return flow


def sources_page(problems):
    flow = []
    flow.append(Paragraph("Sources", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceBefore=4, spaceAfter=8))
    flow.append(h("Primary source"))
    flow.append(body(
        "The playlist at youtube.com/playlist?list=PL_6hP3Z1GQqYrrF1flETaEpkLAX6M8E7j was provided. "
        "This session's network policy blocks youtube.com, and Claude in Chrome is not connected in this "
        "cloud session, so none of its videos could be fetched or transcribed. No quotes in this guide are "
        "attributed to, or copied from, any video transcript."))
    flow.append(h("Supporting sources"))
    flow.append(body(
        "LeetCode problem statements (for exact constraints/return formats) and general, widely-known "
        "algorithmic technique names and explanations, written independently."))
    flow.append(h("On the 46 non-playlist problems"))
    flow.append(body(
        "46 of the 73 problems in this guide (marked with 'Not in the linked YouTube playlist' under "
        "their title) come from the original problem list you gave before the playlist link was shared. "
        "They have no associated video at all — not just an untranscribed one."))
    flow.append(h("Videos named in the provided playlist (titles/channels, not transcribed)"))
    for p in problems:
        note = p["video_note"]
        if note.startswith("Video: "):
            flow.append(small(note.split(". Transcript")[0].replace("Video: ", "• ")))
    return flow
