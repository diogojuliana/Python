import re

registos=""
padraonome=r"Nome:\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
padraonif=r"NIF:\s*(\d{9})"
padraodata=r"Data:\s*(\d{2}/\d{2}/\d{4})"
padraocodigopostal=r"Código Postal:\s*(\d{4}-\d{3})"
padraodominio=r"(?:www\.)?([\w\.-]+\.[a-zA-Z]{2,})"

with open('registos.txt', 'r', encoding='utf-8') as readfile:
    registos = readfile.read()

nomes = re.findall(padraonome, registos)
nifs = re.findall(padraonif, registos)
codigospostais = re.findall(padraocodigopostal, registos)
dominios = re.findall(padraodominio, registos)
datas = re.findall(padraodata, registos)

pessoas = list(zip(nomes, nifs, codigospostais, dominios, datas))
for item in pessoas:
    print(f"{item[0]}|{item[1]}|{item[2]}|{item[3]}|{item[4]}")

with open('resumo.txt', 'w', encoding='utf-8') as writefile:
    for item in pessoas:
        writefile.write(f"{item[0]}|{item[1]}|{item[2]}|{item[3]}|{item[4]}\n")