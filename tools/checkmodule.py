"""Structural checks for a module page. Usage: python tools/checkmodule.py modules/NN-slug.html
Reports body word count, citation/reference cross-check, SVG accessibility, dashes, placeholder words."""
import re, sys, html
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    main = re.search(r"<main.*?</main>", s, re.S).group(0)
    body = re.sub(r"<svg.*?</svg>", "", main, flags=re.S)
    body = re.sub(r"<table.*?</table>", "", body, flags=re.S)
    body = re.sub(r"<form.*?</form>", "", body, flags=re.S)
    body = re.sub(r'<ol class="references">.*?</ol>', "", body, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    words = len(html.unescape(re.sub(r"<[^>]+>", " ", body)).split())
    cites = set(re.findall(r'href="#ref-(\d+)"', s)); refs = set(re.findall(r'id="ref-(\d+)"', s))
    dashes = s.count("\u2014") + s.count("\u2013")
    svgs = s.count("<svg"); titles = len(re.findall(r"<svg.*?<title", s, re.S)); descs = len(re.findall(r"<svg.*?<desc", s, re.S))
    placeholders = re.findall(r"(?i)lorem ipsum|\bTODO\b|coming soon|TBD", re.sub(r"<!--.*?-->", "", s, flags=re.S))
    qs = len(re.findall(r'<fieldset class="q"', s))
    print(f"{f}: body words {words}; refs {len(refs)}; cites missing {sorted(cites-refs)}; uncited {sorted(refs-cites, key=int)}; "
          f"svg {svgs} (title {titles}, desc {descs}); dashes {dashes}; quiz questions {qs}; placeholders {placeholders}")
