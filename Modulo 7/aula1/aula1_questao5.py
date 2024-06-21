index_vogais = []
vogais = 0
frase = input("Digite uma frase: " )
for i in range(len(frase)):
    if frase[i] in ["a","e","i","o","u"]:
        vogais += 1
        index_vogais.append(i)
        

print(f"O numero de vogais: {vogais}")
print(f"Os indices das vogais {index_vogais}")
