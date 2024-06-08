n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
m = (n1+n2+n3)/3
if(m>=60):
    print("Aprovado")
    print("Fim")
elif(m>=40):
    print("Recuperação")
    print("Fim")
else:
    print("Reprovado")
    print("Fim")

