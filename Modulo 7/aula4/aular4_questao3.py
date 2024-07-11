with open("./estomago.txt", 'r',encoding="UTF-8") as arquivo:
      linhas = arquivo.readlines()

      # Texto das primeiras 25 linhas
      primeiras_25_linhas = "\n".join(linhas[:25])
       # Número de linhas do arquivo
      numero_linhas = len(linhas)
      # Linha com maior número de caracteres
      linha_mais_caracteres = max(linhas, key=len)
      numero_caracteres_linha_mais = len(linha_mais_caracteres.strip())
      
      # Nomes nonato e iria
      nomes = ["Nonato", "Íria","nonato","íria"]
      cont_mencoes_nomes = 0
      v = []
      for linha in linhas:
        i = []  
        while linha!=" ":    
            if not(linha == " "):
                i.append(linha)
        v.append(i)
        if v in nomes:
            cont_mencoes_nomes+=1
print(primeiras_25_linhas)
print(numero_linhas)
print(linha_mais_caracteres)
print(cont_mencoes_nomes)