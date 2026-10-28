#!/usr/bin/env python3
"""Portfolio-Builder — JSON profile to static HTML portfolio."""
import argparse, json, html, os
BASE = os.path.dirname(os.path.abspath(__file__))
def main():
    p = argparse.ArgumentParser(); p.add_argument("--profile", default=os.path.join(BASE, "profile.json")); p.add_argument("--out", default="index.html")
    a = p.parse_args(); prof = json.load(open(a.profile))
    skills = "".join(f"<li>{html.escape(s)}</li>" for s in prof.get("skills", []))
    projects = "".join(f"<li><strong>{html.escape(x.get('name',''))}</strong> — {html.escape(x.get('description',''))}</li>" for x in prof.get("projects", []))
    links = "".join(f'<li><a href="{html.escape(v)}">{html.escape(k)}</a></li>' for k, v in prof.get("links", {}).items())
    page = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{html.escape(prof.get('name',''))}</title></head>
<body><h1>{html.escape(prof.get('name',''))}</h1><p>{html.escape(prof.get('headline',''))}</p>
<h2>Skills</h2><ul>{skills}</ul><h2>Projects</h2><ul>{projects}</ul><h2>Links</h2><ul>{links}</ul></body></html>"""
    open(a.out, "w").write(page); print(f"Wrote {a.out}")
if __name__ == "__main__": main()
