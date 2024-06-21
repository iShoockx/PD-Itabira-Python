numero = input("Digite o numero: ")

if len(numero) == 8:
    numero = "9"+ numero

if len(numero) == 9:
    print(f"{numero[:5]}-{numero[5:9]}")            
        
