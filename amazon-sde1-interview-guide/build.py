from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame

from renderer import on_page_black
from builder import build_problem
import master_sections as ms
import data_problems
from data_supplement import SUPPLEMENT


def main():
    problems = data_problems.PROBLEMS
    for p in problems:
        extra = SUPPLEMENT.get(p["title"])
        if extra is None:
            raise KeyError(f'No 9-step supplement fields for "{p["title"]}"')
        p.update(extra)

    doc = BaseDocTemplate(
        "amazon_sde1_interview_guide.pdf",
        pagesize=LETTER,
        leftMargin=0.55*inch, rightMargin=0.55*inch,
        topMargin=0.5*inch, bottomMargin=0.5*inch,
        title="Amazon SDE1 Coding Interview Guide",
        author="Interview Prep Guide",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    template = PageTemplate(id="black", frames=[frame], onPage=on_page_black)
    doc.addPageTemplates([template])

    story = []
    story.extend(ms.cover_page())
    story.extend(ms.toc_page(problems))
    for p in problems:
        story.extend(build_problem(p))
    story.extend(ms.cheat_sheet_page())
    story.extend(ms.sources_page(problems))

    doc.build(story)
    print("Built PDF with", len(problems), "problems.")


if __name__ == "__main__":
    main()
