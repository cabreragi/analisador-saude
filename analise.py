casos = {}

with open("dados/sifilis_congenita_sp.csv", encoding="latin-1") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(";")
        ano = partes[0].strip('"')
        if len(partes) == 2 and ano.isdigit():
            casos[int(ano)] = int(partes[1])

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
