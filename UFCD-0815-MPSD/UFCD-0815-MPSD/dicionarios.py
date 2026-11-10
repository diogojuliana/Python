# not lista "[]" não é acessivel por index 0 1 2 3
# dicionario "{}" é acessivel por maping, ou seja key {"nome":"dario"}
# key -> value

dic_pess=[{"nome":"dario","idade":25,"tel":931651835}, {"nome":"Joao","idade":22,"tel":931651835}]

dic_pess[0]["nome"]

dic_pess={"nome":"dario","idade":25,"tel":931651835} 
print(dic_pess)

dic_pess["cargo"]="obra" # se nao existir cria nova entrada
print(dic_pess)

dic_pess["nome"]="Joao" #se existir vai substituir
print(dic_pess)

dic_pess["nom"]=dic_pess["nome"]
print(dic_pess)

dic_pess.pop("nome") # apaga key & value
print(dic_pess)


print(dic_pess.keys()) # mostra todas as keys
print(dic_pess.values()) # mostra todos os valores
print(dic_pess.items()) # mostra todas as keys & values em tupolas

dic_pess.update({"nom":"Pedro"})
print(dic_pess)

dic_pess.update({"Morada":"R.Do Desespero"})
print(dic_pess)

dic_pess.popitem # Apaga ultimo Elemento inserido


for key,value in dic_pess.items():
    print (f"chave: { key }, Valor: { value }") #LISTAR UM A UM