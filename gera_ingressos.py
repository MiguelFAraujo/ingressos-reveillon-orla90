import uuid
import os

# CONFIGURAÇÕES DO EVENTO
EVENTO = "Ingresso Reveillon Orla 90"
DATA_EVENTO = "31/12/2025"
LOCAL = "Rua 90 – Cordeirinho, Maricá"
PRECO = "R$ 150,00"

# URL BASE PARA VALIDAÇÃO
URL_BASE = "https://meusite.com/validar?token="

# QUANTIDADE TOTAL
TOTAL = 150

# LOTES
LOTES = {
    1: (1, 50),
    2: (51, 100),
    3: (101, 150)
}

# TEMPLATE HTML
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Ingresso {id:03d}</title>
<style>
body {{
    font-family: Arial, sans-serif;
    padding: 20px;
    background: #f3f3f3;
}}
.card {{
    width: 550px;
    background: #fff;
    border: 2px solid #000;
    padding: 20px;
    margin: auto;
}}
h2 {{
    margin-top: 0;
}}
.qr {{
    text-align: center;
    margin: 20px 0;
}}
</style>
</head>
<body>
<div class="card">
    <h2>{evento}</h2>

    <p><b>Data:</b> {data}</p>
    <p><b>Local:</b> {local}</p>
    <p><b>Preço:</b> {preco}</p>

    <p><b>Lote:</b> {lote}</p>
    <p><b>ID:</b> {id}</p>
    <p><b>Token:</b> {token}</p>

    <div class="qr">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={url}" width="250">
    </div>

    <p><b>Validação:</b> {url}</p>
</div>
</body>
</html>
"""

# CRIAR PASTA PARA ARQUIVOS
output_folder = "ingressos_html"
os.makedirs(output_folder, exist_ok=True)

# GERAR INGRESSOS
for i in range(1, TOTAL + 1):
    token = str(uuid.uuid4())
    url = URL_BASE + token

    # IDENTIFICAR O LOTE
    for lote, intervalo in LOTES.items():
        inicio, fim = intervalo
        if inicio <= i <= fim:
            lote_atual = lote
            break

    # GERAR HTML
    html = HTML_TEMPLATE.format(
        id=i,
        token=token,
        url=url,
        evento=EVENTO,
        data=DATA_EVENTO,
        local=LOCAL,
        preco=PRECO,
        lote=lote_atual
    )

    # NOME DO ARQUIVO FINAL
    filename = os.path.join(output_folder, f"ingresso_{i:03d}.html")

    # SALVAR
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

print("✔ 150 ingressos gerados com sucesso!")
print(f"Pasta criada: {output_folder}/")
