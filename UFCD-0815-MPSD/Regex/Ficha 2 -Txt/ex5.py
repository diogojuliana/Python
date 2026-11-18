import re

dados=""
padraonome=r"Nome:\s*([^,]+)"
padraoemail=r"[\w\.]+@[\w]+\.[\w]+"
padraotelemovel=r"\d{3}[-\s]?\d{3}[-\s]?\d{3}"

with open('dados.txt', 'r', encoding='utf-8') as readfile:
    dados = readfile.read()

nomes = re.findall(padraonome, dados)
emails = re.findall(padraoemail, dados)
telemoveis = re.findall(padraotelemovel, dados)

pessoas = list(zip(nomes, emails, telemoveis))
for item in pessoas:
    print(f"{item[0]}|{item[1]}|{item[2]}")

with open('extraidos.txt', 'w', encoding='utf-8') as writefile:
    for item in pessoas:
        writefile.write(f"{item[0]}|{item[1]}|{item[2]}\n")