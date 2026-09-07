# CLAUDE.md

## Project

You are building a complete, publishable online course titled **"Design for Manufacturing and Assembly: From Prototype to Production"** (working title; the author may rename it). The deliverable is a multi-page static HTML site that can be deployed as-is to GitHub Pages, Netlify, or any web host with no build step.

The author is Erdem Yilmaz, a senior manufacturing engineer with about eight years of NPI experience across HVAC, heat pump water heaters, and residential thermal storage products. The course is written in his voice as an experienced practitioner, not as a textbook. It will be promoted on LinkedIn and hosted on his own domain, so credibility is the single most important property of this project. A course with one fabricated citation is worse than a course with no citations.

## Audience

Junior to mid-level mechanical and manufacturing engineers (roughly 0 to 5 years of experience). They know CAD and basic materials and processes. They have not yet been through a full production ramp, a supplier DFM review that rejected their part, or a tolerance stack-up that failed at PVT. Write for a reader who is smart, busy, and wants rules they can apply on Monday.

Assume they are comfortable with basic statistics, engineering drawings, and unit conversions, but explain every acronym on first use and every standard the first time it appears.

## Scope

Full DFx:

- DFM (design for manufacturing) by process: CNC machining, sheet metal, injection molding, die casting and other casting, forging, additive manufacturing, PCB and PCBA  
- DFA (design for assembly): part count reduction, Boothroyd Dewhurst method, fastening, poka-yoke, assembly sequence  
- DFT (design for test): test points, in-circuit and functional test, fixtures, test coverage, testability of mechanical assemblies  
- DFS (design for service and serviceability)  
- Supporting topics: tolerancing and GD\&T for manufacturability, process capability, process selection, cost modeling and should-cost, supplier and contract manufacturer engagement, NPI phase gates (EVT, DVT, PVT), regulatory and compliance considerations that affect design

## Non-negotiable rules

### 1\. Every real-world example, study, statistic, and standard must be verified

- Before writing any case study, historical example, statistic, or citation, use web search to find a primary or credible secondary source and read it. Do not write a claim first and look for a source afterward.  
- Every module ends with a **References** section. Each reference has: author or organization, title, publisher or site, year, URL, and the date you accessed it.  
- Every factual claim that a skeptical senior engineer might challenge gets an inline citation like `[3]` that links to the References entry.  
- Maintain `SOURCES.md` at the repo root: one entry per source, with a one-line note on what it supports and a verification status of **verified** (you read the source and it says what you claim), **secondary** (you found it cited by a credible source but could not read the original), or **unverified**. Unverified sources may not appear in the course. Secondary sources must be labeled as such in the References section.  
- If you cannot verify a widely repeated claim (for example, "70 to 80 percent of product cost is committed during design" or "the rule of 10 for cost of change"), you may still teach the idea, but you must attribute it honestly: say it is a widely cited rule of thumb, name where it is usually attributed, and note that the original data is hard to trace. Never attach a fake precision or a fake study to it.  
- Never invent a company case study, a cost figure, a percentage, a named engineer, or a paper. If you need an illustrative example and no verified real one exists, write it as a clearly labeled **worked example** with invented but realistic numbers and say so in the text ("This is an illustrative example, not a real program").  
- Standards must be cited by their correct designation and current revision, verified by search (for example ASME Y14.5-2018, ISO 2768-1:1989, ISO 286-1:2010, IPC-2221B, IPC-A-610H, IPC-2231, ISO 8015). If you are unsure of a revision, check it. Do not quote standard text verbatim; paraphrase and cite.

### 2\. Do not use the author's employer information

The author has worked at several companies. Do not include any case study, number, supplier name, part, or process detail that could only come from his employers, and do not ask him to supply such details. All examples come from public, verifiable sources or from clearly labeled illustrative examples. If a section would benefit from a personal anecdote, leave a clearly marked placeholder `<!-- AUTHOR: optional personal note here -->` in the HTML source so he can decide what to add himself.

### 3\. Do not copy text or images from other design guides

Manufacturer design guides (Protolabs, Xometry, Fictiv, Hubs, Star Rapid, and similar) are excellent sources for numeric design rules and should be cited, but their text must be paraphrased and their images must not be embedded or traced. All diagrams are drawn by you as inline SVG. Never hotlink images from other sites.

### 4\. Metric units only

All dimensions, tolerances, temperatures, and rates use SI or metric units (mm, µm, °C, MPa, kg, N·m). Where a source gives a value in inches or mils, convert it and cite the original value in parentheses only if the source is explicitly imperial (for example, PCB trace width in mils is common; show mm first and mils in parentheses). Never mix inches and micrometres in the same table.

### 5\. No placeholder content in the final deliverable

No lorem ipsum, no "TODO", no "coming soon", no empty quiz. If a section is not finished, it is not linked from the navigation until it is.

## Curriculum

Build these modules in this order. Each module is one HTML page. Target 2,500 to 4,500 words of body text per module, plus tables, diagrams, exercises, and quiz. Adjust if a topic clearly needs more or less, and note the reason in `PROGRESS.md`.

0. **Introduction: Why DFx** — what DFM, DFA, DFT, DFS mean; where cost is committed in the product lifecycle; cost of change through NPI phases; how to use this course.  
1. **The product development and NPI process** — concept through mass production; EVT, DVT, PVT; phase-gate reviews; who owns DFM at each stage; DFM review as a formal deliverable.  
2. **Process selection and cost drivers** — matching annual volume to process; tooling cost versus piece price; break-even analysis; cycle time, material utilization, secondary operations; a process selection map.  
3. **Tolerancing for manufacturability** — general tolerances (ISO 2768), fits (ISO 286), introduction to GD\&T (ASME Y14.5) with the datum reference frame, position, profile, flatness; tolerance stack-up by worst case and root sum square; process capability, Cp and Cpk, and why a ±0.05 mm tolerance on a molded part is a cost decision.  
4. **DFM for CNC machining** — internal corner radii, depth-to-diameter ratios, thin walls, undercuts, tool access, setups, threads, surface finish, standard stock sizes, cost drivers.  
5. **DFM for sheet metal** — bend radius versus thickness, K-factor and bend allowance, minimum flange length, hole-to-edge and hole-to-bend distances, bend relief, hemming, tabs and slots, flat pattern, coating and hardware (PEM style inserts) considerations.  
6. **DFM for injection molding** — wall thickness and uniformity, draft, ribs and bosses, undercuts and side actions, gates and weld lines, sink and warp, tolerances, mold texture and SPI finish, material selection, tooling classes and life, cost of mold changes.  
7. **DFM for casting and forging** — die casting (wall thickness, draft, ejector marks, porosity), investment casting, sand casting, forging; machining allowances; when casting beats machining.  
8. **DFM for additive manufacturing** — FDM, SLA, SLS, MJF, DMLS; orientation, supports, minimum features, anisotropy, post-processing; AM for tooling and fixtures; when AM is and is not a production process.  
9. **DFM for PCB and PCBA** — IPC standards overview, trace and space, annular rings, via types, panelization, fiducials, component orientation and spacing for reflow and wave, thermal relief, DFM checks from board houses, component selection and lifecycle risk.  
10. **Design for assembly** — Boothroyd Dewhurst approach, the three questions for part elimination, minimum part count, self-locating and self-fastening features, fastener reduction, poka-yoke, assembly sequence and access, estimated assembly time and the cost of a screw.  
11. **Design for test** — test strategy through the phases; ICT, FCT, boundary scan; test points and fixture access; test coverage and escapes; testability of mechanical assemblies (leak test, pressure test, functional checks); designing the test fixture alongside the product.  
12. **Design for service, reliability, and compliance** — serviceability and field replaceable units; design for reliability basics (derating, thermal, environmental); how regulatory requirements (UL, CE, RoHS, REACH, IP ratings, NSF/ANSI 61 where relevant) constrain design decisions early.  
13. **Materials, finishes, and joining** — material selection trade-offs by process; surface finish specification; coatings and plating (anodize, powder coat, zinc, e-coat); welding, brazing, adhesives, press fits; galvanic compatibility.  
14. **Working with suppliers and contract manufacturers** — what a good RFQ package contains; drawings versus model-based definition; the supplier DFM review and how to read the feedback; first article inspection; PPAP and control plans; ECO discipline; the relationship between BOM quality and quote quality.  
15. **Cost modeling and should-cost** — building a bottom-up cost model for a machined, a molded, and a sheet metal part; tooling amortization; the effect of volume; reading a supplier quote; where to push and where not to.  
16. **Capstone: a full DFx review** — take one defined product (a small consumer or industrial assembly you specify fully with a parts list and sketches) through a complete DFM, DFA, DFT, and DFS review, producing a scored findings list and a redesigned BOM. This module is the exam.

Plus these supporting pages: **index.html** (course landing page with outline and how to use), **glossary.html**, **references.html** (consolidated bibliography from all modules), **about.html** (author bio placeholder, license, contact placeholder).

## Structure of every module page

In this order:

1. Module number and title  
2. **Learning objectives** (3 to 6 bullets, each starting with a verb: "Calculate", "Identify", "Specify")  
3. **Why this matters** (2 to 3 paragraphs, one verified real-world example of what goes wrong)  
4. **Core content** with H2 and H3 headings  
5. **Design rules table** — a table of quantitative rules with columns for Feature, Rule of thumb, Typical value or range (metric), Why, Source. Every row cites a source.  
6. **Real-world example or case study** — verified and cited, or labeled illustrative  
7. **Common mistakes** — 5 to 8 specific mistakes, each with the consequence and the fix  
8. **Worked exercise** — a problem the learner solves with numbers (a stack-up, a break-even calculation, a wall thickness redesign, a part count reduction). Show the full worked solution in a collapsible `<details>` block.  
9. **Quiz** — 6 to 10 questions, mix of multiple choice and short numeric. Answers and one-sentence explanations in a collapsible block. Score shown on the page after the learner submits.  
10. **Key takeaways** — 5 to 7 bullets  
11. **References**  
12. Previous / next module navigation

## Site and code requirements

- Plain HTML5, CSS, and vanilla JavaScript. No frameworks, no build step, no CDN dependencies. The site must work from a `file://` open and from any static host.  
- File layout:  
    
  index.html  
    
  modules/00-introduction.html ... modules/16-capstone.html  
    
  glossary.html  
    
  references.html  
    
  about.html  
    
  assets/css/course.css  
    
  assets/js/course.js  
    
  assets/img/ (only for any SVG saved as files; prefer inline SVG)  
    
  SOURCES.md  
    
  PROGRESS.md  
    
  README.md (how to deploy, how to edit, license)  
    
- Shared header with course title and a sidebar or top navigation listing all modules. Current module highlighted. Mobile responsive; the sidebar collapses on narrow screens.  
- Progress tracking: mark a module complete when the learner passes its quiz, store in `localStorage`, show a progress bar on the index page. Wrap all `localStorage` access in try/catch so the page still works when storage is unavailable.  
- Quizzes run entirely in the browser; no server, no external service.  
- Typography: system font stack, 16 to 18 px body text, line length around 70 characters, generous spacing. Light and dark themes via `prefers-color-scheme`. Plain and readable, no decorative color boxes.  
- Every table scrolls horizontally inside its own container on narrow screens; the page never scrolls horizontally.  
- Print stylesheet so a module prints cleanly as a PDF handout.  
- All diagrams are inline SVG with `<title>` and `<desc>` for accessibility, drawn with a consistent stroke width and a two-color scheme that works in both themes. Label dimensions in mm.  
- Semantic HTML, alt text on everything, keyboard-navigable quiz controls, sufficient contrast.  
- Include a `<footer>` on every page with copyright placeholder, a license line (suggest CC BY-NC-SA 4.0 for content and MIT for code, but leave it for the author to confirm), and last-updated date.

## Working method

Work in phases and do not skip ahead.

**Phase A: Research and outline.** For each module, search for and read sources before writing anything. Produce `SOURCES.md` with at least 5 verified sources per module and a one-paragraph outline per module. Identify the real-world example you intend to use for each module and confirm you have a verifiable source for it. Present the outline and the example list, then stop and wait for the author's approval before building.

Candidate starting points to verify (do not assume these say what you expect; read them): Boothroyd, Dewhurst and Knight, *Product Design for Manufacture and Assembly*; Bralla, *Design for Manufacturability Handbook*; Ulrich and Eppinger, *Product Design and Development*; Ashby, *Materials Selection in Mechanical Design*; published DFMA case studies from Boothroyd Dewhurst Inc.; design guides from Protolabs, Xometry, Fictiv, and Hubs; IPC standards summaries; NASA Lessons Learned database; NIST manufacturing publications; published post-mortems of well-documented production problems (search for ones with credible reporting or company statements, not rumor).

**Phase B: Scaffold.** Build `index.html`, the CSS, the JS (navigation, quiz engine, progress), and one complete module (Module 6, injection molding, because it has the richest design rules) as the reference implementation. Stop and ask the author to review it in a browser before continuing.

**Phase C: Build modules.** Build the remaining modules one at a time in curriculum order. After each module: run an HTML validator if one is available (`npx html-validate` or similar), check every external link with a small script and record dead links in `PROGRESS.md`, and update `PROGRESS.md` with what is done and what is next. Commit after every module with a clear message.

**Phase D: Verification pass.** Read every module again against these checks: every numeric rule in a design rules table has a source; every citation resolves to a References entry; every References entry is in `SOURCES.md` as verified or secondary; no imperial units without a metric-first equivalent; no employer-specific content; no placeholder text; every quiz scores correctly; every exercise solution is arithmetically correct (recompute it). Write the results of this pass to `PROGRESS.md`.

**Phase E: Ship.** Write `README.md` with deployment steps for GitHub Pages and Netlify, and a short section on how to edit a module. Produce a final summary listing total word count, number of sources, number of diagrams, and any claims you were unable to verify and therefore removed or labeled.

## Style

- Practitioner voice, direct, specific, first person plural is fine ("we usually see"). No marketing language, no "in today's fast-paced world".  
- Short paragraphs. Tables for anything with numbers. Prose for reasoning.  
- Every rule of thumb comes with the reason behind it. A learner should be able to reconstruct the rule from the reason.  
- Use en dashes or commas rather than long dashes.  
- When you are uncertain, say so in the text. "Suppliers vary on this; ask yours" is better than false precision.

## When to stop and ask

Stop and ask the author when: a module's real-world example cannot be verified and you want to substitute one; you find a conflict between two credible sources on a design rule; the curriculum needs reordering; you are about to make a licensing or branding decision. Do not ask for permission to continue routine building.
