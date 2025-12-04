import pandas as pd
import qrcode
import os
import uuid

df = pd.read_excel("ingressos.xlsx")

os.makedirs("docs", exist_ok=True)

TEMPLATE = ""
with open("template_ingresso.html", "r", encoding="utf-8") as f:
    TEMPLATE = f.read()

LOTE_VALOR = {
    "1": "185,00",
    "2": "195,00",
    "3": "215,00"
}

for index, row in df.iterrows():
    ingresso_id = row["ID"]
    token = row["TOKEN"]
    nome = row["NOME"]
    lote = str(row["LOTE"])
    valor = LOTE_VALOR.get(lote, "0")

    qr_url = f"https://meusite.com/validar?token={token}"

    # gerar QR
    img = qrcode.make(qr_url)
    qr_path = f"docs/qr_{ingresso_id}.png"
    img.save(qr_path)

    html_content = TEMPLATE\
        .replace("{{ID}}", str(ingresso_id))\
        .replace("{{NOME}}", nome)\
        .replace("{{TOKEN}}", token)\
        .replace("{{LOTE}}", lote)\
        .replace("{{VALOR}}", valor)\
        .replace("{{QR_URL}}", f"qr_{ingresso_id}.png")

    with open(f"docs/ingresso_{ingresso_id}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

print("Ingressos gerados!")
