x=int(input("Digite a nota para o filme: (1 a 5)"))

#Se a avaliação for 5, imprima "Excelente!"
if (x==5):
    print("Excelente!")
#Se a avaliação for 4, imprima "Muito Bom!"
elif (x==4):
    print("Muito Bom!")
#Se a avaliação for 3, imprima "Bom!"
elif (x==3):
    print("Bom!")
#Se a avaliação for 2, imprima "Regular."
elif (x==2):
    print("Regular.")
#Se a avaliação for 1, imprima "Ruim."
elif (x==1):
    print("Ruim.")
else:
    print("Valor invalido")