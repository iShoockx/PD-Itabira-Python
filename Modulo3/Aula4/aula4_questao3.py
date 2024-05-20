n1=int(input("Digite o ano: "))
if(n1 % 4 == 0 and (n1 % 100 != 0 or n1 % 400 == 0)):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")