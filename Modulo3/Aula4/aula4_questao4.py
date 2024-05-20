d=int(input("Digite a distancia da viagem(em Km): "))
p=float(input("Digite o peso do pacote(em Kg): "))
#Distância até 100 km: R$1 por kg.
if(d<=100):
    r=p
#Distância entre 101 e 300 km: R$1.50 por kg.
elif(100<=d<=300):
    r=1.5*p
#Distância acima de 300 km: R$2 por kg.
else:
    r=2*p
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
if(p>10):
    r+=10
print(f"O valor do frete é : {r}")