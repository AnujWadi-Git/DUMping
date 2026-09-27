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


def build_problem(p):
    flow = []
    dc = diff_color(p["difficulty"])
    hexcol = "#%02x%02x%02x" % (int(dc.red*255), int(dc.green*255), int(dc.blue*255))
    flow.append(Paragraph(p["title"], S_TITLE))
    meta = (f'LeetCode #{p["lc_num"]} &nbsp;|&nbsp; <font color="{hexcol}"><b>{p["difficulty"]}</b></font> '
            f'&nbsp;|&nbsp; Pattern: {p["pattern"]}')
    flow.append(Paragraph(meta, S_META))
    flow.append(Paragraph(p.get("video_note", ""), S_SMALL))
    flow.append(HRFlowable(width="100%", thickness=0.75, color=ORANGE, spaceBefore=3, spaceAfter=4))

    flow.append(body(f'<b>Problem:</b> {p["problem"]}'))
    flow.append(Paragraph(f'<font color="#4FD1C5"><b>Recognize it:</b></font> {p["trigger"]}', S_SMALL))
    flow.append(Spacer(1, 3))

    left = [
        h("BRUTE FORCE"),
        small(p["brute_idea"]),
        code_block(p["brute_code"], max_lines=40),
        complexity_line("Complexity", p["brute_time"], p["brute_space"]),
    ]
    right = [
        h("OPTIMAL"),
        small(p["optimal_insight"]),
        code_block(p["optimal_code"], max_lines=40),
        complexity_line("Complexity", p["optimal_time"], p["optimal_space"]),
    ]
    flow.append(two_col(left, right))
    flow.append(Spacer(1, 4))
    flow.append(Paragraph(f'<font color="#FF9900"><b>Edge case:</b></font> {p["edge_case"]}', S_SMALL))
    flow.append(Paragraph(f'<font color="#FF9900"><b>Memory hook:</b></font> {p["memory_hook"]}', S_SMALL))

    flow.append(PageBreak())
    return flow
