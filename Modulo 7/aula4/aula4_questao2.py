import os
with open ("helloword.txt","r") as f:
    texto = str(f.read)
    print(texto)
    
palavras = str((texto.split()))
with open ("palavras.txt","w") as p:
        p.write(palavras)

with open ("palavras.txt","rt") as p:
    saida = p.read()
print(saida)