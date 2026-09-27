"""Rendering helpers for the Amazon SDE1 Interview Guide PDF."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Preformatted, HRFlowable, KeepTogether, ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

styles = getSampleStyleSheet()

NAVY = colors.HexColor("#232F3E")
ORANGE = colors.HexColor("#FF9900")
LIGHT_ORANGE = colors.HexColor("#FFF3E0")
LIGHT_BLUE = colors.HexColor("#EAF2FB")
LIGHT_GREEN = colors.HexColor("#EAF7EC")
LIGHT_GREY = colors.HexColor("#F2F2F2")
DARK_GREY = colors.HexColor("#444444")
CODE_BG = colors.HexColor("#F6F8FA")
GREEN = colors.HexColor("#1B7F3A")
RED = colors.HexColor("#C0392B")

def mkstyle(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10, leading=13.5, spaceAfter=6, textColor=colors.black)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_TITLE = mkstyle("S_TITLE", fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=NAVY, spaceAfter=4)
S_SUBTITLE = mkstyle("S_SUBTITLE", fontName="Helvetica", fontSize=11, leading=14, textColor=DARK_GREY, spaceAfter=10)
S_H2 = mkstyle("S_H2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=NAVY, spaceBefore=12, spaceAfter=6)
S_H3 = mkstyle("S_H3", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=colors.HexColor("#B35C00"), spaceBefore=6, spaceAfter=3)
S_BODY = mkstyle("S_BODY", fontName="Helvetica", fontSize=9.7, leading=13, spaceAfter=5)
S_BODY_B = mkstyle("S_BODY_B", fontName="Helvetica-Bold", fontSize=9.7, leading=13, spaceAfter=5)
S_SAY = mkstyle("S_SAY", fontName="Helvetica-Oblique", fontSize=9.7, leading=13.5, textColor=colors.HexColor("#1B4D6B"))
S_KEY = mkstyle("S_KEY", fontName="Helvetica", fontSize=9.7, leading=13.5, textColor=colors.HexColor("#1B5E20"))
S_CODE = ParagraphStyle("S_CODE", fontName="Courier", fontSize=8.6, leading=11, textColor=colors.black)
S_SMALL = mkstyle("S_SMALL", fontName="Helvetica", fontSize=8.6, leading=11.5, textColor=DARK_GREY)
S_BULLET = mkstyle("S_BULLET", fontName="Helvetica", fontSize=9.7, leading=13, leftIndent=12, spaceAfter=3, bulletIndent=0)
S_TOC = mkstyle("S_TOC", fontName="Helvetica", fontSize=10.5, leading=16)
S_SECTION_TITLE = mkstyle("S_SECTION_TITLE", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=colors.white)


def diff_color(diff):
    return {"EASY": GREEN, "MEDIUM": colors.HexColor("#B8860B"), "HARD": RED}.get(diff, colors.black)


def box(flowables, bg, border, pad=8):
    t = Table([[flowables]], colWidths=[6.6 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.75, border),
        ("LEFTPADDING", (0, 0), (-1, -1), pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), pad - 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def say_this(*lines):
    paras = [Paragraph("<b>SAY THIS —</b>", mkstyle("saylabel", fontName="Helvetica-Bold", fontSize=8.5, textColor=colors.HexColor("#1B4D6B"), spaceAfter=3))]
    for l in lines:
        paras.append(Paragraph(l, S_SAY))
    from reportlab.platypus import Frame
    inner = []
    inner.extend(paras)
    tbl = box(inner, LIGHT_BLUE, colors.HexColor("#8FB8D8"))
    return tbl


def key_insight(text):
    inner = [
        Paragraph("<b>KEY INSIGHT</b>", mkstyle("keylabel", fontName="Helvetica-Bold", fontSize=8.5, textColor=colors.HexColor("#1B5E20"), spaceAfter=3)),
        Paragraph(text, S_KEY),
    ]
    return box(inner, LIGHT_GREEN, colors.HexColor("#8FCB9B"))


def code_block(code):
    code = code.rstrip("\n")
    pre = Preformatted(code, S_CODE, maxLineLength=95)
    t = Table([[pre]], colWidths=[6.6 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D0D7DE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def bullets(items, style=S_BULLET):
    return ListFlowable(
        [ListItem(Paragraph(i, style), bulletColor=ORANGE) for i in items],
        bulletType="bullet", start="•", leftIndent=14,
    )


def h2(text):
    return Paragraph(text, S_H2)


def h3(text):
    return Paragraph(text, S_H3)


def body(text):
    return Paragraph(text, S_BODY)


def complexity_table(rows):
    data = [["", "Time", "Space"]] + rows
    t = Table(data, colWidths=[1.6 * inch, 2.5 * inch, 2.5 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def recap_table(rows):
    t = Table(rows, colWidths=[1.7 * inch, 4.9 * inch])
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DDDDDD")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, LIGHT_GREY]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def dialogue(lines):
    """lines: list of (speaker, text)"""
    flow = []
    for speaker, text in lines:
        color = "#B35C00" if speaker == "Interviewer" else "#1B4D6B"
        flow.append(Paragraph(f'<font color="{color}"><b>{speaker}:</b></font> {text}', S_BODY))
    return box(flow, colors.HexColor("#FAFAFA"), colors.HexColor("#CCCCCC"))


def header_block(p):
    diff = p["difficulty"]
    dc = diff_color(diff)
    title_line = f'{p["title"]}'
    meta = f'LeetCode #{p.get("lc_num", "—")} &nbsp;|&nbsp; <font color="{dc.hexval() if hasattr(dc,"hexval") else "#000"}"><b>{diff}</b></font> &nbsp;|&nbsp; Pattern: {p["pattern"]} &nbsp;|&nbsp; {p["relevance"]}'
    flow = [
        Paragraph(title_line, S_TITLE),
        Paragraph(meta, S_SUBTITLE),
        HRFlowable(width="100%", thickness=1.2, color=ORANGE, spaceAfter=8),
    ]
    return flow


def video_source_block(p):
    vs = p.get("video_source")
    if vs:
        text = vs
    else:
        text = ("Video source: Not available from the provided source — no playlist link or video URL "
                "was included with this request, so no transcript could be retrieved. The explanation below is "
                "written from first principles / general knowledge of this problem (in the style of standard "
                "references such as NeetCode and LeetCode), not transcribed from any video.")
    return Paragraph(f'<i>{text}</i>', S_SMALL)
