import re

dados=""
padraoemail=r"[\w\.]+@[\w]+\.[pt]+"

with open('dados.txt', 'r', encoding='utf-8') as readfile:
    dados = readfile.read()

emails = re.findall(padraoemail, dados)

print(emails)