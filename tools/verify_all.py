"""Phase D cross-checks over all modules and pages."""
import re, glob, html, sys
SRC = open("SOURCES.md", encoding="utf-8").read()
src_urls = set(re.findall(r'https?://[^\s|)\]>]+', SRC))
def norm(u): return u.rstrip('/').replace('http://','https://').lower()
src_norm = {norm(u) for u in src_urls}
problems = []
sections = ["objectives","why","rules","case","mistakes","exercise","quiz","takeaways","references"]
for f in sorted(glob.glob("modules/*.html")):
    s = open(f, encoding="utf-8").read()
    f = f.replace("\\", "/")
    name = f.split("/")[-1]
    num = re.search(r'modules/(\d\d)-', f).group(1)
    dm = re.search(r'data-module="(\d+)"', s).group(1)
    if dm != num: problems.append((name, "data-module mismatch", dm))
    for sec in sections:
        if sec == "quiz" and 'class="quiz' not in s: continue
        if f'id="{sec}"' not in s: problems.append((name, "missing section id", sec))
    if 'data-pager' not in s: problems.append((name, "missing pager", ""))
    if '<footer' not in s: problems.append((name, "missing footer", ""))
    # references vs SOURCES
    ol = re.search(r'<ol class="references">(.*?)</ol>', s, flags=re.S).group(1)
    for li in re.findall(r'<li id="ref-(\d+)">(.*?)</li>', ol, flags=re.S):
        urls = re.findall(r'href="([^"]+)"', li[1])
        if not urls: problems.append((name, "ref without URL", li[0])); continue
        if not any(norm(html.unescape(u)) in src_norm for u in urls):
            problems.append((name, "ref URL not in SOURCES.md", html.unescape(urls[0])))
        if not re.search(r'\b(19|20)\d\d\b|n\.d\.', li[1]): problems.append((name, "ref without year or n.d.", li[0]))
    # quiz answers exist
    for fs in re.findall(r'<fieldset class="q"[^>]*>(.*?)</fieldset>', s, flags=re.S):
        head = re.search(r'<fieldset class="q"([^>]*)>', s)  # placeholder
    for m in re.finditer(r'<fieldset class="q"([^>]*)>(.*?)</fieldset>', s, flags=re.S):
        attrs, body = m.group(1), m.group(2)
        ans = re.search(r'data-answer="([^"]+)"', attrs).group(1)
        if 'data-type="numeric"' in attrs:
            try: float(ans)
            except: problems.append((name, "numeric answer not a number", ans))
            if 'data-tolerance' not in attrs: problems.append((name, "numeric without tolerance", ans))
        else:
            if f'value="{ans}"' not in body: problems.append((name, "answer option missing", ans))
        if 'class="explain"' not in body: problems.append((name, "question without explanation", ans[:20]))
    # placeholders
    for pat in [r'lorem ipsum', r'\bTODO\b', r'coming soon', r'\bTBD\b', r'XXX']:
        for mm in re.finditer(pat, s, flags=re.I):
            ctx = s[max(0, mm.start()-60):mm.end()+40].replace("\n"," ")
            problems.append((name, "placeholder-like text", ctx))
    # imperial units to review (outside parentheses is suspicious)
    body = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
    for mm in re.finditer(r'\b\d[\d.,]*\s?(inches|inch|in\.|psi|lbs?|°F|ft)\b', body):
        ctx = body[max(0, mm.start()-50):mm.end()+30].replace("\n"," ")
        problems.append((name, "imperial unit (review)", ctx))
    # author placeholders count
    n_auth = len(re.findall(r'<!-- AUTHOR', s))
    if n_auth == 0: problems.append((name, "no AUTHOR note", ""))
    # dashes
    if '\u2014' in s or '\u2013' in s: problems.append((name, "long dash", ""))
for f in ["index.html","glossary.html","references.html","about.html"]:
    s=open(f,encoding="utf-8").read()
    if '\u2014' in s or '\u2013' in s: problems.append((f,"long dash",""))
    for pat in [r'lorem ipsum', r'\bTODO\b', r'coming soon']:
        if re.search(pat,s,flags=re.I): problems.append((f,"placeholder",pat))
for p in problems: print(" | ".join(p))
print(len(problems), "items")
