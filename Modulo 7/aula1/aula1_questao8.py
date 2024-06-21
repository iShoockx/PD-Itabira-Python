cpf = input("Digite seu cpf")
m1 = 10
m2 = 11
aux = 0
aux2 = 0
print(cpf[12:])
#verificador primeiro numero
for i in cpf[:11]:
    if not i ==".":
        
        v = int(i)*m1
        aux += v
        m1 -= 1


resto = aux%11
if resto < 2:
    digito1 = 0
else: 
    digito1 = 11-resto



#Segundo digito
for j in cpf[:11]:
    if not (j =="."):
        v = int(j)*m2
        aux2 += v
        m2 -= 1
aux2 += digito1*2


resto = aux2%11
if resto < 2:
    digito2 = 0
else: 
    digito2 = 11-resto

digito_v = (digito1 * 10) + digito2
digito_v = f"{digito_v:2.0}"
if cpf[12:] == str(digito_v):
    print("cpf valido")
else:
    print("Cpf invalido")

