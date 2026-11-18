import re 

registos=""
nifvalido=r"NIF:\s*([123568]\d{8})"
with open('registos.txt', 'r', encoding='utf-8') as readfile:
    registos = readfile.read()

nifs = re.findall(nifvalido, registos)
print(nifs)
