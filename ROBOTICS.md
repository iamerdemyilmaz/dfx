# ROBOTICS.md: Part 8 of the DFx course, robotic systems

How to use: this file sits at the repo root next to `CLAUDE.md`. Every rule in `CLAUDE.md` still applies: verified sources only, no invented case studies, no employer content, metric units, the module page structure, the verification tools, and the token discipline. This file adds three modules and the rules specific to them. Kick it off with the prompt at the bottom.

## Why

The course covers DFx by process. It does not cover the product most of its readers are increasingly asked to build: a robot. Robots concentrate every DFx problem in one place, an actuator: precision gears, bearings with preload, a motor, an encoder, a brake, seals and grease, a harness, a controller, all inside a housing whose bore alignment decides whether the assembly lasts a year or a month. Then the company has to build hundreds of them, test each one, and certify the machine they go into. Part 8 teaches that, with the same standard of evidence as the rest of the course.

## Rules specific to Part 8

1. **No target company.** The modules are written for "a company building mobile or manipulating robots at fleet scale". Never name, describe, or imply the internal practices of any specific private company as a design target. Public companies and products may be used as examples only when the fact is public and cited: a published patent, a datasheet, a standard, a paper, a court filing, a published teardown, a company's own published talk or blog. Never write "companies like X need".
2. **Nothing from the author's interviews or conversations with companies.** Same rule as employer content in `CLAUDE.md`. Leave `<!-- AUTHOR: -->` placeholders where a personal note might go.
3. **Named products stay factual and cited.** A statement like "strain wave gears lose torsional stiffness under repeated overload" is fine with a source. A statement about a named manufacturer's field failure rate is not, unless it is in a published document you read.
4. **Numbers are ranges from sources, not design values.** Backlash classes, gear accuracy grades, bearing L10 formulas, seal drag torque, tread hardness, and similar figures come from standards, catalogs, and papers with citations. Where sources vary, give the range and say so.

## Candidate sources to verify, not assume

Standards and handbooks: ISO 1328 (cylindrical gear accuracy), AGMA 2001 and ISO 6336 (gear rating), AGMA 1010 (gear failure nomenclature, the authoritative catalog of gear failure modes), ISO 281 (bearing L10 life), ISO 15243 (bearing damage classification), ISO 286 (fits), ISO 9283 (robot performance criteria and test methods: repeatability, accuracy), ISO 9409 (robot mechanical interfaces), ISO 10218 (industrial robot safety), ISO/TS 15066 (collaborative robots), ISO 3691-4 (driverless industrial trucks), ANSI/RIA R15.08 (industrial mobile robots), UL 3100 (automated mobile platforms), ISO 13849 (safety-related control), IEC 61508, IEC 60034 (rotating machines), DIN 65151 and ISO 16130 (Junker vibration loosening test), Shigley's *Mechanical Engineering Design*, Dudley's *Handbook of Practical Gear Design*, Harris and Kotzalas *Rolling Bearing Analysis*.

Actuator literature: Harmonic Drive and Nabtesco published catalogs and engineering data (ratcheting, lost motion, rated versus momentary peak torque, life curves); Wittenstein and Neugart planetary catalogs (backlash classes, efficiency, run-in); Wensing et al. 2017 on the MIT Cheetah proprioceptive actuator; Grimminger et al. 2020, Open Dynamic Robot Initiative; Seok et al. on the Cheetah leg; Katz's MIT Mini Cheetah actuator thesis; published moteus and ODrive documentation on encoder calibration and cogging; Tesla's published Optimus talks for actuator architecture (only what was said publicly); NASA Lessons Learned and NTRS reports on actuator, gear, and bearing failures on flight hardware; published Mars rover actuator and drill anomaly reports; Kiva Systems, AutoStore, Ocado, Exotec, and Attabotics patents and public product data for lattice and grid storage robots (drive units, wheel change mechanisms, lifting, charging); the Ocado versus AutoStore litigation record as a public description of grid robot mechanics; published teardowns of collaborative robot joints; SKF, Schaeffler, and NSK published bearing failure atlases and mounting guides; Klüber and similar published grease selection guides; polyurethane wheel manufacturers' published tread data.

Manufacturing and test: published gearbox end-of-line test literature (back-to-back or four-square rigs, torque ripple, transmission error, no-load torque signatures, acoustic testing); published press-fit force-displacement monitoring literature; encoder alignment and calibration papers; HALT and HASS literature (Hobbs); MIL-STD-810 for vibration and shock methods; published MES and traceability practice in automotive; time study literature for MODAPTS and MOST (Zandin, *MOST Work Measurement Systems*); line balancing and takt time (any standard IE text, cited); discrete event simulation of assembly lines (published FlexSim case studies or academic papers).

## The three modules

Numbering continues after the capstone; Module 16 stays the capstone of the process modules and the index page gets a "Part 8: Robotic systems" heading.

### 17. Actuators and gear trains: DFx and failure modes

Learning objectives around: choosing between planetary, strain wave, cycloidal, and direct or quasi-direct drive for a given torque, speed, backlash, and cost target; reading an actuator specification (rated, peak, momentary peak torque; backlash and lost motion; torsional stiffness; efficiency; L10); the anatomy of a robot joint or drive unit as a manufacturing problem.

Core content: the actuator as a stack of tolerances (housing bore concentricity and parallelism, bearing fits and preload, gear center distance, encoder air gap) with a worked stack-up; gear failure modes per AGMA 1010 (pitting, micropitting, scuffing, wear, tooth root fatigue, and the misalignment edge loading that causes most of them early); bearing failure modes per ISO 15243 (brinelling from shock and transport, false brinelling from vibration, spalling, preload loss, contamination); strain wave specifics (flexspline fatigue, ratcheting under overload, wave generator bearing wear, lost motion growth over life); cycloidal and planetary specifics (pin and roller wear, carrier misalignment, load sharing); lubrication (fill quantity, leakage paths, grease degradation, temperature); motor and electronics failures relevant to the mechanical engineer (winding overtemperature, magnet demagnetization, encoder contamination, cable fatigue at moving joints, connector wear); brakes (wear, glazing, holding torque drift); fasteners under vibration (Junker test, thread locker, torque control); wheels and tread (wear, delamination, flat spotting under sustained load); frames and welds (fatigue at brackets); batteries and charging contacts as mechanical wear items.

Manufacturing challenges as a design rules table: gear grade versus process (hobbed, shaved, ground, powder metal, molded) and cost; bore machining datum strategy (link to Module 3 and the GD&T course); bearing fit selection for rotating versus stationary ring and thermal growth; press-fit process control; preload setting methods; grease dosing; run-in; encoder mounting; magnet handling; cleanliness; heavy component handling; traceability of every serialized part.

Real-world examples: at least three verified (candidates: a NASA flight actuator anomaly report; a published rover drive or drill failure; a published grid storage robot mechanism from a patent or the litigation record; the MIT Cheetah or ODRI actuator papers on why quasi-direct drive was chosen over high-ratio gearing).

Exercise: pick an actuator for a stated joint (torque, speed, duty cycle, backlash limit, volume, cost) from three candidate architectures and defend it; compute L10 for the output bearing under a stated load spectrum; do the bore-to-bore stack-up.

### 18. Test stations, fixtures, and jigs for actuators and robots

Learning objectives around: designing the test strategy for an actuator and for a whole robot through EVT, DVT, PVT and production; specifying a test station; designing the alignment fixtures that make the assembly correct in the first place.

Core content: the test ladder (incoming inspection, sub-assembly, actuator end-of-line, robot end-of-line, burn-in, sample audit); actuator end-of-line tests and what each detects: no-load current and torque versus speed sweep (friction, stiction, seal drag, assembly damage), breakaway torque, torque ripple and cogging, backlash and lost motion by torsional hysteresis curve, torsional stiffness, efficiency under load on a dynamometer or back-to-back rig, brake holding torque, thermal rise, acoustic signature, encoder calibration and offset, leak or IP test; friction taught properly (Stribeck behavior, stiction, seal and grease contribution, temperature dependence, why the run-in curve matters, what a friction signature limit should be based on); robot end-of-line (drive, lift, climb or reach, sensor and camera calibration on a target fixture, communications, battery and charging, safety stop and brake, a short mission on a test track or a sample structure); burn-in and HASS; golden units and gauge R&R on every test station (link to the Six Sigma course); pass and fail limits from data, not guesses; test data captured per serial number.

Fixtures and jigs: axis parallelism and concentricity fixtures (dial indicator pairs, precision mandrels, laser alignment, CMM when it is worth it); bearing press fixtures with force-displacement monitoring and what the curve shows; gear mesh contact pattern checks; preload setting fixtures; wheel alignment and toe on a drive module; frame flatness and rail straightness checks; assembly fixtures that locate on the datum features from the drawing (link to the GD&T course); fixture design rules (3-2-1 location, repeatability, poka-yoke, ergonomics for heavy parts, calibration and control of the fixture itself as a gauge).

Real-world examples: at least three verified (candidates: published gearbox EOL test methods; a published encoder calibration procedure; ISO 9283 test methods as used in a published robot datasheet; a NASA or automotive published press-fit monitoring case).

Exercise: write the end-of-line test specification for a stated drive unit (tests, limits with rationale, cycle time, fixture list); design the parallelism check for a two-bore housing and state its uncertainty.

### 19. Building the fleet: system-level DFx, safety certification, and the assembly line

Learning objectives around: what changes when a robot goes from ten units to a thousand; the certifications that shape the design early; designing the assembly line and its time budget.

Core content: system-level DFx (harness and cable management in moving joints, connector selection and mating cycles, battery pack assembly and its safety requirements, sensor mounting and calibration provisions, serviceability of wear items in the field, modularity of drive units); the safety and compliance map for mobile and industrial robots (ISO 3691-4, ANSI/RIA R15.08, UL 3100, ISO 10218, ISO/TS 15066, ISO 13849 performance levels, EMC, IP ratings) and what each demands from the mechanical design before DVT; traceability (serial numbers on every actuator, test data per unit, MES, ECO discipline at fleet scale, link to Module 14); field failure feedback (RMA analysis, failure mode Pareto, closing the loop to design); the assembly line: process flow, sub-assembly versus main line, takt time from demand, line balancing, time studies with MODAPTS and MOST and when each is appropriate, discrete event simulation (what a FlexSim style model answers and what it does not), ergonomics and lifting for heavy modules, kitting, poka-yoke, capacity planning; the economic case (cost per unit versus volume, tooling and fixture investment, test station capital, when to automate a station).

Real-world examples: at least three verified (candidates: a published AMR or AGV safety certification write-up; a published time study or line balancing case; a published account of a robotics company's ramp with numbers from the company itself).

Exercise: from a stated demand and a stated process list with times, compute takt, balance the line, identify the bottleneck station, and state the fixture and test station count; then a MODAPTS estimate for one assembly step.

## Structure, verification, and sessions

Each module follows the page structure in `CLAUDE.md` exactly (objectives, why this matters, core content, design rules table with sources, real-world example, common mistakes, worked exercise, quiz, key takeaways, references). Same word target as the process modules; note deviations in `PROGRESS.md`. Diagrams are inline SVG drawn by you: an actuator cross-section with the tolerance stack labeled, a torsional hysteresis curve, a Stribeck curve, a press-fit force-displacement curve with good and bad signatures, a test ladder, a line balance chart.

Run the existing `tools/verify_all.py` after each module. Add the three modules to `course.js` with `built: true` only when complete. Update `index.html`, `glossary.html`, and `references.html`.

Sessions and model recommendation, per the token discipline in `CLAUDE.md`:

- **Session R1** (strongest model): Phase A for the three modules only. Search for and read sources, produce `SOURCES.md` entries with at least 8 verified sources per module (these modules lean on standards and catalogs more than the others), a one-paragraph outline per module, the list of real-world examples with sources, and the list of any claims you could not verify. Stop for the author's approval.
- **Session R2** (strongest model): build Module 17. Stop for review.
- **Sessions R3 and R4** (strongest model for 18, mid-tier acceptable for 19): build the remaining modules one per session.
- **Session R5** (mid-tier): index, glossary, references, README, verification pass, final summary.

---

# Kickoff prompt (paste into Claude Code in the DFx course folder)

Read CLAUDE.md, then ROBOTICS.md fully. Print your model recommendation line for Session R1. Do Session R1 only: Phase A research and outline for Modules 17, 18, and 19 as ROBOTICS.md describes. Do not write any HTML. When done, summarize the three outlines, list the real-world examples you intend to use with their sources, list any claims you could not verify, then stop and wait for my approval.

# Standing resume prompt (later sessions)

Read CLAUDE.md, ROBOTICS.md, and the top of PROGRESS.md, then continue from the Resume here line. Print your model recommendation line first.
