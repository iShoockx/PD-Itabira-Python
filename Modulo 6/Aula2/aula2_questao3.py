import random

lista_1 = []
lista_2 = []
lista_3 = []

for i in range(20):
    lista_1.append(random.randint(0,50))
    lista_2.append(random.randint(0,50))

for i in range(20):
    if lista_1[i] in lista_2:
        if lista_1[i] in lista_3:
            break
        else:    
            lista_3.append(lista_1[i])

    
print(f"lista 1 - {lista_1}")
print(f"lista 2 - {lista_2}")
print(f"lista 3 - {lista_3}")

for i in lista_3:
    print(f"{i}: (lista 1 ={lista_1.count(i)}  Lista 2 ={lista_2.count(i)})")