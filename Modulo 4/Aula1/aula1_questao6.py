n = int(input("Digite um valor: "))
i = 0
soma,soma_Sapo,soma_rato,soma_coelho  = 0,0,0,0
while(n > i):
    x = int(input("Digite a Quantia de especies: "))
    animal = (input("Digite a primeira letra do animal: "))
    soma = x + soma
        
    if(animal == "C"):
        soma_coelho += x
    
    if(animal == "R"):
        soma_rato += x
    
    if(animal == "S"):
        soma_Sapo += x
    
    i+=1

print(f"Total: {soma} Cobaias")

print(f"Total de Coelhos: {soma_coelho} ")

print(f"Total de Ratos: {soma_rato} ")

print(f"Total de Sapos: {soma_Sapo} ")

print(f"Percentual de coelhos: {soma_coelho/soma*100:,.2f} % ")

print(f"Percentual de Ratos: {soma_rato/soma*100:,.2f} % ")

print(f"Percentual de Sapos: {soma_Sapo/soma*100:,.2f} % ")
