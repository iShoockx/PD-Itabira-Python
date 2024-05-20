
c=float(input("Digite O valor do comprimento: "))
l=float(input("Digite O valor do Largura: "))
m=float(input("Qual é o preço do metro quadrado: "))
area=c*l
p=m*area
print(f"A area do terreno é {area} m^2 e o preço é R$ {p:,.2f}")