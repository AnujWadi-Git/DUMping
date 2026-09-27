from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from reportlab.lib import colors
from renderer import (
    S_TITLE, S_META, S_H, S_BODY, S_SMALL, ORANGE, MUTED, FG, BOX_BORDER,
    diff_color, h, body, small, code_block, two_col, complexity_line
)


def section_divider(title, subtitle):
    from renderer import S_COVER_TITLE, S_COVER_SUB
    flow = [Spacer(1, 2.2 * inch),
            Paragraph(title, S_COVER_TITLE),
            Spacer(1, 8),
            Paragraph(subtitle, S_COVER_SUB),
            PageBreak()]
    return flow


def step(n, label, text, color="#4FD1C5"):
    return Paragraph(f'<font color="{color}"><b>{n}. {label}:</b></font> {text}', S_SMALL)


def build_problem(p):
    flow = []
    dc = diff_color(p["difficulty"])
    hexcol = "#%02x%02x%02x" % (int(dc.red*255), int(dc.green*255), int(dc.blue*255))
    flow.append(Paragraph(p["title"], S_TITLE))
    meta = (f'LeetCode #{p["lc_num"]} &nbsp;|&nbsp; <font color="{hexcol}"><b>{p["difficulty"]}</b></font> '
            f'&nbsp;|&nbsp; Pattern: {p["pattern"]} &nbsp;|&nbsp; {p.get("video_note", "")}')
    flow.append(Paragraph(meta, S_META))
    flow.append(HRFlowable(width="100%", thickness=0.75, color=ORANGE, spaceBefore=2, spaceAfter=3))

    flow.append(step("1", "Restate &amp; clarify", f'{p["problem"]} <i>Ask:</i> {p["clarify"]}', color="#FF9900"))
    flow.append(Spacer(1, 2))

    left = [
        step("2", "Brute force", p["brute_idea"]),
        code_block(p["brute_code"], max_lines=40),
        step("3", "Complexity", f'{p["brute_time"]} time, {p["brute_space"]} space'),
    ]
    right = [
        step("4", "Bottleneck", p["bottleneck"]),
        step("5", "Optimize", p["optimal_insight"]),
        Paragraph('<font color="#4FD1C5"><b>6. Code it (narrate as you write):</b></font>', S_SMALL),
        code_block(p["optimal_code"], max_lines=40),
        step("9", "Final complexity", f'{p["optimal_time"]} time, {p["optimal_space"]} space', color="#FF9900"),
    ]
    flow.append(two_col(left, right))
    flow.append(Spacer(1, 3))
    flow.append(step("7", "Test", p["test"]))
    flow.append(step("8", "Other edge cases", p["other_edges"]))
    flow.append(Paragraph(f'<font color="#FF9900"><b>Memory hook:</b></font> {p["memory_hook"]}', S_SMALL))

    flow.append(PageBreak())
    return flow
