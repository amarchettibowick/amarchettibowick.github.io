# Your academic site — Manuscript / Walnut

Plain HTML/CSS, no build step, no external fonts or dependencies — everything
uses your system's serif fonts (Palatino, falling back to Georgia), so it
loads instantly and looks the same everywhere.

## Design notes
- **Palette**: warm paper background, walnut-brown ink and accent.
- **Margin rule**: the thin vertical brown line down the left edge of every
  page is intentional — it's meant to evoke a ruled manuscript margin. It's
  the `<div class="margin-rule">` right after `<body>` in each file; delete
  that one line in each file if you'd rather not have it.
- **Drop cap**: the first paragraph on the home page has an oversized first
  letter, in the classic manuscript style. Controlled by the `dropcap` class
  in `index.html` / `.bio.dropcap` in `style.css`.
- **Numbered entries**: papers on the home and research pages are numbered
  automatically via CSS counters — just add or remove `<div class="paper">`
  blocks and the numbers update themselves.
- **Leader rows**: the CV and Contact pages use a dotted "table of contents"
  line between a label and a value — a nod to a printed table of contents.

## Files
- `index.html` — home page (bio, selected papers)
- `research.html` — full publications & working papers
- `cv.html` — CV sections (plus a download button for a PDF)
- `contact.html` — email and profile links
- `style.css` — shared styling for all pages

## To customize
Everything in `[brackets]` is a placeholder. Find-and-replace across all four
`.html` files:
- `[Your Name]`
- `[Assistant Professor of Economics]`, `[University Name]`
- Bio paragraphs on `index.html`
- Paper titles, coauthors, and abstracts on `index.html` and `research.html`
- CV entries on `cv.html`
- Email and profile links on `contact.html`

To enable the "Download CV (PDF)" button, add a file named `cv.pdf` to this
same folder.

## Publishing with GitHub Pages
1. Add these files to the root of your repo (or a `docs/` folder — whichever
   your Pages source is set to).
2. Commit and push.
3. In the repo's Settings → Pages, confirm the source branch/folder matches
   where you put these files.
4. Your site will be live at `https://<username>.github.io/<repo>/`
   (or your custom domain, if configured).
