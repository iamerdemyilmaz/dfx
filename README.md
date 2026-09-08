# Design for Manufacturing and Assembly: From Prototype to Production

A free, practitioner-written online course on design for manufacturing (DFM), assembly (DFA), test (DFT), and service (DFS) for mechanical and manufacturing engineers with roughly zero to five years of experience. Seventeen modules, a glossary, and a consolidated bibliography, as a static HTML site with no build step and no dependencies.

Author: Erdem Yilmaz.

## Contents

```
index.html                 course landing page with outline and progress bar
modules/00-introduction.html ... modules/16-capstone.html
glossary.html
references.html            consolidated bibliography
about.html                 author, method, licence, contact
assets/css/course.css      shared stylesheet (light and dark themes, print)
assets/js/course.js        navigation, quiz engine, progress tracking
SOURCES.md                 source register with verification status
PROGRESS.md                build log, decisions, verification results
tools/                     small Python checks used during authoring
```

## Viewing locally

Open `index.html` in a browser. Everything works from a `file://` URL. For a local server instead:

```bash
python -m http.server 8765
```

then visit <http://localhost:8765/>.

## Deploying

The site is static. Copy the files to any web host, or use one of these.

### GitHub Pages

1. Push the repository to GitHub.
2. In the repository settings, open **Pages**, choose **Deploy from a branch**, select the `main` branch and the `/ (root)` folder, and save.
3. The site appears at `https://<user>.github.io/<repository>/` within a minute or two. Paths in the site are relative, so it works in a subfolder. If the user site `<user>.github.io` carries a custom domain, this project site is served under it as well; the course is published as the repository `dfx`, so it appears at `https://erdemyilmaz.me/dfx/`.

For a custom domain, add a `CNAME` file containing the domain name and configure DNS as GitHub's Pages documentation describes.

### Netlify

1. Create a new site from the Git repository, or drag the folder onto the Netlify dashboard.
2. Leave the build command empty and set the publish directory to `/` (the repository root).
3. Deploy. Netlify serves `index.html` at the root.

No environment variables, build steps, or functions are needed.

## Editing a module

Each module is one self-contained HTML page in `modules/`. The sections appear in a fixed order: title, learning objectives, why this matters, core content, design rules table, real-world example, common mistakes, worked exercise, quiz, key takeaways, references, previous/next navigation.

- **Citations.** Inline citations are `<sup class="cite"><a href="#ref-N">[N]</a></sup>` and resolve to `<li id="ref-N">` in the module's `<ol class="references">`. Every reference carries author or organisation, title, publisher or site, year, URL, and the access date. Add each new source to `SOURCES.md` with its verification status. Sources that could not be read in full are marked with `<span class="tag">(secondary: ...)</span>`.
- **Quizzes.** Each question is a `<fieldset class="q">` with `data-answer`. Multiple choice uses radio inputs whose `value` matches `data-answer`. Numeric questions add `data-type="numeric"` and `data-tolerance`. The pass mark is 70 percent, set by `PASS_MARK` in `course.js`. Each module also opens with a three-question "Before you start" form marked `data-pre`; it is graded in the browser with explanations but never recorded as progress.
- **Diagrams.** All diagrams are inline SVG with `<title>` and `<desc>`, `viewBox` about 640 wide, `stroke="currentColor"`, and the classes `diagram-soft`, `diagram-accent`, `diagram-accent-fill`, `diagram-text`, `diagram-text-muted`.
- **Navigation.** The module list lives in the `MODULES` array at the top of `assets/js/course.js`. A module is linked only when its `built` flag is `true`.
- **Style rules.** Metric units only, imperial in parentheses only when the source is imperial. No long dashes; write ranges as "X to Y". Illustrative examples are labelled as such in the text.

### Checks

Python 3 with `requests` is enough for the authoring checks in `tools/`:

```bash
python tools/checkmodule.py modules/06-injection-molding.html
```

reports body word count, unresolved or uncited references, SVG accessibility, long dashes, quiz question count, and placeholder text.

```bash
python tools/checklinks.py modules/06-injection-molding.html
```

requests every external link and reports its HTTP status. Several publishers return 403 to scripts but work in a browser; these are listed in `PROGRESS.md`.

```bash
python tools/checkdashes.py modules/*.html
```

fails if any em or en dash is present.

## Licence

Proposed, pending the author's confirmation: course content (text, tables, diagrams, exercises, quizzes) under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/); site code (HTML, CSS, JavaScript) under the [MIT License](https://opensource.org/license/mit). Cited sources remain the property of their publishers.
