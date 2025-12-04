# gera_index.py
import os, html

docs_folder = "docs"
files = sorted([f for f in os.listdir(docs_folder) if f.lower().endswith(".html")])

title = "Ingressos - Reveillon Orla 90"
lines = []
lines.append(f"<!doctype html>\n<html lang='pt-br'>\n<head>\n<meta charset='utf-8'>\n<title>{title}</title>\n<style>body{{font-family:Arial}} .wrap{{max-width:900px;margin:auto}} .card{{border:1px solid #ddd;padding:12px;margin:6px 0}}</style>\n</head>\n<body>\n<div class='wrap'><h1>{title}</h1>\n<p>Data: 31/12/2025 — Local: Rua 90 - Cordeirinho, Maricá</p>\n<hr>\n<div>\n")

for f in files:
    safe = html.escape(f)
    lines.append(f"<div class='card'><a href='./{safe}' target='_blank'>{safe}</a></div>\n")

lines.append("</div>\n</div>\n</body>\n</html>")

with open(os.path.join(docs_folder,"index.html"),"w",encoding="utf-8") as fh:
    fh.write("".join(lines))

print("index.html criado em docs/index.html")
