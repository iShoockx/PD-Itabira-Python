n = int(input("Digite um valor: "))
maior=0
while(n > 0):
    x = int(input("Digite o valor de X: "))
    if(x>maior):
        maior=x
        n = n - 1
    else:
        n = n - 1
else:
    print(maior)