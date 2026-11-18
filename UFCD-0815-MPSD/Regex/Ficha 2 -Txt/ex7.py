import re 

registos=""
padraonif=r"NIF:\s*(\d{9})"

with open('registos.txt', 'r', encoding='utf-8') as readfile:
    registos = readfile.read()

nifs = re.findall(padraonif, registos)

print(nifs)