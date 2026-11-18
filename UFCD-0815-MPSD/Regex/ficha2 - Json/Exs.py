import re as reg
import json
import os

novo=[] #Para ex 5
nome_email = [] #Para ex 6
padraoemail = r"^[\w\.-]+@[\w\.-]+\.\w+$"

#Ex 1 -----------------------------------------------------------------------------------------------

with open("dados.json", "r", encoding="utf-8") as readfile:
    dados = json.load(readfile)

# 2 -----------------------------------------------------------------------------------------------
for d in dados:
        estado = "válido" if reg.match(padraoemail, d["email"]) else "inválido"
        novo.append((d['nome'], d['email'], estado)) # Ex5
        print(f"{d['nome']}: {d['email']} -> {estado}")

nome_email = [(d['nome'], d['email']) for d in dados if reg.match(padraoemail, d["email"])] # Ex6

#Ex3 -----------------------------------------------------------------------------------------------

pattdominio = r"//([\w\.-]+)(\.\w+)$"


for d in dados:
    dominio = reg.search(pattdominio, d["site"])
    if dominio:
        print(f"{d['nome']}: {d['email']} -> Domínio: {dominio.group(2)}") 
    else:
        print(f"{d['nome']}: {d['email']} -> Domínio não encontrado")

pattnif = r"^[123568]\d{8}$"

#Ex 4 -----------------------------------------------------------------------------------------------
for d in dados:
    nif = reg.search(pattnif, d["nif"])
    if nif:
        print(f"{d['nome']}: {d['email']} -> NIF: {nif.group(0)}")
        novo.append((d['nome'], d['email'], "válido")) # Ex5

    else:
        print(f"{d['nome']}: {d['email']} -> NIF inválido")
        
        
patttelefone = r"^\D*(\d\D*){9}$"
# Ex 5 -----------------------------------------------------------------------------------------------
for d in dados:
    telefone = reg.search(patttelefone, d["telemovel"])
    if telefone:
        print(f"{d['nome']}: {d['email']} -> Telefone: {telefone.group(0)}")
        novo.append((d['nome'], d['email'], "válido")) # Ex5
    else:
        print(f"{d['nome']}: {d['email']} -> Telefone inválido")


with open("dados_validos.json", "w", encoding="utf-8") as writefile:
    json.dump(novo, writefile, ensure_ascii=False, indent=4)

# Ex 6 -----------------------------------------------------------------------------------------------
with open("nome_email.txt", "w", encoding="utf-8") as writefile:
    for nome, email in nome_email:
        writefile.write(f"{nome}: {email}\n")
