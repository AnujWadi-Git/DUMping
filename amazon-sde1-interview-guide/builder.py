from reportlab.platypus import Spacer, PageBreak, Table, TableStyle, Paragraph
from reportlab.lib.units import inch
from reportlab.lib import colors
from renderer import (
    h2, h3, body, say_this, key_insight, code_block, bullets, complexity_table,
    recap_table, dialogue, header_block, video_source_block, S_SECTION_TITLE, NAVY
)


def section_divider(title, subtitle):
    t = Table([[Paragraph(title, S_SECTION_TITLE)]], colWidths=[6.6 * inch], rowHeights=[1.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 20),
    ]))
    from renderer import S_SUBTITLE
    flow = [Spacer(1, 1.6 * inch), t, Spacer(1, 10), Paragraph(subtitle, S_SUBTITLE), PageBreak()]
    return flow


def build_problem(p):
    """p is a dict with all the content for one problem. Returns list of flowables ending with PageBreak."""
    flow = []
    flow.extend(header_block(p))
    flow.append(video_source_block(p))
    flow.append(Spacer(1, 8))

    # STEP 1
    flow.append(h2("STEP 1 — Restate the Problem"))
    flow.append(body(p["restate"]))
    flow.append(h3("What I should clarify"))
    flow.append(bullets(p["clarify_questions"]))
    flow.append(say_this(*p["restate_say"]))

    # STEP 2
    flow.append(h2("STEP 2 — Brute Force First"))
    flow.append(h3("Idea"))
    flow.append(body(p["brute_idea"]))
    flow.append(say_this(*p["brute_say"]))

    # STEP 3
    flow.append(h2("STEP 3 — Brute Force Complexity"))
    flow.append(h3("Time Complexity"))
    flow.append(body(p["brute_time"]))
    flow.append(h3("Space Complexity"))
    flow.append(body(p["brute_space"]))
    flow.append(say_this(p["brute_complexity_say"]))

    # STEP 4
    flow.append(h2("STEP 4 — Identify the Bottleneck"))
    flow.append(body(p["bottleneck"]))
    flow.append(say_this(p["bottleneck_say"]))

    # STEP 5
    flow.append(h2("STEP 5 — Optimization"))
    flow.append(h3("Key insight / pattern: " + p["pattern"]))
    flow.append(body(p["optimization_explain"]))
    flow.append(key_insight(p["key_insight"]))
    flow.append(say_this(*p["optimization_say"]))

    # STEP 6
    flow.append(h2("STEP 6 — Code While Narrating"))
    for block in p["code_blocks"]:
        flow.append(code_block(block["code"]))
        flow.append(say_this(block["say"]))
        flow.append(body("<b>WHY:</b> " + block["why"]))
        flow.append(Spacer(1, 4))

    # STEP 7
    flow.append(h2("STEP 7 — Dry Run"))
    flow.append(body(p["dry_run"]))
    flow.append(say_this(p["dry_run_say"]))

    # STEP 8
    flow.append(h2("STEP 8 — Edge Case Test"))
    flow.append(body(p["edge_case"]))
    flow.append(say_this(p["edge_case_say"]))
    flow.append(h3("Other edge cases to remember"))
    flow.append(bullets(p["other_edge_cases"]))

    # STEP 9
    flow.append(h2("STEP 9 — Final Complexity"))
    flow.append(complexity_table(p["final_complexity_rows"]))
    flow.append(Spacer(1, 4))
    flow.append(say_this(p["final_complexity_say"]))

    # Pushback
    flow.append(h2("If the Interviewer Pushes Back"))
    for q, a in p["pushback"]:
        flow.append(h3(q))
        flow.append(body(a))

    # Mistakes
    flow.append(h2("Common Mistakes"))
    flow.append(bullets(p["mistakes"]))

    # Recovery
    flow.append(h2("If I Get Stuck — Recovery"))
    flow.append(bullets(p["recovery"]))

    # Pattern recognition
    flow.append(h2("Pattern Recognition"))
    pr = p["pattern_recognition"]
    flow.append(body(f'<b>Trigger words:</b> {pr["triggers"]}'))
    flow.append(body(f'<b>Pattern:</b> {pr["pattern"]}'))
    flow.append(body(f'<b>First thought:</b> {pr["first_thought"]}'))
    flow.append(body(f'<b>Common trap:</b> {pr["trap"]}'))

    # Memory hook
    flow.append(h2("Memory Hook"))
    flow.append(key_insight(p["memory_hook"]))

    # 30 second recap
    flow.append(h2("30-Second Recap"))
    rows = [
        ["Pattern", p["pattern"]],
        ["Key idea", p["recap_key_idea"]],
        ["Data structure", p["recap_data_structure"]],
        ["Main algorithm", p["recap_algorithm"]],
        ["Time", p["recap_time"]],
        ["Space", p["recap_space"]],
        ["Biggest edge case", p["recap_edge_case"]],
    ]
    flow.append(recap_table(rows))

    # Full talk track
    flow.append(Spacer(1, 6))
    flow.append(h2("Full Amazon Talk Track"))
    flow.append(dialogue(p["talk_track"]))

    flow.append(PageBreak())
    return flow
