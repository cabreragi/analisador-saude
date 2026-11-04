import matplotlib.pyplot as plt
casos = {}

with open("dados/sifilis_congenita_sp.csv", encoding="latin-1") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(";")
        ano = partes[0].strip('"')
        if len(partes) == 2 and ano.isdigit():
            casos[int(ano)] = int(partes[1])
casos_inicio = casos[2016]
casos_fim = casos[2024]
           
variacao = ((casos_fim - casos_inicio) / casos_inicio) * 100

print("\n--- ANÁLISE DA EVOLUÇÃO DOS CASOS ---")
print(f"Casos em 2016: {casos_inicio}")
print(f"Casos em 2024: {casos_fim}")
print(f"Variação percentual: {variacao:.2f}%")

valores = []
for ano in casos:
    if 2016 <= ano <= 2024:
        valores.append(casos[ano])

print("Período: 2016 a 2024")
print("Total de casos:", sum(valores))
print("Média por ano:", round(sum(valores) / len(valores), 1))
print("Maior número:", max(valores))
print("Menor número:", min(valores))

print()
print("Ano | Casos | Variação")

anos = sorted(a for a in casos if 2016 <= a <= 2024)

for i, ano in enumerate(anos):
    if i == 0:
        print(ano, casos[ano], "-")
    else:
        anterior = casos[anos[i - 1]]
        variacao = (casos[ano] - anterior) / anterior * 100
        print(ano, casos[ano], f"{variacao:.1f}%")

valores_anos = [casos[a] for a in anos]

plt.figure(figsize=(9, 5))
barras = plt.bar(anos, valores_anos, color="steelblue")

for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura,
        f"{int(altura):,}".replace(",", "."),
        ha="center",
        va="bottom"
    )
plt.title("Sífilis congênita: casos confirmados no município de SP (2016-2024)")
plt.xlabel("Ano de diagnóstico")
plt.ylabel("Casos confirmados")
plt.xticks(anos)
plt.savefig("grafico_casos.png", dpi=150)
plt.show()
