
s=(input("Digite seu genero:(F ou M) "))
i=int(input("Digite sua idade: "))
t=int(input("Digite seu tempo de serviço: "))

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
a=(s=="F" and i>60) or (s=="M" and i>65)
#B: Ou ter trabalhado pelo menos 30 anos
b= t>=30
#C: Ou ter 60 anos  e trabalhado pelo menos 25.
c= i>=60 and t>=25
print(a or b or c)