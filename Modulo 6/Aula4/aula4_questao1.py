#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
list_1 = []
for i in range(20,51):
    list_1.append(i)

list_comp1 = [n for n in list_1 if n%2==0]
print(list_comp1)

#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
list_2 = []
for i in range(1,10):
    list_2.append(i)
list_comp2 = [n*n for n in list_2]
print(list_comp2)


#Todos os números entre 1 e 100 que sejam divisíveis por 7
list_3 = []
for i in range(1,101):
    list_3.append(i)
list_comp3 = [n for n in list_3 if n%7 == 0]
print(list_comp3)

    

#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 
list_4 = []
for i in range(0,30,3):
    list_4.append(i)
list_comp4 = ["Par" if n%2 == 0 else "Impar" for n in list_4]
print(list_comp4)