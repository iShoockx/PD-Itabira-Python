espaços = 0
frase = input("Digite uma frase")
for i in frase:
    if i == " ":
        espaços += 1
print(f"O numero de espaços: {espaços}")
