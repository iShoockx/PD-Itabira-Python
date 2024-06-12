import math
import random 

aux = 0
n = int(input("Digite um numero de repetiçoes: "))
for i in range(n):
    aux = random.randint(0,100)
    aux += aux
print(f"{math.sqrt(aux):,.2f}")