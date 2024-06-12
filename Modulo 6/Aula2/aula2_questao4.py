v1 = []
v2 = []

n1 = int(input("Digite a quantidade de elementos que tera na lista 1: "))
for i in range(n1):
    v1.append(int(input(f"Digite os {n1} elementos da lista: ")))

n2 = int(input("Digite a quantidade de elementos que tera na lista 2: "))
for i in range(n2):
    v2.append(int(input(f"Digite os {n2} elementos da lista: ")))

for i in range(n2):
    if n1>i:
        print(v1[i])
        print(v2[i])
    
    else:
        print(v2[i])