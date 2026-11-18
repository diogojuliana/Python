import re

dados=""
padraotelemovel=r"\d{3}[-\s]?\d{3}[-\s]?\d{3}"

with open('dados.txt', 'r', encoding='utf-8') as readfile:
    dados = readfile.read()

telemoveis = re.findall(padraotelemovel, dados)

print(telemoveis)