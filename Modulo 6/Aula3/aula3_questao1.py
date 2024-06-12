i,n = 0,-1
v = []
while(i>n):
    v.append(input("Insira os valores na lista: (caso queira sair digite x)"))
    if i>3:
        if v[i] == "x":
            v.pop(i)
            break
    i+=1

print(f"Lista original:{v}")
print(f"Os 3 primeiro numeros: {v[:3]}")
print(f"Os 2 ultimos numeros: {v[:-3:-1]}")
print(f"Lista invertida: {v[::-1]}")
print(f"Indice Par: {v[::2]}")
print(f"Indice Impar: {v[1::2]}")