#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:  
import random

num_elementos = random.randint(5,20)
v = []
for i in range(num_elementos):
    v.append(random.randint(1,10))
print(v)
print(sum(v))
print(sum(v)/len(v))