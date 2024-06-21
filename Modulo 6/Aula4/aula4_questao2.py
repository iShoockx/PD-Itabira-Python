Frase = input("Digite uma frase: ")

vogais = [l for l in Frase if l in ["a","e","i","o","u"] ]
vogais.sort()
print(vogais)
consoantes = [l for l in Frase if not l in ["a","e","i","o","u"," "] ]
print(consoantes)

