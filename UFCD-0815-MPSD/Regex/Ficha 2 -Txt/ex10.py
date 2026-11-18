import re 

registos=""
padraodominio=r"(?:www\.)?([\w\.-]+\.[a-zA-Z]{2,})"

with open('registos.txt', 'r', encoding='utf-8') as readfile:
    registos = readfile.read()

dominios = re.findall(padraodominio, registos)

print(dominios)