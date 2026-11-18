wrd = input("Insira uma palavra: ")
cont = {}

for letra in wrd:
    if letra in cont:
        cont[letra]+=1
    else:
        cont[letra]=1

print(cont)
