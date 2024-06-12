import random

i,n = 0,1
x = random.randint(0,10)

while(i < n):
    y = int(input("Adivinhe o número entre 1 e 10: "))
    
    if(x==y):
        print(f"Correto! O número é: {x}")
        break
    if(abs(x-y)<3):
        print("Muito alto, tente novamente!")
    
    elif(abs(x-y)>3):
        print("Muito baixo, tente novamente!")
    
