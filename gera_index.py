import os

files = sorted(os.listdir("docs"))
links = ""

for f in files:
    if f.startswith("ingresso_") and f.endswith(".html"):
        links += f'<li><a href="{f}" target="_blank">{f}</a></li>\n'

template = ""
with open("docs/index.html.template", "r", encoding="utf-8") as f:
    template = f.read()

index_final = template.replace("{{LISTA}}", links)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index_final)

print("index.html atualizado!")
