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
            op = input("Digite o número da opção desejada: ")
            UI.menu(estado, op)
        
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
            interacao_administrador = int(input("Digite o número da opção desejada: "))
            UI.menu(estado, interacao_administrador)
        
#----------------------------------------------------------------      
# Método para gerenciar o menu de acordo com o estado e a opção escolhida

    @staticmethod
    def menu(estado, op):
        if estado == 0:
            if op == 1:
                UI.Cliente_Inserir()
            elif op == 2:
                UI.verificar_estado()
            else:
                print("Opção inválida. Tente novamente.")
                UI.main(0)        
        
        if estado == 1:
            if op == 1:
                UI.Carrinho_Inserir()
            elif op == 2:
                UI.produto_listar()
            elif op == 3:
                UI.inserir_no_carrinho()
            elif op == 4:
                UI.visualizar_carrinho()
            elif op == 5:
                UI.confirmar_compra()
            elif op == 6:
                UI.listar_carrinho()
            elif op == 7:
                UI.deslogar()
            else:
                print("Opção inválida. Tente novamente.")
                UI.main(estado)
            
        if estado == 2:
            if op == 1:
                UI.Carrinho_listar()
            elif op == 2:
                UI.Cliente_Inserir()
            elif op == 3:
                UI.Cliente_excluir()
            elif op == 4:
                 UI.Cliente_atualizar()
            elif op == 5:
                UI.Cliente_listar()
            elif op == 6:
                UI.Categoria_inserir()
            elif op == 7:
                UI.Categoria_excluir()
            elif op == 8:
                UI.Categoria_atualizar()
            elif op == 9:
                UI.Categoria_listar()
            elif op == 10:
                UI.Produto_inserir()
            elif op == 11:
                UI.Produto_excluir()
            elif op == 12:
                UI.Produto_atualizar()
            elif op == 13:
                UI.Produto_listar()
            elif op == 14:
                UI.reajustar_preco_produtos()
            elif op == 15:
                UI.deslogar()
            else:
                print("Opção inválida. Tente novamente.")
                UI.main(estado)
        
        


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
    def verificar_estado():
        print("Para entrar no sistema, por favor, insira como você quer entrar:\n1. Cliente\n2. Administrador")
        estado = int(input("Digite o número da opção desejada: "))
        if estado == 1:
            print("Você escolheu entrar como cliente.")
            return 1
        elif estado == 2:
            print("Você escolheu entrar como administrador.")
            return 2
        

    @staticmethod
    def deslogar():
        print("Deslogando...")
        estado = 0
        UI.main(estado)

"""
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

#----------------------------------------------------------------

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