import os
import glob
import markdown
from flask import Flask, render_template_string, abort

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOCS = {}

def load_docs():
    pattern = os.path.join(BASE_DIR, "**/*.md")
    files = glob.glob(pattern, recursive=True)
    pattern2 = os.path.join(BASE_DIR, "**/Pairing")
    files += glob.glob(pattern2, recursive=True)
    for f in sorted(files):
        rel = os.path.relpath(f, BASE_DIR)
        if rel.startswith("."):
            continue
        DOCS[rel] = f

load_docs()

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Campaign Manager</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: Georgia, serif; background: #1a1208; color: #e8d5a3; display: flex; height: 100vh; overflow: hidden; }
  #sidebar {
    width: 280px; min-width: 220px; background: #111008; border-right: 2px solid #5a3e1b;
    overflow-y: auto; padding: 0; flex-shrink: 0;
  }
  #sidebar h1 {
    font-size: 1rem; text-transform: uppercase; letter-spacing: 2px;
    color: #c9a84c; padding: 1.2rem 1rem 1rem; border-bottom: 1px solid #3a2810;
    background: #0d0a04;
  }
  .section-header {
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1.5px;
    color: #7a5c2e; padding: 0.8rem 1rem 0.4rem; border-top: 1px solid #2a1e0c;
  }
  #sidebar a {
    display: block; padding: 0.45rem 1rem 0.45rem 1.4rem;
    color: #c4a96a; text-decoration: none; font-size: 0.85rem;
    border-left: 3px solid transparent; transition: all 0.15s;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  #sidebar a:hover { background: #221a08; border-left-color: #c9a84c; color: #f0d890; }
  #sidebar a.active { background: #2d2010; border-left-color: #c9a84c; color: #f0d890; font-weight: bold; }
  #content { flex: 1; overflow-y: auto; padding: 2rem 3rem; max-width: 900px; }
  #content h1 { font-size: 2rem; color: #f0d890; border-bottom: 2px solid #5a3e1b; padding-bottom: 0.5rem; margin-bottom: 1.2rem; }
  #content h2 { font-size: 1.4rem; color: #c9a84c; margin: 1.5rem 0 0.6rem; }
  #content h3 { font-size: 1.1rem; color: #b8923a; margin: 1.2rem 0 0.4rem; }
  #content h4 { font-size: 0.95rem; color: #a07830; margin: 1rem 0 0.3rem; }
  #content p { line-height: 1.8; margin-bottom: 0.9rem; color: #dcc888; }
  #content ul, #content ol { margin: 0.5rem 0 1rem 1.5rem; }
  #content li { line-height: 1.7; color: #dcc888; margin-bottom: 0.2rem; }
  #content table { border-collapse: collapse; margin: 1rem 0; width: 100%; }
  #content th { background: #2d2010; color: #f0d890; padding: 0.5rem 0.8rem; border: 1px solid #5a3e1b; text-align: left; }
  #content td { padding: 0.4rem 0.8rem; border: 1px solid #3a2810; color: #dcc888; }
  #content tr:nth-child(even) td { background: #1f170a; }
  #content code { background: #0d0a04; border: 1px solid #3a2810; border-radius: 3px; padding: 0.1rem 0.3rem; font-size: 0.85em; color: #c9a84c; }
  #content pre { background: #0d0a04; border: 1px solid #3a2810; border-radius: 5px; padding: 1rem; overflow-x: auto; margin: 1rem 0; }
  #content pre code { border: none; padding: 0; background: none; }
  #content blockquote { border-left: 3px solid #5a3e1b; margin: 1rem 0; padding: 0.5rem 1rem; background: #1f170a; color: #b8a070; }
  #content hr { border: none; border-top: 1px solid #3a2810; margin: 1.5rem 0; }
  #content a { color: #c9a84c; }
  .welcome { text-align: center; padding: 4rem 2rem; color: #7a5c2e; }
  .welcome h2 { font-size: 2rem; color: #c9a84c; margin-bottom: 1rem; }
</style>
</head>
<body>
<div id="sidebar">
  <h1>⚔ Campaign Manager</h1>
  {% for section, items in sections.items() %}
    <div class="section-header">{{ section }}</div>
    {% for label, path in items %}
      <a href="/doc/{{ path }}" {% if current == path %}class="active"{% endif %}>{{ label }}</a>
    {% endfor %}
  {% endfor %}
</div>
<div id="content">
  {% if content %}
    {{ content | safe }}
  {% else %}
    <div class="welcome">
      <h2>⚔ Gitz vs Slaves</h2>
      <p>Path to Glory Campaign Manager</p>
      <p style="margin-top:2rem;">Select a document from the sidebar to begin.</p>
    </div>
  {% endif %}
</div>
</body>
</html>"""

def build_sections():
    order = {
        "Campaign Lore": [],
        "WH P2G": [],
        "Agent Flows": [],
        "AI Planning": [],
        "Root": [],
    }
    for rel in sorted(DOCS.keys()):
        parts = rel.split(os.sep)
        name = os.path.splitext(parts[-1])[0] if "." in parts[-1] else parts[-1]
        if parts[0] in order:
            order[parts[0]].append((name, rel))
        else:
            order["Root"].append((name, rel))
    sections = {k: v for k, v in order.items() if v}
    return sections

@app.route("/")
def index():
    return render_template_string(HTML, sections=build_sections(), content=None, current=None)

@app.route("/doc/<path:docpath>")
def doc(docpath):
    if docpath not in DOCS:
        abort(404)
    filepath = DOCS[docpath]
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    html = markdown.markdown(raw, extensions=["tables", "fenced_code", "nl2br"])
    return render_template_string(HTML, sections=build_sections(), content=html, current=docpath)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
