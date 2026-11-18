import re

registos=""
padraocodigopostal=r"Código Postal:\s*(\d{4}-\d{3})"
with open('registos.txt', 'r', encoding='utf-8') as readfile:
    registos = readfile.read()

codigospostal = re.findall(padraocodigopostal, registos)

print(codigospostal)