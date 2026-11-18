dados=""

with open('dados.txt', 'r', encoding='utf-8') as readfile:
    dados = readfile.read()

print(dados)