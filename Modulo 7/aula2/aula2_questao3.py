frase_inversa = ""
frase1= ""
while True:
    frase = input("Digite uma frase: ")
    frase = frase.lower()
    for i in frase:
        if not(i == "!" or i == "?" or i == " "):
            frase1 += i 
    for i in frase[-1::-1]:
        if not(i == "!" or i == "?" or i == " "):
            frase_inversa += i 
    if frase1 == frase_inversa:
        print("A frase é um palindromo")
    else:
        print("A frase nao é um palindromo")