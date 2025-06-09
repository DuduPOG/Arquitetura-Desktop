from view import View

class UI():
    # estados : 0 = visitante, 1 = cliente, 2 = administrador
    @staticmethod
    def main(estado):
        View.cadastrar_admin()
        estado = 0
        # Loop para o visitante
        while estado == 0:
            print("\nBem-vindo ao sistema de Comercio Eletrônico!")
            print("\nO que você deseja fazer?")
            print("1. Abrir uma conta")
            print("2. Entrar no sistema\n")
            interacao_visitante = input("Digite o número da opção desejada: ")
            UI.menu(estado, interacao_visitante)
        
        # Loop para o cliente
        while estado == 1:
            print("\nSeja bem vindo!\n")
            print("O que você deseja fazer?")
            print("1. Criar um carrinho de compras")
            print("2. Listar produtos disponiveis")
            print("3. Inserir produtos no carrinhos")
            print("4. vizualizar carrinho")
            print("5. Confirmar compra")
            print("6. Listar minhas compras")
            print("7. Sair do sistema\n")
            interacao_cliente = input("Digite o número da opção desejada: ")
            UI.menu(estado , interacao_cliente)
        
        # Loop para o administrador
        # View.cliente_inserir("admin", "admin", "84911223344")
        while estado == 2:
            print("\nBem-vindo administrador!\n")
            print("O que você deseja fazer?")
            print("1. Listar as compras")
            print("2. Inserir cliente")
            print("3. Excluir cliente")
            print("4. Atualizar cliente")
            print("5. listar cliente")
            print("\n6. Inserir categoria")
            print("7. Excluir categoria")
            print("8. Atualizar categoria")
            print("9. listar categoria")
            print("\n10. Inserir produto")
            print("11. Excluir produto")
            print("12. Atualizar produto")
            print("13. listar produto")
            print("14. reajustar o preço dos produtos\n")
            print("15. Sair do sistema\n")
            interacao_administrador = input("Digite o número da opção desejada: ")
            UI.menu(estado , interacao_administrador)
        
#----------------------------------------------------------------      
# Método para gerenciar o menu de acordo com o estado e a opção escolhida

    @staticmethod
    def menu(estado, op):
        opcao = op
        if estado == 0:
            if opcao == "1":
                return UI.Cliente_Inserir()
            elif opcao == "2":
                return UI.login()
            else:
                print("Opção inválida. Tente novamente.")
                return UI.main(0)        
        
        if estado == 1:
            if opcao == "1":
                return UI.Carrinho_Inserir()
            elif opcao == "2":
                return UI.produto_listar()
            elif opcao == "3":
                return UI.inserir_no_carrinho()
            elif opcao == "4":
                return UI.visualizar_carrinho()
            elif opcao == "5":
                return UI.confirmar_compra()
            elif opcao == "6":
                return UI.listar_carrinho()
            elif opcao == "7":
                return UI.deslogar()
            else:
                print("Opção inválida. Tente novamente.")
                return UI.main(estado)
            
        if estado == 2:
            if opcao == "1":
                return UI.Carrinho_listar()
            elif opcao == "2":
                return UI.Cliente_Inserir()
            elif opcao == "3":
                return UI.Cliente_excluir()
            elif opcao == "4":
                return UI.Cliente_atualizar()
            elif opcao == "5":
                return UI.Cliente_listar()
            elif opcao == "6":
                return UI.Categoria_inserir()
            elif opcao == "7":
                return UI.Categoria_excluir()
            elif opcao == "8":
                return UI.Categoria_atualizar()
            elif opcao == "9":
                return UI.Categoria_listar()
            elif opcao == "10":
                return UI.Produto_inserir()
            elif opcao == "11":
                return UI.Produto_excluir()
            elif opcao == "12":
                return UI.Produto_atualizar()
            elif opcao == "13":
                return UI.Produto_listar()
            elif opcao == "14":
                return UI.reajustar_preco_produtos()
            elif opcao == "15":
                return UI.deslogar()
            else:
                print("Opção inválida. Tente novamente.")
                return UI.main(estado)
        
        


#----------------------------------------------------------------
    @staticmethod
    def Cliente_listar():
        print("Estes são todos os clientes cadastrados:")
        #for c in Clientes.listar():
         #   print(c)
        for c in View.cliente_listar():
            print(c)
    
    @staticmethod
    def Cliente_Inserir():
        print("Para criar uma conta, por favor, insira os seguintes dados:")
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        telefone = input("Digite seu telefone: ")
        print("Conta criada com sucesso!")
        View.Cliente_Inserir(nome, email, telefone)
       
    
    @staticmethod
    def Cliente_excluir():#Delete
        UI.cliente_listar
        id = int(input("Informe o ID do cliente que será excluído: "))
        #c = Cliente(id, "", "", "")
        #Clientes.excluir(c)
        View.cliente_excluir(id, "", "", "")


    @staticmethod
    def Cliente_atualizar():#Update
        UI.cliente_listar
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe seu novo nome: ")
        email = input("Informe seu novo email: ")
        fone = input("Informe seu novo telefone: ")
        #c = Cliente(id, nome, email, fone)
        #Clientes.atualizar(c)
        View.cliente_atualizar(id, nome, email, fone)

#----------------------------------------------------------------
    @staticmethod
    def Categoria_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para sua categoria: ")
        View.categoria_inserir(desc)

    
    @staticmethod
    def Categoria_excluir():#Delete
        UI.categoria_listar
        id = int(input("Informe o ID da categoria que será excluída: "))
        View.categoria_excluir(id, "")


    @staticmethod
    def Categoria_atualizar():#Update
        UI.categoria_listar
        id = int(input("Informe o ID da categoria a ser atualizada: "))
        desc = input("Informe sua nova descrição: ")
        View.categoria_atualizar(id, desc)


    @staticmethod
    def Categoria_listar():#Read
        print("Estas são todas as categorias existentes:")
        for c in View.categoria_listar():
            print(c)

#----------------------------------------------------------------
    @staticmethod
    def Produto_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para seu produto: ")
        preco = float(input("Informe seu preço: "))
        estoque = int(input("Informe a quantidade no estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID da categoria desejada: "))
        View.produto_inserir(desc, preco, estoque, id_categoria)

    
    @staticmethod
    def Produto_excluir():#Delete
        UI.produto_listar
        id = int(input("Informe o ID do produto que será excluído: "))
        View.produto_excluir(id, "", "", "", "")


    @staticmethod
    def Produto_atualizar():#Update
        UI.produto_listar
        id = int(input("Informe o ID do produto a ser atualizado: "))
        desc = input("Informe sua nova descrição: ")
        preco = float(input("Informe seu novo preço: "))
        estoque = int(input("Informe sua nova quantidade em estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID do novo produto: "))
        View.produto_atualizar(id, desc, preco, estoque, id_categoria)


    @staticmethod
    def Produto_listar():#Read
        print("Estes são todos os produtos disponíveis:")
        for c in View.produto_listar():
            print(c)
#----------------------------------------------------------------
    @staticmethod
    def login_inserir(email,senha):
        View.login_inserir(email,senha)
    
    @staticmethod
    def login():
        print("Para entrar no sistema, por favor, insira seus dados:")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        # Verifica se o email e senha estão corretos
        for usuario in View.login_listar():
            if usuario['email'] == email and usuario['senha'] == senha:
                print("Login realizado com sucesso!")
                estado = 1
                UI.main(estado) 
             
            elif email == "admin" and senha == "84911223344":
                estado = 2
                print("Login realizado com sucesso!")
                UI.main(estado)  
            
            else:
                print("Email ou senha incorretos. Tente novamente.")
                UI.main(estado)
            
    @staticmethod
    def deslogar():
        print("Deslogando...")
        estado = 0
        UI.main(estado)
#----------------------------------------------------------------
"""
    @staticmethod   
    def Carrinho_Inserir():
        View.iniciar_carrinho()
    
    @staticmethod
    def produto_listar():
        View.produto_listar()
    
    @staticmethod
    def Carrinho_Listar():
        View.listar_carrinho
    
    @staticmethod
    def inserir_no_carrinho():
        print("Para inserir produtos no carrinho, por favor, insira os seguintes dados:")
        id_produto = input("Digite o ID do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        View.inserir_no_carrinho(id_produto, quantidade)
    
    @staticmethod
    def visualizar_carrinho():
        View.visualizar_carrinho()
    
    @staticmethod
    def confirmar_compra():
        View.confirmar_compra()
    


#----------------------------------------------------------------
    @staticmethod
    def listar_as_compras():
        for carrinho in View.listar_carrinho:
            print(f"Carrinho ID: {carrinho.get_id}, Data do carrinho:{carrinho.get_data().strftime('%d/%m/%Y %H:%M')},Cliente ID: {carrinho.get_id_cliente}, Total: {carrinho.get_total},o carrinho esta ativo: {carrinho.get_carrinho}")

    @staticmethod
    def manter_cadastros_produtos():
   
    @staticmethod
    def manter_cadastros_clientes():

    @staticmethod
    def manter_cadastros_categorias():
        
    @staticmethod
    def reajustar_preco_produtos():
    """
UI.main(0)