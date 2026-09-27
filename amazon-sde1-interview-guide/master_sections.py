"""Front matter, section dividers, and back matter (cheat sheet, crash review, sources)."""
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from reportlab.lib import colors
from renderer import (
    S_TITLE, S_SUBTITLE, S_H2, S_H3, S_BODY, S_BODY_B, S_SMALL, S_TOC,
    NAVY, ORANGE, LIGHT_BLUE, LIGHT_GREEN, LIGHT_ORANGE, LIGHT_GREY,
    body, h2, h3, bullets, key_insight, say_this, complexity_table
)
from builder import section_divider


def cover_page():
    title_style = S_TITLE.clone("cover_title")
    title_style.fontSize = 30
    title_style.leading = 34
    flow = []
    flow.append(Spacer(1, 1.6 * inch))
    flow.append(Paragraph("Amazon SDE1", title_style))
    flow.append(Paragraph("Coding Interview Master Guide", title_style))
    flow.append(Spacer(1, 14))
    flow.append(HRFlowable(width="60%", thickness=2, color=ORANGE, spaceAfter=14))
    flow.append(Paragraph(
        "How to solve the problem <b>and</b> how to talk through it in an Amazon coding interview.",
        S_SUBTITLE))
    flow.append(Spacer(1, 30))
    box_inner = [
        Paragraph("<b>What's inside</b>", S_H3),
        body("54 problems, organized by pattern (Arrays &amp; Hashing, Two Pointers, Sliding Window, "
             "Stacks, Binary Search, Linked Lists, Trees/BST, Graphs, Heaps, Greedy, Backtracking, "
             "Dynamic Programming, Design, and more)."),
        body("Every problem follows the same 9-step Amazon talk track: restate, clarify, brute force, "
             "complexity, bottleneck, optimize, code while narrating, dry run, edge case, final complexity."),
        body("Every problem also includes: interviewer push-back Q&amp;A, common mistakes, a recovery "
             "script for getting stuck, pattern recognition cues, a memory hook, a 30-second recap, and "
             "a full realistic talk-track dialogue."),
        body("A final Pattern Cheat Sheet, a Universal Interview Flow page, and a 24-Hour Crash Review."),
    ]
    from renderer import box
    flow.append(box(box_inner, LIGHT_ORANGE, ORANGE, pad=14))
    flow.append(Spacer(1, 24))
    flow.append(Paragraph(
        "<b>A note on sources:</b> No playlist link or video URL was included in the request that produced "
        "this guide, so no video transcripts could be retrieved. Every explanation below is written from "
        "first principles / general problem-solving knowledge (in the style of standard references such as "
        "NeetCode and LeetCode), not transcribed from any video. Where a problem's write-up references "
        "\"the video,\" that refers to this limitation — see the Sources page at the end for full detail.",
        S_SMALL))
    flow.append(PageBreak())
    return flow


def toc_page(section_titles):
    flow = []
    flow.append(Paragraph("Table of Contents", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=10))
    for i, title in enumerate(section_titles, 1):
        flow.append(Paragraph(f"{i}. {title}", S_TOC))
    flow.append(Paragraph(f"{len(section_titles)+1}. Amazon SDE1 Pattern Cheat Sheet", S_TOC))
    flow.append(Paragraph(f"{len(section_titles)+2}. How to Talk in an Amazon Coding Interview", S_TOC))
    flow.append(Paragraph(f"{len(section_titles)+3}. 24-Hour Amazon Coding Crash Review", S_TOC))
    flow.append(Paragraph(f"{len(section_titles)+4}. Sources", S_TOC))
    flow.append(PageBreak())
    return flow


def how_to_talk_page():
    flow = []
    flow.append(Paragraph("How to Talk in an Amazon Coding Interview", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=10))
    flow.append(body("This is the universal flow. Print it, read it right before you walk in."))
    steps = [
        "<b>Listen</b> — let the interviewer finish the full problem statement before saying anything.",
        "<b>Restate</b> — \"So just to confirm, we're given...\" in your own words.",
        "<b>Clarify</b> — ask 2-4 real questions: constraints, edge cases, input properties, expected output format.",
        "<b>Example</b> — walk through a small concrete example together if one isn't given.",
        "<b>Brute force</b> — state the simplest correct approach, even if obviously slow.",
        "<b>Complexity</b> — say the brute force's time and space complexity out loud, and WHY.",
        "<b>Bottleneck</b> — name specifically what's slow or wasteful about the brute force.",
        "<b>Optimize</b> — introduce the better approach and name the pattern if you recognize one.",
        "<b>Explain the data structure</b> — say why THIS structure fixes THIS bottleneck.",
        "<b>Code while talking</b> — narrate what each block does and why, in small pieces.",
        "<b>Test</b> — dry run your code on the given example, out loud, tracking variables.",
        "<b>Edge cases</b> — test at least one meaningful edge case explicitly.",
        "<b>Complexity again</b> — restate the FINAL time and space complexity, unprompted.",
        "<b>Ask if they want anything else</b> — \"Would you like me to handle any other cases, or discuss alternatives?\"",
    ]
    flow.append(bullets(steps))
    flow.append(Spacer(1, 10))
    flow.append(h2("Short Example Script"))
    from builder import dialogue
    flow.append(dialogue([
        ("Me", "So just to make sure I understand the problem correctly, we're given..."),
        ("Interviewer", "Yes, that's right."),
        ("Me", "Okay. A couple of clarifying questions first: can the input be empty, and are duplicates possible?"),
        ("Interviewer", "Assume non-empty, duplicates possible."),
        ("Me", "Got it. The straightforward approach would be to check every pair, which is O(n squared) time and O(1) space."),
        ("Interviewer", "Can you do better?"),
        ("Me", "The bottleneck is that I'm re-scanning for information I've already seen. I can fix that with a hash map, which gets us to O(n) time."),
        ("Me", "Let me code that... here I'm building a map of value to index as I scan, so I can check for a complement in O(1)."),
        ("Me", "Let me test this on the example... and here's an edge case with duplicates to make sure it still holds."),
        ("Me", "So the final solution is O(n) time and O(n) space."),
    ]))
    flow.append(PageBreak())
    return flow


def cheat_sheet_page():
    flow = []
    flow.append(Paragraph("Amazon SDE1 Pattern Cheat Sheet", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=10))
    flow.append(body("Use this as a lookup table during practice: hear the clue on the left, think the pattern on the right."))
    rows = [
        ["Interview clue", "Pattern", "Example problem(s)"],
        ["Need a pair/complement quickly", "Hash Map", "Group Anagrams, Product Except Self"],
        ["Sorted array + search for a value/boundary", "Binary Search", "Find K Closest Elements, Pow(x,n)"],
        ["Sorted array, converge from both ends", "Two Pointers", "Two Sum II, Boats to Save People"],
        ["Contiguous subarray/substring with a condition", "Sliding Window", "Min Size Subarray Sum, Find All Anagrams"],
        ["Matching brackets / most-recent-first processing", "Stack", "Evaluate RPN, Decode String, Simplify Path"],
        ["Next greater/smaller element to the side", "Monotonic Stack", "Next Greater Element I"],
        ["Shortest path in an unweighted grid/graph", "BFS", "Rotting Oranges, Walls and Gates"],
        ["Multiple starting points spreading simultaneously", "Multi-Source BFS", "Rotting Oranges, Walls and Gates"],
        ["Explore all possibilities / generate combinations", "Backtracking", "Generate Parentheses, Combination Sum"],
        ["Top-K / Kth largest or smallest, ongoing stream", "Heap", "Kth Largest in a Stream, Top K Frequent"],
        ["Best result built from repeated subproblems", "Dynamic Programming", "Climbing Stairs, Perfect Squares"],
        ["Cycle detection / duplicate via pointers", "Fast &amp; Slow Pointers", "Linked List Cycle, Find the Duplicate Number"],
        ["Locally best choice is provably globally best", "Greedy", "Jump Game, Task Scheduler, Car Pooling"],
        ["Node value bounded by ALL ancestors", "DFS with Valid Range", "Validate Binary Search Tree"],
        ["Tree values in sorted order", "In-order Traversal", "Kth Smallest Element in a BST"],
        ["Rebuild a structure from a serialized form", "Preorder DFS + markers", "Serialize/Deserialize Binary Tree"],
        ["Need O(1) insert, remove, AND random access", "Hash Map + Array", "Insert Delete GetRandom O(1)"],
        ["Overlapping intervals with a running capacity", "Difference Array / Line Sweep", "Car Pooling"],
        ["Minimize the maximum / maximize the minimum", "Binary Search on the Answer", "Split Array Largest Sum"],
        ["Pairs cancel out, one value doesn't", "Bit Manipulation (XOR)", "Single Number"],
    ]
    t = Table(rows, colWidths=[2.3*inch, 1.7*inch, 2.6*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8.3),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT_GREY]),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    flow.append(t)
    flow.append(PageBreak())
    return flow


def crash_review_page():
    flow = []
    flow.append(Paragraph("24-Hour Amazon Coding Crash Review", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=10))
    flow.append(body(
        "If you only have one day, prioritize by PATTERN, not by individual question — patterns transfer "
        "to problems you haven't seen before; memorized answers to specific questions don't. These groupings "
        "reflect how foundational and how often each pattern recurs across this guide's problems, not any "
        "claim about which exact questions Amazon will ask."))
    flow.append(h2("Must Understand (do these first)"))
    flow.append(bullets([
        "<b>Hash Map</b> — Group Anagrams, Product of Array Except Self, Top K Frequent Elements. Foundation for a huge fraction of interview problems.",
        "<b>Two Pointers</b> — Two Sum II, Boats to Save People. Simple, very common, easy points if solid.",
        "<b>Sliding Window</b> — Minimum Size Subarray Sum, Find All Anagrams. Natural extension of two pointers.",
        "<b>BFS/DFS on trees and graphs</b> — Max Depth, Validate BST, Rotting Oranges, Walls and Gates. Amazon asks tree/graph traversal constantly.",
        "<b>Dynamic Programming basics</b> — Climbing Stairs, Maximum Subarray (Kadane's). The gateway to all other DP.",
    ]))
    flow.append(h2("Should Understand"))
    flow.append(bullets([
        "<b>Stacks &amp; Monotonic Stack</b> — Evaluate RPN, Next Greater Element, Decode String.",
        "<b>Heaps</b> — Kth Largest Element in a Stream. Recognize the 'top-K' signal.",
        "<b>Backtracking</b> — Generate Parentheses, Combination Sum. Understand the prune-as-you-go mindset.",
        "<b>Binary Search variants</b> — Find K Closest Elements, and Binary Search on the Answer (Split Array Largest Sum).",
        "<b>Linked List manipulation</b> — Add Two Numbers, Linked List Cycle (Fast &amp; Slow Pointers).",
    ]))
    flow.append(h2("If Time Remains"))
    flow.append(bullets([
        "<b>Design problems</b> — Min Stack, Insert Delete GetRandom O(1). Common but lower frequency than core patterns.",
        "<b>Advanced DP</b> — Distinct Subsequences, Unique Binary Search Trees.",
        "<b>Bit manipulation</b> — Single Number, Number of 1 Bits, Reverse Bits.",
        "<b>Niche/simulation problems</b> — Car Pooling, Task Scheduler, Integer to Roman, Add Binary.",
    ]))
    flow.append(Spacer(1, 8))
    flow.append(key_insight(
        "Under time pressure, review the 30-Second Recap and Memory Hook for every problem in \"Must Understand\" "
        "first, then \"Should Understand.\" Skim the Pattern Cheat Sheet last, right before you walk in."))
    flow.append(PageBreak())
    return flow


def sources_page(problem_titles):
    flow = []
    flow.append(Paragraph("Sources", S_TITLE))
    flow.append(HRFlowable(width="100%", thickness=1, color=ORANGE, spaceAfter=10))
    flow.append(h2("Primary source"))
    flow.append(body(
        "None of the requested YouTube playlist videos could be retrieved or transcribed for this guide. "
        "The original request described a playlist of problems by title but did not include an actual "
        "playlist URL or individual video links, so this guide's explanations, code, dry runs, and talk "
        "tracks were <b>not</b> transcribed from, or based on, any specific video's transcript or narration. "
        "No quotes are attributed to any video anywhere in this guide."))
    flow.append(h2("Supporting sources"))
    flow.append(bullets([
        "LeetCode problem statements and constraints (used to confirm exact problem definitions, e.g. return formats, index conventions).",
        "General, widely-known algorithmic techniques and terminology consistent with standard references such as NeetCode's pattern catalog (Two Pointers, Sliding Window, Backtracking, etc.) — no specific NeetCode video content was transcribed or quoted.",
        "Standard computer science background on data structures and algorithms (hash maps, heaps, trees, graphs, dynamic programming, bit manipulation).",
    ]))
    flow.append(h2("Per-problem video source note"))
    flow.append(body(
        "Every problem page in this guide includes an italicized note under its title stating explicitly that "
        "video transcript access was not available for that problem, consistent with the note above. This is "
        "repeated per-problem, as requested, rather than only stated once here."))
    flow.append(Spacer(1, 10))
    flow.append(h3("Problems covered in this guide"))
    cols_text = ", ".join(problem_titles)
    flow.append(Paragraph(cols_text, S_SMALL))
    return flow
