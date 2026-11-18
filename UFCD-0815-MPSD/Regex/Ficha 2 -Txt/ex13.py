from datetime import datetime
import re

padraodata = r"Data:\s*(\d{2}/\d{2}/\d{4})"

with open("registos.txt", "r", encoding="utf-8") as readfile:
  registos = readfile.read()

datas_encontradas = re.findall(padraodata, registos)

limite_superior = datetime.strptime("01/01/2025", "%d/%m/%Y").date()

for data_str in datas_encontradas:
  data = datetime.strptime(data_str, "%d/%m/%Y").date()

  if data < limite_superior:
    print(f"Data {data_str} é válida.")