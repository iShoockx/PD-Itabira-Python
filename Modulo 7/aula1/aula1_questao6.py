frase = input("Digite uma frase: ")
objetivo = input("Digite uma palavra objetivo: ")
v = []
for i in frase:
    while i != " ":
        x = []
        for j in objetivo:
            if j in frase :
                 x.append(j)
        v.append(x)
print(v)
#Nao consegui