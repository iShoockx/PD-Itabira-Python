import random
lista_crip = []
def encrypt(lista,encode):
    for i in lista:
        letras_crip = []
        for j in i:
            x = ord(j)+encode
            y = chr(x)
            letras_crip.append(y)
        lista_crip.append(letras_crip)
    return lista_crip
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

z = encrypt(nomes,random.randint(1,10))
print(z)


          

