import csv
# variaveis universais durante o processo
campos_produtos = ["ID","Produto","Preço"] # Campos para o field names dos produtos
campos_contas = ['Nome','Senha','Codigo','ID']
ID_existe = False
nome_existe = False
senha_existe = False
resposta_alteraçao_existe = False




def adicionar_csv(ms1,msg2,campos,lista_dicionario,arquivo):
    dado1 = input(ms1)
    if dado1 != "0":
        dado2 = input(msg2)
        # Automatizaçao do Id do produto
        for num_id in lista_dicionario:
            num = int(num_id["ID"])
            id = num + 1
        
        # Escolha de qual dados usar
        tamanho_campos = len(campos)
        
        if tamanho_campos == 3:
            dados = [{"ID": id, "Produto": dado1, "Preço": dado2}] # Montagem dos danos para inserçao no csv 
        
        
        elif tamanho_campos == 4:
            dados = [{"Nome": dado1,'Senha': dado2, 'Codigo':"01",'ID':id}] # Montagem dos danos para inserçao no csv 

        
        # Insenrçao dos dados
        with open(arquivo, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos) 
            escritor.writerows(dados)   #Inserçao de dados
        print(f"Criado com sucesso")

def removedor_csv(lista_dicionario,campos,arquivo):

    pergunta_de_id = input("Digite o ID do produto: (Digite 0 caso queira cancelar a açao) ")
    #Verificador de id
    for verificador_id in lista_dicionario:
        if pergunta_de_id == verificador_id["ID"]:
            ID_existe = True
    if ID_existe:
        if pergunta_de_id != "0":
            
            lista_dicionario = [linha for linha in lista_dicionario if linha['ID'] != pergunta_de_id]
            with open(arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                escritor = csv.DictWriter(arquivo_csv, fieldnames=campos) 
                escritor.writeheader() #Reescrevendo o cabeçalho para nao ficar sem colunas
                escritor.writerows(lista_dicionario) #removendo o campo
            print("Remoção feita com sucesso")

def atualizar_csv(key):

    if key == 0 :
        # Colocando as variaveis que se diferenciam do produto pro usuario
        campos = campos_produtos
        lista_dicionario = leitor_Produtos_csv
        arquivo = 'Trabalho-Pratico\\produtos.csv'
        escolha_campo = input("Oque voce deseja alterar \n 1) Nome do produto \n 2)Preço do produto \n (Digite 0 caso queira cancelar a açao)")
        if escolha_campo == "1":
            coluna = "Produto"
            msg = "Digite o novo Nome: "
            resposta_alteraçao_existe = True
        elif escolha_campo == "2":
            coluna = "Preço"
            msg = "Digite o novo Preço: "
            resposta_alteraçao_existe = True
        else:
            print("Valor invalido")
    
    elif key == 1:
        campos = campos_contas
        lista_dicionario = leitor_contas_csv
        arquivo ='Trabalho-Pratico\\Contas.csv'
        escolha_campo = input("Oque voce deseja alterar \n 1) Nome do usuario \n 2)senha do usuario \n 3) Codigo do usuario\n (Digite 0 caso queira cancelar a açao)")
        if escolha_campo == "1":
            coluna = "Nome"
            msg = "Digite o novo Nome: "
            resposta_alteraçao_existe = True
        elif escolha_campo == "2":
            coluna = "Senha"
            msg = "Digite a nova Senha: "
            resposta_alteraçao_existe = True
        elif escolha_campo == "3":
            coluna = "Codigo"
            msg = "Digite o novo Codigo: "
            resposta_alteraçao_existe = True
        
            
    if not resposta_alteraçao_existe:
        print("Valor invalido")
    
    else:
        pergunta_de_id = input("Qual o ID : ")
        novo_nome = input (msg)
        
        #Conferindo se ID existe
        for  procura_id in lista_dicionario:
            if pergunta_de_id == procura_id["ID"]:
                ID_existe = True
        
        if not ID_existe:
            print("Valor de ID nao foi encontrado")
        
        else:   
            for  procura_id in lista_dicionario:
                if pergunta_de_id == procura_id["ID"]:
                    procura_id[coluna] = novo_nome # Trocando campo 
            with open(arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                escritor = csv.DictWriter(arquivo_csv, fieldnames=campos) 
                escritor.writeheader() #Reescrenvendo cabeçalho
                escritor.writerows(lista_dicionario)   #Reenomeando de dados
                1
            print("Atualizaçao feita com sucesso")

def mostrar_produto():
    for itens_dict_produtos in leitor_Produtos_csv:
        print(f"{itens_dict_produtos["ID"]}  {itens_dict_produtos["Produto"]} {itens_dict_produtos["Preço"]} R$")
#Inicio do programa

with open('Trabalho-Pratico\\Contas.csv', newline='', encoding='utf-8') as csvcontas:
    leitor_contas_csv = list(csv.DictReader(csvcontas)) # Salva como lista para pode iterar mais de uma vez caso precise
    with open('Trabalho-Pratico\\produtos.csv', newline='', encoding='utf-8') as csvProdutos:
        leitor_Produtos_csv = list(csv.DictReader(csvProdutos))
    
    op = input("1: Login \n2: Cadastrar:  ")
    if op == "1":    
    # Condiçao para proximo estagio
        nome_existe=False
    #Pergunta ao usuario
        nome = input("Digite o seu nome de usuario: ")
    #Iterando sob a lista de dicionas para descompactar e verificar os dados do usuario    
        for itens_dict_contas in leitor_contas_csv:
            if itens_dict_contas['Nome'] == nome:
                verifica_senha = itens_dict_contas["Senha"] # Salvando informaçoes para confirmação
                verifica_codigo = itens_dict_contas['Codigo']
                nome_existe = True
        # Condiçao para proximo estagio
        senha_existe = False
        if not nome_existe :
            print("Nome nao foi encontrado")
        
        # Verificador de senha
        else:
            senha = input("Digite sua senha")
            if senha == verifica_senha:
                senha_existe = True        
        
        if senha_existe == False:
            print("Senha nao encontrada")

        if senha_existe == True:
            if verifica_codigo == "01":
                print("Escolha o numero do seu produto")
                mostrar_produto()
                #Pergunta ao cliente do produto
                op_cliente = input()
                # Verificador se o ID realmente existe
                for itens_op in leitor_Produtos_csv:
                    if op_cliente == itens_op["ID"]:
                        ID_existe = True
                        
                if not ID_existe:
                    print("Valor sinserido não existe")
                
                # Confirmaçao de compra
                
                else:
                    op2_cliente = input(f'Deseja mesmo comprar o {itens_op["Produto"]} (s/n)? ')
                    if op2_cliente.lower() == "s":
                        print("Comprado. Obrigado pela preferência")

                        
                    #Aba para Funcionarios
            elif verifica_codigo == "02":
                    
                    # Recepçao
                    op_funcio = input(f"Ola {nome} suas permissoes como Funcionario são \n 1) Adicionar Produtos \n 2)Remover Produtos \n 3) Atualizar produtos \n 4) Mostrar produtos ")
                    
                    #Adicionar Produtos
                    if op_funcio == "1":
                        adicionar_csv ("Digite o nome do Produto(Digite 0 caso queira cancelar a açao)","Digite o preço do produto",campos_produtos,leitor_Produtos_csv,'Trabalho-Pratico\\produtos.csv')
                    
                    #Remover Produtos
                    elif op_funcio == "2":
                        removedor_csv(leitor_Produtos_csv,campos_produtos,'Trabalho-Pratico\\produtos.csv')


                    # Atualizar produtos
                    elif op_funcio == "3":
                        atualizar_csv(0)
                    
                    # Mostrar produtos
                    elif op_funcio == "4":
                        mostrar_produto()
                    
                    #Aba para gerente
            elif verifica_codigo == "03":
                        op_gerente1 = input(f"Ola {nome} suas permissoes como Gerente são \n 1) Adicionar Produtos/usuarios \n 2)Remover Produtos/usuarios \n 3) Atualizar produtos/usuarios \n 4) Mostrar produtos")
                    
                    #Adicionar
                        if op_gerente1 == "1":
                            op_gerente2 = input("Digite: \n1) Produtos \n2) Usuarios")
                            if op_gerente2 == "1":
                                adicionar_csv ("Digite o nome do Produto(Digite 0 caso queira cancelar a açao)","Digite o preço do produto",campos_produtos,leitor_Produtos_csv,'Trabalho-Pratico\\produtos.csv')
                            elif op_gerente2 == "2":    
                                adicionar_csv ("Digite o nome(Digite 0 caso queira cancelar a açao)","Digite a Senha",campos_contas,leitor_contas_csv,'Trabalho-Pratico\\Contas.csv')

                        #Remover
                        elif op_gerente1 == "2":
                            op_gerente2 = input("Digite: \n1) Produtos \n2) Usuarios")
                            if op_gerente2 == "1":
                                removedor_csv(leitor_Produtos_csv,campos_produtos,'Trabalho-Pratico\\produtos.csv')

                            elif op_gerente2 == "2":   
                                removedor_csv(leitor_contas_csv,campos_contas,'Trabalho-Pratico\\Contas.csv')
                        
                        #Atualizar
                        elif op_gerente1 == "3":
                            op_gerente2 = input("Digite: \n1) Produtos \n2) Usuarios")
                            if op_gerente2 == "1":
                                atualizar_csv(0)
                            elif op_gerente2 == "2":   
                                atualizar_csv(1)
                    
                    #Mostra Produto
                        elif op_gerente1 == "4":
                            mostrar_produto()
                        else:
                            print("Valor invalido")
            else:
                print("Erro permissao nao encontrada no sistema")
                    
                        
    elif op == "2":
        adicionar_csv("Digite seu Nome(Digite 0 caso queira cancelar a açao)","Digite sua Senha",campos_contas,leitor_contas_csv,'Trabalho-Pratico\\Contas.csv')
    
    else:
        print("Valor invalido")
