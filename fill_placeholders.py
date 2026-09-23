#!/usr/bin/env python3
"""
fill_placeholders.py

Fills in the repeated [bracket] placeholders across your site's HTML files
in one pass, instead of editing four files by hand.

HOW TO USE
----------
1. Put this script in the same folder as your site's HTML files (index.html,
   research.html, data.html — the folder you download from Claude / push to
   GitHub).
2. Edit the REPLACEMENTS dictionary below: fill in the value on the right of
   each line with your real information. Leave a line blank (empty quotes)
   to skip it for now.
3. Run it:
       python3 fill_placeholders.py
4. It rewrites the .html files in place. If your folder is a git repo, run
   `git diff` afterward to see exactly what changed before you commit.

You can re-run this any time — e.g. if you redownload a new page from Claude
that still has the same bracket placeholders in it, just drop it in this
folder and run the script again.

EXTENDING IT
------------
Add more lines to REPLACEMENTS for anything you want swapped out everywhere
it appears — for example "[Coauthor Name]": "Alex Kim" if the same coauthor
shows up in several papers. For one-off content (a specific paper's title,
abstract, or a single CV entry), it's usually simplest to just type it
straight into the HTML file, since each of those is unique anyway.
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. EDIT THIS SECTION with your real information.
#    Keys must match the placeholder text exactly as it appears in the HTML.
# ---------------------------------------------------------------------------
REPLACEMENTS = {
    "[Your Name]": "Alessandro Marchetti-Bowick",
    "[Assistant Professor of Economics]": "Ph.D. candidate, Economics",
    "[University Name]": "UC Berkeley",
    "you@university.edu": "amarchettibowick[at]berkeley[dot]edu",
}

# ---------------------------------------------------------------------------
# 2. You shouldn't need to edit anything below this line.
# ---------------------------------------------------------------------------
SITE_DIR = Path(__file__).resolve().parent
HTML_FILES = sorted(SITE_DIR.glob("*.html"))
BRACKET_PATTERN = re.compile(r"\[[^\[\]]+\]")


def main():
    if not HTML_FILES:
        print("No .html files found next to this script.")
        print("Move fill_placeholders.py into the same folder as index.html, etc.")
        return

    active = {old: new for old, new in REPLACEMENTS.items() if new.strip()}
    skipped_empty = [old for old, new in REPLACEMENTS.items() if not new.strip()]

    all_found = set()
    all_replaced = set()

    for path in HTML_FILES:
        text = path.read_text(encoding="utf-8")
        all_found |= set(BRACKET_PATTERN.findall(text))

        changed = False
        for old, new in active.items():
            if old in text:
                text = text.replace(old, new)
                all_replaced.add(old)
                changed = True

        path.write_text(text, encoding="utf-8")
        print(f"{'Updated' if changed else 'No changes to'} {path.name}")

    print()
    if skipped_empty:
        print("Skipped (left blank in REPLACEMENTS — fill these in and re-run):")
        for old in skipped_empty:
            print(f"  {old}")
        print()

    remaining = sorted(b for b in all_found if b not in all_replaced)
    if remaining:
        print("Other [bracket] placeholders still in your files (unique content —")
        print("usually easiest to edit directly in the HTML):")
        for b in remaining:
            print(f"  {b}")
    else:
        print("No other bracket placeholders found.")


if __name__ == "__main__":
    main()
