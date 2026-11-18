import re

dados=""
padraonome=r"Nome:\s*([^,]+)"

with open('dados.txt', 'r', encoding='utf-8') as readfile:
    dados = readfile.read()

nomes = re.findall(padraonome, dados)

print(nomes)