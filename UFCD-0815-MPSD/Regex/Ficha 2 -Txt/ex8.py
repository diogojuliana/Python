import re

registos=""
padraodata=r"Data:\s*\d{2}/\d{2}/([1-9]\d{0,2}|1\d{3}|20[0-1]\d|202[0-4])"
with open('registos.txt', 'r', encoding='utf-8') as readfile:
    registos = readfile.read()

data = re.findall(padraodata, registos)

print(data)