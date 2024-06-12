#1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida: A lista ordenada sem modificar a lista original// A lista original// O índice do maior valor da lista// O índice do menor valor da lista
import random

v = []
for i in range(20):
    v.append(random.randint(-100,100)
)
print(sorted(v))
print(v)
print(v.index(max(v)))
print(v.index(min(v)))
