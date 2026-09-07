"""Check every external link in the given HTML files. Usage: python tools/checklinks.py file1.html file2.html ...
Prints one line per URL with HTTP status. Exit code 0 always; review output."""
import re, sys, urllib.request, urllib.error, ssl, concurrent.futures
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) dfx-course-linkcheck"}
def check(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                return url, r.status, ""
        except urllib.error.HTTPError as e:
            if method == "GET": return url, e.code, ""
        except Exception as e:
            if method == "GET": return url, 0, type(e).__name__
    return url, 0, "unknown"
urls = set()
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    urls.update(re.findall(r'href="(https?://[^"]+)"', s))
with concurrent.futures.ThreadPoolExecutor(8) as ex:
    for url, code, err in sorted(ex.map(check, sorted(urls))):
        flag = "OK " if 200 <= code < 400 else ("BLOCKED" if code in (401, 403, 405, 429) else "DEAD")
        print(f"{flag:8}{code:4} {url} {err}")
