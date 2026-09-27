"""Dark-theme, one-page-per-problem renderer for the Amazon SDE1 guide."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted, HRFlowable
)

BG = colors.HexColor("#0D0D0D")
FG = colors.HexColor("#EDEDED")
MUTED = colors.HexColor("#A0A0A0")
ORANGE = colors.HexColor("#FF9900")
CYAN = colors.HexColor("#4FD1C5")
GREEN = colors.HexColor("#7EE787")
RED = colors.HexColor("#FF6B6B")
CODE_BG = colors.HexColor("#1A1A1A")
CODE_BORDER = colors.HexColor("#333333")
BOX_BORDER = colors.HexColor("#2A2A2A")

def diff_color(d):
    return {"EASY": GREEN, "MEDIUM": ORANGE, "HARD": RED}.get(d, FG)

def mk(name, **kw):
    base = dict(fontName="Helvetica", fontSize=8.3, leading=10.6, textColor=FG, spaceAfter=2)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_TITLE = mk("S_TITLE", fontName="Helvetica-Bold", fontSize=15, leading=17, textColor=colors.white, spaceAfter=1)
S_META = mk("S_META", fontSize=8, textColor=MUTED, spaceAfter=3)
S_H = mk("S_H", fontName="Helvetica-Bold", fontSize=9, textColor=ORANGE, spaceBefore=4, spaceAfter=2)
S_BODY = mk("S_BODY")
S_CODE = ParagraphStyle("S_CODE", fontName="Courier", fontSize=6.9, leading=8.4, textColor=GREEN)
S_SMALL = mk("S_SMALL", fontSize=7.3, textColor=MUTED, leading=9.2)
S_TOC = mk("S_TOC", fontSize=10, leading=15, textColor=FG)
S_COVER_TITLE = mk("S_COVER_TITLE", fontName="Helvetica-Bold", fontSize=28, leading=32, textColor=colors.white)
S_COVER_SUB = mk("S_COVER_SUB", fontSize=12, leading=16, textColor=MUTED)


def on_page_black(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], stroke=0, fill=1)
    canvas.restoreState()


def code_block(code, max_lines=16):
    lines = code.rstrip("\n").split("\n")
    if len(lines) > max_lines:
        lines = lines[:max_lines - 1] + ["# ..."]
    code = "\n".join(lines)
    pre = Preformatted(code, S_CODE)
    t = Table([[pre]], colWidths=[3.35 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, CODE_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def two_col(left_flow, right_flow):
    t = Table([[left_flow, right_flow]], colWidths=[3.45 * inch, 3.45 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 8),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def h(text):
    return Paragraph(text, S_H)


def body(text):
    return Paragraph(text, S_BODY)


def small(text):
    return Paragraph(text, S_SMALL)


def complexity_line(label, tc, sc):
    return Paragraph(f'<font color="#4FD1C5"><b>{label}:</b></font> {tc} time &nbsp;|&nbsp; {sc} space', S_SMALL)
