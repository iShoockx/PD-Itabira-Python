frase = input("Digite uma frase")
vogais = ["a","e","i","o","u","A","E","I","O","U"]
frase_modificada = ""
x = str
for i in frase:
    if i in vogais:
        frase_modificada +="*"
    else:
        frase_modificada+=i
    
print (frase_modificada)