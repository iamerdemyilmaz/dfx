# PROGRESS.md

Project: *Design for Manufacturing and Assembly: From Prototype to Production* (static HTML course).
Spec: CLAUDE.md. Source register: SOURCES.md.

## Status summary

| Phase | Status | Date |
|-------|--------|------|
| A – Research and outline | Complete, approved by author | 2026-09-07 |
| B – Scaffold + reference module (06) | Complete, approved by author (4,900 words accepted) | 2026-09-07 |
| C – Remaining modules | Complete: modules 00 to 16, glossary, references, about | 2026-09-07 |
| D – Verification pass | Complete (see Phase D record) | 2026-09-07 |
| E – Ship (README, final summary) | Complete (see Phase E record) | 2026-09-07 |
| Part 8 R1 – Robotics Phase A (Modules 17 to 19) | Complete, approved by author 2026-09-11 | 2026-09-11 |
| Part 8 R2 – Module 17 | Built, verified, awaiting author review | 2026-09-11 |

Author decisions (2026-09-07): outlines and examples approved; Module 11 uses the Boeing 787 battery case (Ariane 5 kept as alternative); capstone product is the portable 12 V tyre inflator; books appear only in an unnumbered "Further reading" list, never as numbered references; licence text shown in footers as "proposed" until confirmed.

## Phase D record (2026-09-07)

Checks run over every module with `tools/verify_all.py`, `tools/checkmodule.py`, `tools/checkdashes.py`, and `tools/checklinks.py`, plus a browser pass on each module (quiz submitted with the answer key, SVG text bounds measured, mobile width 375 px checked for horizontal scroll).

| Check | Result |
|---|---|
| Every citation `[n]` resolves to a `ref-n` entry, and every entry is cited | Pass, all 17 modules (checkmodule "cites missing []; uncited []") |
| Every References URL appears in `SOURCES.md` | Pass after adding S-162 (I-Connect007 IPC-2231 article, cited in Modules 1 and 9, which had been read but not registered) |
| Every References entry has a year or "n.d." | Pass after adding years or "n.d." to 15 entries (NIST e-Handbook, Fabricator, TIGER TDS, Formlabs, IPC-7351B, NASA PD-ED-1201, NAVSEA SD-18, ASTM B633 and B117, ASME Y14.41) |
| Every design rules table row cites a source | Pass (checked when each module was built; capstone Table 12 re-checked) |
| Secondary sources labelled in References | Pass; 32 of 162 register entries are secondary and each carries a `(secondary: ...)` tag where cited |
| Imperial units only after a metric value | Pass. Two flagged strings reviewed: Module 6 "25 mm (1 inch)" and Module 15 "2.2046 lb/kg" conversion note, both metric-first |
| No employer-specific content | Pass; all cases are public and cited, all examples labelled illustrative; 17 `<!-- AUTHOR -->` placeholders left for optional personal notes and the bio/licence/contact |
| No placeholder text | Pass. "TBD" appears three times in Module 14 as deliberate content (an example of a defective BOM line), not as a placeholder |
| No em or en dashes | Pass, all pages (checkdashes) |
| Quiz scores correctly | Pass; every module's quiz submitted with the answer key in the browser scores 100 % and marks the module complete; index shows 17 of 17 |
| Exercise arithmetic recomputed | Pass; recomputed in Python when each module was built (Module 3 Q5 and Module 5 Q2 corrected then; Module 15 and 16 recomputed 2026-09-07 with results in the Phase C log) |
| SVG accessibility | Pass; 33 inline diagrams, each with `<title>` and `<desc>`, no text outside the viewBox |
| Section structure | Pass; every module has objectives, why, rules, case, mistakes, exercise, quiz, takeaways, references, pager, footer |
| Mobile layout | Pass at 375 px (no horizontal scroll) |

**External links (2026-09-07).** 221 module reference entries, 148 distinct URLs. All return 200 to a scripted request except the following, which return 403 or 406 to scripts but open normally in a browser (confirmed for each during the build): ACM Digital Library (2), ANSI webstore (6), ISO (4), CPSC, FlightGlobal, The Fabricator, GlobalSpec, Keysight, NAVSEA, NSF, CBS News (406, opened in browser 2026-09-07), and acqnotes.com (TLS handshake fails for the script; opened in browser 2026-09-07). No dead links remain: the copper.org Statue of Liberty pages (404) were replaced in Module 13, and the USTRANSCOM Better Buying Power PDF (404) was replaced in Module 15.

## Phase E record (2026-09-07)

- `README.md` written: local viewing, GitHub Pages and Netlify deployment, how to edit a module, the authoring checks, proposed licences.
- Word count: about 89,800 words of module text including tables (body prose per module in the Phase C log; every module between 3,100 and 4,900 prose words except the capstone, which is table-heavy by design).
- Sources: 162 register entries (130 verified, 32 secondary); 148 distinct URLs cited across 221 module reference entries; consolidated on `references.html`.
- Diagrams: 33 inline SVGs. Quizzes: 134 questions across 17 modules.
- Claims not verified and therefore removed or relabelled (details in the Phase A record and Phase C log): the "70 to 80 percent of cost committed in design" figure (taught as folklore, with Ulrich and Pearson's measurement instead); the "rule of ten" cost-of-change curve (attributed to Boehm, labelled as a rule of thumb); IBM Proprinter part-count figures (omitted; only the fact of the comparison is cited); a "40:1" additive claim (removed); the copper.org "rivets pulled through the skin" and "1,800 bars" Statue of Liberty details (removed when the page disappeared); Boothroyd Dewhurst outcome ranges (presented as vendor claims); mould class cycle counts, SPI finish grades, PPAP capability thresholds, and ASTM B633 class values (from public reproductions, labelled secondary); IEC 60529 digit meanings (from the IEC's own page, verified).
- Open items for the author: confirm the licences (CC BY-NC-SA 4.0 content, MIT code) shown as "proposed" in every footer, on `about.html`, and in `README.md`; replace the bio, add a contact method, and decide on the 17 optional personal-note placeholders; decide whether to keep the working title.

## Post-ship change (2026-09-07): pre-module check

At the author's request each module now opens with a three-question "Before you start" form (`form.quiz[data-pre]`) placed after the learning objectives. It is graded in the browser with the same engine and shows explanations, but the engine returns before recording progress, so only the end-of-module quiz marks a module complete. 51 questions added (3 per module); verify_all.py checks their answer options like any other question. Browser test on Module 6: wrong answers give "You got 0 of 3" with explanations shown and no progress written; correct answers give "3 of 3"; the main quiz still records completion.

## Post-ship change (2026-09-10): quizzes

At the author's request Module 0 (introduction) has no quiz and no pre-check; it is flagged `quiz: false` and the progress bar counts the 16 quizzed modules. Pre-check questions were reworded so that none asks about a particular study, case, or named source: Module 1 question 3 (phase-gate purpose), Module 12 question 1 (derating), Module 15 question 3 (should-cost), Module 16 questions 2 and 3, and several explanations. End-of-module quizzes are unchanged and still include a question on each module's cited case where relevant.

## Part 8 – Robotic systems: Phase A record (Session R1, 2026-09-11)

**Model recommendation printed at session start:** strongest model (Fable 5.1), as ROBOTICS.md specifies for R1.

**Scope:** Phase A only, for Modules 17, 18, 19 as defined in ROBOTICS.md. No HTML written. 61 sources examined; 47 registered in SOURCES.md as S-163 to S-223 (S-206 unused), of which 40 verified (PDF, page, or catalogue page read) and 7 secondary. Per module: 17 has 31 entries (26 verified), 18 has 11 (9 verified), 19 has 17 (15 verified); several are shared.

**Blocked or failed sources (recorded, not used or used as secondary):** SKF web pages (404 or blocked); Schaeffler WL 80100 manual and Molex product specifications (403 or timeout); NIOSH manual PDF (403); Springer chapter body (paywall); ODrive documentation (CDN access denied); moteus calibration guide (thin); Klüber gear grease PDF (skimmed only); Wittenstein backlash "constant over life" claim (marketing page; not used).

### Module 17 – Actuators and gear trains: DFx and failure modes (outline)

A robot joint or drive unit is a stack of tolerances: housing bore concentricity and parallelism, bearing fits and preload, gear centre distance, encoder air gap; a worked bore-to-bore stack-up links back to Module 3. Architecture choice (planetary, strain wave, cycloidal, quasi-direct drive) is framed by what the specification sheets actually define: Harmonic Drive's ratcheting torque, lost motion, wave generator L10 of 7,000 to 10,000 h and its life formula (S-170); Nabtesco's lost motion at ±3 % of rated torque, backlash at zero torque, momentary maximum of 500 % (S-171); planetary backlash classes from under 1 to 12 arcmin (S-172, S-173); and the quasi-direct drive case for backdrivability and cheap, low-ratio transmissions (S-174 to S-176, with Katz's US$300 BOM and 0.28° backlash as the honest trade). Failure modes follow the two standards that name them: gear modes per ANSI/AGMA 1010 (S-164) and bearing modes per ISO 15243 as laid out in SKF's atlas (S-168, S-169), with false brinelling from standstill vibration, true brinelling from shock, preload loss from wear (S-178), and lubrication and kinematic design failures (S-179) as the recurring early killers. Lubrication (S-185), fasteners under vibration with the Junker test (S-183, S-184), tread materials (S-187), and the manufacturing rules table (gear grade versus process, bore datum strategy, fit selection, press-fit control, preload setting per S-189, grease dosing, encoder alignment per S-192, traceability) complete the module. Diagrams: actuator cross-section with the stack labelled; torsional hysteresis curve showing lost motion and backlash.

### Module 18 – Test stations, fixtures, and jigs (outline)

The test ladder from incoming inspection to actuator end-of-line, robot end-of-line, burn-in, and audit, with each actuator test tied to what it detects: no-load torque versus speed and breakaway torque for friction and assembly damage (friction taught from the Stribeck regimes, S-200); torsional hysteresis for backlash, lost motion, and stiffness (S-170, S-171); transmission error and single-flank testing for gear quality and noise (S-198, S-199); brake holding torque, thermal rise, encoder offset calibration (S-192), leak or ingress checks. Robot end-of-line uses ISO 9283 pose repeatability as the datasheet language (S-194, S-195) and a short mission on a fixture. HALT in design and HASS in production (S-201, S-202) and MIL-STD-810 as a tailoring framework (S-203). Gauge R&R on every station links to the Six Sigma course (S-205). Fixtures: press-fit force-displacement monitoring with the curve as a gauge (S-196, S-197); alignment and parallelism checks; preload setting fixtures (S-189); 3-2-1 location and fixture calibration. Diagrams: Stribeck curve; press-fit curve with good and bad signatures; test ladder.

### Module 19 – Building the fleet (outline)

What changes from ten to a thousand units: harness and connector wear (mating cycle ratings, S-193), battery pack safety (S-214, S-215), serviceability and modular drive units, traceability per serial with test data (Module 14's ECO discipline at fleet scale). The safety map before DVT: ISO 3691-4:2023 for driverless trucks including AMRs (S-207), ANSI/RIA R15.08-1 with IMR Types A, B, C (S-208), UL 3100 for automated mobile platforms (S-209), ISO 10218-1:2025 and ISO/TS 15066 for manipulators and collaborative operation (S-210, S-211), ISO 13849-1 performance levels and IEC 61508 (S-212, S-213), with OTTO Motors' published third-party assessment as the example of what a manufacturer states (S-223). The assembly line: takt from demand (S-217), line balancing procedure and efficiency (S-218), MODAPTS and MOST as predetermined time systems and when each fits (S-219, S-220), discrete event simulation and what it answers (S-221), NIOSH lifting limits for heavy modules (S-216), kitting and poka-yoke, and the economic case for automating a station. Diagram: line balance chart. Amazon's fleet numbers (S-222) and the Kiva drive unit patent (S-182) show what a fleet-scale mechanism looks like in public documents.

### Real-world examples intended, with sources

- Module 17: ISS Solar Alpha Rotary Joint bearing failure and recovery, NASA/TP-2011-217116 (S-179); Space Shuttle body flap actuator bearings, wear leading to preload loss, NASA/TM-2008-215057 (S-178); Curiosity drill feed mechanism stall after brake release, JPL 2022 (S-180); why quasi-direct drive was chosen over high-ratio gearing, MIT Cheetah and ODRI papers and Katz thesis (S-174 to S-176); grid storage robot mechanics from the AutoStore v Ocado judgment (S-181).
- Module 18: UR5e datasheet quoting ISO 9283 repeatability (S-195); press-fit monitoring practice from Promess and Sciemetric (S-196, S-197); gear noise and ghost frequencies in production, Gravel 2013 (S-198); Harmonic Drive and Nabtesco hysteresis-curve definitions as the basis of an end-of-line torsional test (S-170, S-171).
- Module 19: OTTO Motors third-party safety assessment to R15.08 (S-223); Amazon's more than one million robots since 2012 and the Kiva drive unit patent (S-222, S-182); gearbox assembly line balancing with FlexSim (S-221, abstract only).

### Claims I could not verify to the standard required, and how they will be handled

1. Gear accuracy grade achievable by process (hobbing, shaving, honing, grinding): only vendor blogs found. Will be given as "commonly quoted ranges" with ISO 1328-1 named as the class system, labelled secondary (S-191), unless an AGMA or Gear Technology source is found in R2.
2. NIOSH load constant 23 kg and multiplier formulas: manual PDF blocked; secondary until read (S-216).
3. MODAPTS 1 MOD = 0.129 s and MOST TMU = 0.036 s: from summaries and Wikipedia; labelled secondary (S-219, S-220).
4. Connector durability of 30 mating cycles: Molex documents unreachable by script; secondary (S-193).
5. HALT origin with Gregg Hobbs in 1988: secondary (S-202).
6. Curiosity drill foreign-object-debris hypothesis: press reports only; the JPL abstract (brake, high-drag state) is what will be cited.
7. Bearing fit rules (tight fit on the ring under circumferential load): Schaeffler manual blocked; secondary until read (S-188).
8. Wittenstein's "backlash constant over service life": marketing statement, not used.
9. Tesla Optimus talks, Ocado and Locus ramp figures: not pursued; Amazon's own published count is the fleet-scale figure used.
10. ODrive encoder and anti-cogging calibration: documentation inaccessible; encoder offset will be taught from the MathWorks example (S-192) and cogging described qualitatively.

**Resume here (Part 8):** Phase A approved 2026-09-11. Session R2 built Module 17 (`modules/17-actuators-gear-trains.html`, linked, published); awaiting the author's review. Next is Session R3: build Module 18 (strongest model) using S-194 to S-205 plus the shared actuator sources, then stop for review; then R4 for Module 19 (mid-tier acceptable) and R5 for index text, glossary, references page, README, and the verification pass. Numbering: Module 16 remains the capstone of the process modules; the index gets a "Part 8: Robotic systems" heading; `course.js` gets three new entries with `built: false` until each module is complete.

## Phase C log

Author instruction (2026-09-07): no em or en dashes anywhere in the course, including numeric ranges. `tools/checkdashes.py` enforces this; `tools/checkmodule.py` reports word count, citation cross-check, SVG accessibility, dashes, placeholders, and quiz count.

| Module | Date | Body words | Refs | Diagrams | Quiz Qs | Link check | Notes |
|---|---|---|---|---|---|---|---|
| 00 Introduction | 2026-09-07 | 3,623 | 12 | 1 | 7 | 7 OK; 5 return 403 to automated requests (ACM ×2, ANSI webstore, CPSC, FlightGlobal) but were opened successfully during research | Boehm & Basili 2001 upgraded to verified after reading the UMD-hosted PDF. |
| 01 NPI process | 2026-09-07 | 3,125 | 7 | 1 | 7 | 8 OK | IPC-2231 description limited to what the readable trade-press source states. |
| 02 Process selection | 2026-09-07 | 3,190 | 17 | 2 | 8 | 16 OK; CBS News returns 406 to scripts (opened during research; secondary) | Exercise arithmetic recomputed in Python. |
| 03 Tolerancing | 2026-09-07 | 4,173 | 16 | 2 | 8 | 13 OK; ISO catalogue pages (3) return 403 to scripts, opened during research | Simply Bearings page used only for shaft deviations because its H7 value conflicts with IT7 = 21 µm; noted in SOURCES S-134. Exercise and quiz arithmetic recomputed. |
| 04 CNC machining | 2026-09-07 | 3,847 | 12 | 1 | 8 | 12 OK | Comet 1 (Hansard + inquiry summary) used for stress concentration; Apple unibody as the case. |
| 05 Sheet metal | 2026-09-07 | 3,674 | 10 | 2 | 8 | 7 OK; CPSC, ISO, The Fabricator return 403 to scripts | PEM handbook (PDF) replaced the blocked PEM FAQ as the hardware source. |
| 06 Injection molding | 2026-09-07 | 4,904 | 14 | 3 | 8 | 14 OK | Length accepted by author. |
| 07 Casting and forging | 2026-09-07 | 4,080 | 10 | 2 | 8 | 10 OK | NADCA draft formula recovered as D = √L / C (the PDF text lost the root sign; verified against NADCA's own 1 in example giving about 2°). Sioux City fan disk (FAA Lessons Learned, read in browser) as the inspection lesson; Tesla casting as the case. |
| 08 Additive | 2026-09-07 | 3,281 | 13 | 2 | 8 | 12 OK; ISO catalogue 403 to scripts | Machine-specific rule variance (Formlabs Form 2 vs Form 3) used as the cautionary example; GE nozzle as the case. |
| 09 PCB and PCBA | 2026-09-07 | 4,272 | 16 | 2 | 8 | 14 OK; ANSI webstore (2) and GlobalSpec return 403 to scripts | Trace-width arithmetic recomputed in Python; Galaxy IV tin whisker as the case. |
| 10 Design for assembly | 2026-09-07 | 3,851 | 9 | 2 | 8 | 9 OK | IBM Proprinter numbers deliberately omitted (unverifiable); IDEXX and L3Harris cases used, labelled vendor/practitioner-published. |
| 11 Design for test | 2026-09-07 | 3,838 | 9 | 2 | 8 | 8 OK; Keysight blog 403 to scripts (read during research) | 787 battery (NTSB) as the case; Ariane 5 as the second example; escape and leak arithmetic recomputed. |
| 12 Service, reliability, compliance | 2026-09-07 | 4,032 | 16 | 2 | 8 | 13 OK; ANSI, NAVSEA, NSF return 403 to scripts | Directive 2024/1799 and the Blue Guide page read and upgraded to verified; IEC IP-ratings page read in browser. |
| 13 Materials, finishes, joining | 2026-09-07 | 4,313 | 18 | 2 | 8 | 18 OK | The copper.org "Reclothing the First Lady of Metals" pages are gone (404); ref-2 replaced with the live CDA press release (1,500 saddles, 300,000 rivets, verified). The "rivets pulled through the skin" and "1,800 bars replaced" claims, which rested only on search excerpts of the dead page, were removed. Brazing clearance wording aligned to Lucas-Milhaupt. |
| 14 Suppliers and CMs | 2026-09-07 | 3,870 | 11 | 2 | 8 | 10 OK; ANSI webstore (APQP listing) 403 to scripts, page known to exist | AS9102 Rev. C (June 2023) via High QA summary; ASME page lists Y14.41-2026 as current, course says 2019 edition in wide use and notes 2026. "TBD" appears three times as deliberate content (an example of a bad BOM line), not as a placeholder; the placeholder checker flags it. Hyatt facts from the TAMU ethics PDF (NBS quotes, dates, hearing findings) and the NIST page (113 dead, 186 injured, probable cause). |
| 15 Cost modeling and should-cost | 2026-09-07 | 4,166 | 12 | 2 | 8 | 11 OK; acqnotes.com rejects scripted fetches (TLS/anti-bot) but was read in the browser | Ulrich & Pearson PDF re-read for the Krups scenario, 48 %/31 % ranges, price-versus-cost pairs, and purchased-parts share. Hubs CNC rate table and moulding cost bands read on the live pages. Boothroyd Dewhurst sheet metal costing page used for imperial reference values, converted to metric in Table 1. FAR 15.407-4 read and upgraded to verified. BBP 2.0 memo PDFs (USTRANSCOM 404, OSD 403) replaced by the AcqNotes BBP 3.0 list and a DoD News article for the 2010 origin. Exercise arithmetic recomputed in Python (component rounding gives $10.48 sheet metal, exact $10.47; break-evens 528/349/3,168 with rounded figures). |
| 16 Capstone | 2026-09-07 | about 2,800 prose words plus 12 tables | 19 | 3 | 8 | 18 OK; Keysight 403 to scripts (known) | Body prose is below the 2,500 to 4,500 target by design: the module is the exam and its content is the specification, baseline BOM, four findings tables, the consolidated scored list, and the redesigned BOM (12 tables, about 2,600 words of table text). Product, dimensions, allowances, and costs are labelled illustrative. All rules cite the module and source that introduced them; no new sources. Arithmetic (IPC-2221 trace width, NADCA draft, DFA indices, part and fastener counts) recomputed in Python. |
| 17 Actuators and gear trains (Part 8) | 2026-09-11 | 5,010 | 29 | 2 | 8 (+3 pre-check) | 23 OK; ISO (5), ANSI webstore, MathWorks return 403 to scripts, all read in the browser or verified via search | Body text over the 4,500 target by about 500 words because ROBOTICS.md asks this module to cover architecture choice, specification reading, gear and bearing failure modes, lubrication, brakes, fasteners, wheels, frames, and a manufacturing rules table; kept rather than cut, flagged for the author. Exercise arithmetic (equivalent load, L10, stack-up, ratio table) computed in Python. New navigation feature: a `part` field on a module entry renders a "Part 8: Robotic systems" heading in the sidebar and the index list; Modules 18 and 19 registered with `built: false`. |

Links that return 403 to scripts are recorded here rather than as dead; they will be re-checked by hand in Phase D.

## Phase B record (2026-09-07)

Built: `index.html`, `assets/css/course.css`, `assets/js/course.js`, `modules/06-injection-molding.html`, `tools/checklinks.py`, `.claude/launch.json` (local preview server).

- Navigation is generated by `course.js` from a single module list; only modules with `built: true` are linked. Unbuilt modules appear as plain text with no "coming soon" wording. Glossary, references, and about pages are listed but unlinked until built.
- Quiz engine: radio and numeric questions, per-question verdicts and explanations, pass mark 70 %, progress saved to `localStorage` under `dfx-course-progress` inside try/catch. Progress bar and per-module status on the index.
- Module 6 body text: 4,904 words excluding tables, quiz, references, and diagram text (target 2,500–4,500). Over target by about 400 words because it is the reference implementation and the richest rules set; it covers eleven H2 topics from the spec. Author may ask for trimming.
- Module 6 has 14 numbered references, all links returned HTTP 200 on 2026-09-07 (`tools/checklinks.py`). Three inline SVG diagrams, each with `<title>` and `<desc>`.
- HTML validation: `npx html-validate` is not available on this machine (no Node). Validation was done by structural checks in Python (citation/reference cross-check, SVG accessibility elements) and browser rendering. Install Node or use the W3C validator for a formal pass in Phase D.
- Books (Boothroyd et al., Bralla) appear under "Further reading" only, per author decision.


---

## Phase A record (2026-09-07)

### Method

Every candidate source was searched for and then read (web page, PDF text extraction, or publisher catalogue page) before being entered in SOURCES.md. 128 sources were registered (S-01 to S-128). Counts by status:

| Status | Count | Notes |
|--------|-------|-------|
| verified | 95 | Read directly. Includes 17 PDFs read in full or in the relevant sections. |
| secondary | 36 | Mostly printed books (Boothroyd et al., Ulrich & Eppinger, Bralla, Ashby, Swift & Booker, Fischer, Machinery's Handbook, Shingo, Cooper), paid standard bodies, and a few web pages that blocked automated fetching but whose content was confirmed through search excerpts or a second source. |
| unverified | 0 | Not permitted in the course. |

Every module has at least five verified sources. Books are registered as secondary because I cannot read them; where the course states a specific claim from a book, that claim is routed through a verified source that quotes the book with page numbers (for example the DFMA Forum papers S-88 and S-89 quote Boothroyd's DFA index and the 2.93 s / 3 s ideal assembly time).

### Candidate claims and examples that failed verification (not to be used as stated)

| Claim / example | Finding | Decision |
|-----------------|---------|----------|
| "70 to 80 percent of product cost is committed during design" | Ulrich & Pearson (S-20) trace it to 1980s trade-press tables (Miller 1988) and call it folklore; their coffee-maker data show design range 48 % vs manufacturing-system range 31 % under stated assumptions. | Teach as a widely cited rule of thumb, cite Ulrich & Pearson as the honest test of it, no fake precision. |
| "Rule of ten" for cost of change | Traceable to Boehm 1976/1981 software data (5:1 to 100:1). No manufacturing-specific dataset found. | Teach as a heuristic attributed to Boehm; state that the hardware version is by analogy. |
| IBM Proprinter 152 → 32 parts, 1866 → 170 s | Numbers appear only in third-party summaries; dfma.com history page names the 1987 comparison but gives no numbers; Boothroyd's book not readable. | Do not quote the numbers. Use IDEXX (S-86) and L3Harris (S-88) cases, which are verified, and mention Proprinter qualitatively as the historical origin. |
| Airbus A380 "CATIA V4 vs V5" as root cause | Widely reported in trade press; Airbus's own statement (S-25) blames the late 3D digital mock-up and learning curve, not a software version. | Use Airbus's wording; mention the CATIA version story only as press reporting. |
| LEGO "0.002 mm" or "0.005 mm tolerance" | LEGO's own history page says ABS allowed moulding "to an accuracy of 1/200 mm" (0.005 mm) in 1963; no official page gives 0.002 mm. | Quote only the 1/200 mm statement, attributed to LEGO's history page. |
| Tesla "40 % rear underbody cost saving", "300 robots removed" | Found only in secondary reporting without a Tesla document. | Omit. Use Musk's Q1 2020 call quote (70 parts → 1) via S-64, labelled secondary. |
| Samsung Note7 "200,000 devices and 30,000 batteries tested" | Appears in press summaries of Samsung's presentation; Samsung's press-release text I could read does not include it. | Label secondary if used; the verified facts are date, cause (batteries), third parties, and 8-point check. |
| ICT probe pitch / test pad rules "from IPC" | No IPC document read; values are from Sierra Circuits' DFT page (S-92). | Attribute to Sierra Circuits, not IPC. |
| Cpk ≥ 1.33 / Ppk ≥ 1.67 "required by PPAP" | Confirmed only via secondary summaries of PPAP 4th ed. | Present as the AIAG PPAP default acceptance criteria, labelled secondary, with "confirm with your customer". |
| MIL-STD-889 "0.15 / 0.25 / 0.50 V anodic index" rule | Current MIL-STD-889D (S-114) uses a corrosion-rate ranking instead; the voltage rule is from superseded revisions. | Teach the current D methodology; mention the old rule as legacy. |
| PEM minimum sheet thickness and hole tolerance | FAQ page blocked; values from search excerpt only. | Re-check against PEM catalogue during Phase C before use. |

### Fetch failures to retry in Phase C (content currently secondary)

FlightGlobal (S-24), PEM FAQ (S-53), The Fabricator (S-51), NSF (S-105), ECHA candidate-list page, ANSI blog pages, Justia/CourtListener Hyatt decision, SAE AS9102C page (S-122), Repairer Driven News (S-65), Samsung US newsroom (timed out). If a retry fails, the entry stays secondary and is labelled so in the module References.

### Standards revision notes

- ASME Y14.5-2018 is current and reaffirmed 2024 (R2024). ASME's site also lists a Y14.41-2026 edition; the course will cite Y14.41-2019 as the widely available edition and note the 2026 release exists. Verify before Module 14 is written.
- IPC-2231 has an A revision (IPC-2231A); cite IPC-2231A as current, 2019 as first release.
- IPC-2221: a C revision is listed by some resellers; IPC's own shop still lists Revision B (2012). Re-check before Module 9 is written.
- ASTM B117 current is B117-26 (per ANSI blog, secondary); B633 current is B633-23 (verified).
- IEC 60529 current consolidated edition is 2.2 (2013). IEC 60335-1 current is Ed. 6.0 (2020).
- MIL-STD-889D (2021) supersedes 889C (2016).

---

## Module outlines and chosen real-world examples

Target 2,500–4,500 words body text each. Word-count deviations will be recorded here as modules are built.

**Module 0 – Introduction: Why DFx.** Defines DFM, DFA, DFT, DFS and the umbrella term DFx; explains where cost becomes locked in across concept, detail design, tooling, and ramp; tests the "80 % of cost is set in design" folklore against Ulrich and Pearson's coffee-maker study (S-20, S-21) and presents the "rule of ten" as Boehm's software heuristic applied by analogy (S-22, S-23); closes with how to use the course. *Real-world example:* the Airbus A380 wiring-harness delay of 2006, in which late integration of design data forced rework on installed harnesses and cost EADS a stated €2.8 bn plus the €2 bn already announced (S-25, S-24). *Exercise:* compute the cost of a late change under three phase-multiplier assumptions and see how sensitive the answer is.

**Module 1 – The product development and NPI process.** Walks concept → EVT → DVT → PVT → mass production, mapping the hardware-industry stage names (S-27) onto formal phase-gate frameworks (NASA life cycle reviews S-28; Stage-Gate S-29, S-30); defines what "DFM review as a formal deliverable" means at each gate, who owns it, and what tooling maturity is expected at each build. *Real-world example:* Tesla's Model 3 ramp of 2017–2018, using Musk's own statements that excessive automation was a mistake and that the overly complex conveyor system was removed (S-31, S-32). *Exercise:* build a gate checklist for a given part and decide which findings block DVT exit.

**Module 2 – Process selection and cost drivers.** Matches annual volume to process using tooling cost versus piece price and break-even analysis; covers cycle time, material utilisation, and secondary operations; presents a process-selection map built from verified supplier bands (Hubs tooling classes and volumes S-10; NADCA's own comparison of die casting with investment casting, powder metal, and plastics S-33; CNC cost drivers S-11, S-36; stock sizes S-12) with Ashby and Swift & Booker as further reading (S-04, S-05). *Real-world example:* Ford's 2015 F-150 move to an aluminium-alloy body, cutting roughly 230–320 kg (500–700 lb), as a material-and-process decision made at very high volume (S-34, S-35). *Exercise:* break-even between machining, soft tooling, and hard tooling for a housing at three volumes.

**Module 3 – Tolerancing for manufacturability.** General tolerances (ISO 2768-1 and -2, S-15, S-37–S-39), ISO 286 IT grades and preferred fits (S-16, S-40, S-41), an introduction to GD&T under ASME Y14.5-2018 with datum reference frames, position, profile, and flatness (S-14), the ISO 8015 independency principle (S-17), worst-case and RSS stack-ups (S-42), and process capability with Cp/Cpk and the reject-rate table (S-13). Explains why ±0.05 mm on a moulded part is a cost decision using Protolabs' resin tolerance of ±0.002 mm/mm (S-06). *Real-world example:* the Hubble primary mirror, where a 1.3 mm spacing error in the test fixture (needed to be correct to 10 µm) went undetected because two independent tests that showed the error were discounted (S-43, S-44). *Exercise:* a five-part stack-up solved worst-case and RSS, then converted to a Cpk requirement.

**Module 4 – DFM for CNC machining.** Internal corner radii versus pocket depth, depth-to-diameter limits for pockets and holes, thin walls, undercuts, tool access and setups, threads, surface finish specification (ASME B46.1, S-48), standard stock sizes and blank allowances, and the cost drivers (S-07, S-09, S-11, S-12, S-36). *Real-world example:* Apple's 2008 unibody MacBook, in which a multi-part enclosure was replaced by one machined part, as a case where a high-cost process was chosen deliberately for a system benefit (S-46). *Exercise:* redesign a pocketed bracket to cut cycle time by changing radii, depths, and setups.

**Module 5 – DFM for sheet metal.** Bend radius versus thickness, K-factor and bend allowance with the full formula (S-50, S-51), minimum flange length, hole-to-edge and hole-to-bend clearances expressed in multiples of thickness (S-08, S-49), bend relief, hems, tabs and slots, flat-pattern development, coatings, and self-clinching hardware including PEM's centreline-to-edge rule and bulging failure (S-52, S-53). *Real-world example:* the 2016 CPSC recall of about 2.8 million Samsung top-load washers whose sheet-metal tops could detach from the chassis under vibration, remedied by reinforcing the top (S-54). *Exercise:* compute a flat pattern for a three-bend bracket and check every feature clearance.

**Module 6 – DFM for injection molding (reference implementation).** Wall thickness and uniformity by resin, draft including textured surfaces, ribs and bosses, undercuts and side actions, gates, weld lines, sink and warp, tolerances and DIN 16742/ISO 20457 tolerance groups, SPI finish grades, material selection, SPI mould classes 101–105 and tool life, and the cost of mould changes (S-06, S-10, S-55–S-59). *Real-world example:* two verified items rather than one weak one: LEGO's statement that ABS enabled moulding to 1/200 mm in 1963 (S-58) to show what precision moulding costs and demands, and Ulrich & Pearson's observation that a coffee-maker maker hid sink marks on a cheap polypropylene tank with a ribbed pattern instead of switching to a resin two to three times more expensive (S-20, S-21). *Exercise:* wall-thickness and rib redesign of a housing to remove sink and reduce cycle time.

**Module 7 – DFM for casting and forging.** Die casting (wall thickness, the NADCA draft formula and constants, ejector marks, porosity, standard versus precision tolerances, S-33), investment casting (S-63), sand casting (S-61, S-62), forging (draft, parting line, fillet and corner radii, net-shape limits, S-60), machining allowances, and when casting beats machining. *Real-world example:* Tesla's Model Y rear underbody, where Musk stated a 70-part stamped assembly would become one high-pressure die casting (S-64, S-65; labelled secondary as press reports of Tesla statements). *Exercise:* apply the NADCA draft formula and tolerance build-up to a die-cast bracket and compare with a machined alternative.

**Module 8 – DFM for additive manufacturing.** The seven ISO/ASTM 52900 process categories (S-66); design rules for FDM, SLA, SLS, MJF, and DMLS with side-by-side supplier values showing how much rules vary by machine (S-18, S-19, S-67–S-73); orientation, supports, anisotropy, post-processing, AM for tooling and fixtures, and when AM is and is not a production process. *Real-world example:* GE Aviation's LEAP fuel nozzle tip, 20 brazed and welded pieces consolidated into one printed part, 25 % lighter and 5× more durable, with more than 33,000 produced by late 2018 (S-74). *Exercise:* orient and support a bracket for DMLS and estimate the effect of build height on cost.

**Module 9 – DFM for PCB and PCBA.** IPC standards overview (IPC-2221B, IPC-A-610H, IPC-2231A, IPC-7351B, S-75–S-78), trace and space, annular rings, via types and aspect ratios, panelisation and rails, fiducials (S-80), component orientation and spacing for reflow and wave (S-81), thermal relief, board-house DFM checks and typical minima (S-79, S-82), component selection and lifecycle risk (S-85). *Real-world example:* the 1998 loss of the Galaxy IV satellite, attributed by the manufacturer to tin whiskers shorting a tin-plated relay in the control processor, as documented by NASA (S-83, S-84). *Exercise:* size a power trace with the IPC-2221 current formula and lay out test-friendly fiducials and rails on a panel.

**Module 10 – Design for assembly.** The Boothroyd Dewhurst method, the three questions for part elimination, theoretical minimum part count, the DFA index with the 2.93 s ideal time, handling and insertion penalties, fastener reduction and the real cost of a screw, self-locating and self-fastening features, poka-yoke (S-90), and assembly sequence and access (S-86–S-89, S-01). *Real-world example:* the IDEXX Catalyst Dx access door redesign, 183 → 31 parts, 63 → 0 fasteners, 45 → 11 minutes (S-86), plus the L3Harris electronics-enclosure worked case (S-88); both are vendor-published and will be labelled as such. *Exercise:* DFA index before and after on a six-part assembly.

**Module 11 – Design for test.** Test strategy through EVT/DVT/PVT; ICT, functional test, and boundary scan (IEEE 1149.1-2013, S-91, S-93); test points, probe pitch, and fixture access (S-92); test coverage and escapes; testability of mechanical assemblies with pressure-decay and hydrostatic leak testing (S-94, S-95); designing the fixture alongside the product. *Real-world example:* the 2013 Boeing 787 APU battery fire in Boston, where the NTSB found the certification tests did not consider the most severe internal-short case and cell manufacturing inspection could not reliably detect defects (S-96). *Alternative if the author prefers a non-aviation case:* Ariane 5 flight 501 (S-97). *Exercise:* build a test-coverage matrix and decide which nets and which mechanical checks must be reachable.

**Module 12 – Design for service, reliability, and compliance.** Serviceability and field-replaceable units, the EU right-to-repair directive (S-107), design-for-reliability basics with NASA derating factors (S-98, S-99) and IEC 60068 environmental tests (S-110), and how regulatory requirements constrain design early: CE marking and the Blue Guide (S-106), IEC 60335-1 (S-101), RoHS substances and limits (S-102), REACH Article 33 (S-103), IP ratings under IEC 60529 (S-100), and NSF/ANSI/CAN 61 and 372 for potable-water contact (S-104, S-105). *Real-world example:* the Galaxy Note7 recall, where Samsung and three independent bodies identified battery defects from two suppliers and introduced an eight-point battery safety check (S-108, S-109). *Exercise:* derate a power board's components and classify an enclosure to an IP code.

**Module 13 – Materials, finishes, and joining.** Material selection trade-offs by process (S-04), surface finish specification, anodising types (S-111), zinc plating classes (S-112), powder coat and e-coat (S-118), salt-fog testing (S-113), welding, brazing, adhesives, press fits (S-47), plastics joining (S-117), and galvanic compatibility under MIL-STD-889D (S-114). *Real-world example:* the Statue of Liberty, whose iron armature corroded galvanically against the copper skin once the shellac-and-asbestos insulation failed, and was replaced in the 1981 to 1986 restoration with a PTFE-isolated stainless steel armature (S-115; S-116 now the CDA press release giving the saddle and rivet counts). *Exercise:* choose a fastener, plating, and isolation scheme for an aluminium-to-steel joint in a humid environment.

**Module 14 – Working with suppliers and contract manufacturers.** What a good RFQ package contains (S-119), drawings versus model-based definition under ASME Y14.41 (S-123), reading a supplier DFM review, first article inspection under AS9102C (S-122), PPAP elements and levels and APQP control plans (S-45, S-120, S-121), ECO discipline, and the link between BOM quality and quote quality. *Real-world example:* the 1981 Hyatt Regency walkway collapse, where a fabricator's change from one continuous hanger rod to two rods, made to simplify fabrication, doubled the load on a connection and was approved on shop drawings without being recalculated (S-124, S-125). *Exercise:* review a supplier's DFM feedback list and classify each item as accept, negotiate, or reject with reasons.

**Module 15 – Cost modeling and should-cost.** Bottom-up cost models for a machined, a moulded, and a sheet-metal part; tooling amortisation; the effect of volume; reading a quote; where to push and where not to; should-cost as defined in FAR 15.407-4 and DoD Better Buying Power (S-126, S-127). *Real-world example:* Ulrich & Pearson's cost model of 18 coffee makers, including the Krups 178 scenario in which redesign to the Rowenta architecture cut estimated cost from $14.54 to $9.72 in the same plant, and to $4.98 with plant and design changes together (S-20, S-21). *Exercise:* build the three cost models in a table and compute break-even volumes.

**Module 16 – Capstone: a full DFx review.** An illustrative product fully specified by the course (parts list, sketches, target volume 20,000 units/year, target cost) taken through DFM, DFA, DFT, and DFS reviews producing a scored findings list and a redesigned BOM. **Proposed product: a portable 12 V DC tyre inflator** with two moulded housing halves, a die-cast aluminium cylinder head, a machined piston and crank, a sheet-metal motor bracket and heat shield, a PCBA with pressure sensor and display, a membrane keypad, purchased motor, hose and chuck, and about 20 fasteners. It exercises every process module without touching HVAC, water heating, or thermal storage. **Alternative:** a handheld digital anemometer (smaller, fewer processes). Author to choose.

---

## Decisions needed from the author before Phase B

1. Approve the module outlines and real-world examples above, or name substitutions.
2. Module 11: Boeing 787 battery (NTSB) or Ariane 5 (ESA) as the primary example.
3. Module 16: tyre inflator or anemometer as the capstone product.
4. Confirm that books may appear in References labelled "secondary (not read directly)", or ask me to drop book citations entirely and keep them as unnumbered further reading.
5. Licence: proposed CC BY-NC-SA 4.0 for content and MIT for code (spec suggestion), to be confirmed before about.html is written.
