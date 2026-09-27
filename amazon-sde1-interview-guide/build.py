import sys
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, PageTemplate, Frame
from reportlab.platypus import NextPageTemplate, PageBreak

from builder import build_problem, section_divider
import master_sections as ms

import data_arrays
import data_twoptr_sliding
import data_stacks
import data_binarysearch
import data_linkedlists
import data_trees
import data_graphs
import data_heaps
import data_greedy
import data_backtracking
import data_dp
import data_design
import data_other

SECTIONS = [
    ("1. Arrays & Hashing", data_arrays.PROBLEMS,
     "Foundational hash-map patterns: counting, grouping, prefix/suffix products."),
    ("2. Two Pointers", data_twoptr_sliding.PROBLEMS[:2],
     "Converging pointers on sorted data or paired constraints."),
    ("3. Sliding Window", data_twoptr_sliding.PROBLEMS[2:],
     "Growing/shrinking a contiguous window efficiently."),
    ("4. Stacks", data_stacks.PROBLEMS,
     "Most-recent-first processing: expressions, brackets, paths, monotonic stacks."),
    ("5. Binary Search", data_binarysearch.PROBLEMS,
     "Searching sorted structures, and binary-searching the ANSWER itself."),
    ("6. Linked Lists", data_linkedlists.PROBLEMS,
     "Pointer manipulation, cycle detection, and cloning with hash maps."),
    ("7. Trees & BST", data_trees.PROBLEMS,
     "Recursive tree traversal, BST properties, and tree construction."),
    ("8. Graphs", data_graphs.PROBLEMS,
     "Multi-source BFS on grids. (The playlist's generic 'graph algorithms' entry is covered here "
     "via these two concrete BFS problems, plus the BFS/DFS templates in the final cheat sheet.)"),
    ("9. Heaps / Priority Queue", data_heaps.PROBLEMS,
     "Maintaining a bounded top-K set efficiently."),
    ("10. Greedy", data_greedy.PROBLEMS,
     "Provably-optimal local choices: reachability, scheduling, capacity sweeps."),
    ("11. Backtracking", data_backtracking.PROBLEMS,
     "Constrained exploration with pruning, plus one constraint-checking problem (Valid Sudoku)."),
    ("12. Dynamic Programming", data_dp.PROBLEMS,
     "Building answers from smaller subproblems, bottom-up."),
    ("13. Design / Data Structure Design", data_design.PROBLEMS,
     "Combining structures to hit multiple operation complexity targets at once."),
    ("14. Other Important Amazon-Style Problems", data_other.PROBLEMS,
     "Bit manipulation, simulation, and greedy-formatting problems that round out the playlist."),
]

def main():
    doc = SimpleDocTemplate(
        "amazon_sde1_interview_guide.pdf",
        pagesize=LETTER,
        leftMargin=0.7*inch, rightMargin=0.7*inch,
        topMargin=0.6*inch, bottomMargin=0.6*inch,
        title="Amazon SDE1 Coding Interview Master Guide",
        author="Interview Prep Guide",
    )

    story = []
    story.extend(ms.cover_page())
    section_titles = [t for t, _, _ in SECTIONS]
    story.extend(ms.toc_page(section_titles))

    all_titles = []
    for title, problems, subtitle in SECTIONS:
        story.extend(section_divider(title, subtitle))
        for p in problems:
            all_titles.append(p["title"])
            story.extend(build_problem(p))

    story.extend(ms.cheat_sheet_page())
    story.extend(ms.how_to_talk_page())
    story.extend(ms.crash_review_page())
    story.extend(ms.sources_page(all_titles))

    doc.build(story)
    print("Built PDF with", len(all_titles), "problems.")

if __name__ == "__main__":
    main()
