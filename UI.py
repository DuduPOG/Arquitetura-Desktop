from view import View
import sys

class UI():
    # estados : 0 = visitante, 1 = cliente, 2 = administrador
    @staticmethod
    def menu():
        View.cadastrar_admin()
        # Loop para o visitante:
        print("---------------------------------------------")
        print("Bem-vindo ao sistema de Comercio Eletrônico!")
        print("---------------------------------------------")
        print("      \nO que você deseja fazer?\n")
        print("   1. Abrir uma conta")
        print("   2. Entrar no sistema")
        print("   3. Sair do sistema\n")
        op = int(input("Digite o número da opção desejada: "))
        print("")
        UI.main(op)
    
    @staticmethod
    def menu_estado(estado):
        # Loop para o cliente
        while estado == 1:
            print("-------------------------------------------")
            print("      Seja bem vindo, cliente !")
            print("-------------------------------------------")
            print("\nO que você deseja fazer?\n")
            print("   1. Criar um carrinho de compras")
            print("   2. Listar produtos disponiveis")
            print("   3. Inserir produtos no carrinhos")
            print("   4. vizualizar carrinho")
            print("   5. Confirmar compra")
            print("   6. Listar minhas compras")
            print("   7. Deslogar\n")
            op = int(input("Digite o número da opção desejada: "))
            UI.main_estado(1,op)
            
        
        # Loop para o administrador
        # View.cliente_inserir("admin", "admin", "84911223344")
        while estado == 2:
            print("-------------------------------------------")
            print("      Bem-vindo administrador !")
            print("-------------------------------------------")
            print("\nO que você deseja fazer?\n")
            print("   1. Listar as compras")
            print("   2. Inserir cliente")
            print("   3. Excluir cliente")
            print("   4. Atualizar cliente")
            print("   5. listar cliente \n")
            print("   6. Inserir categoria")
            print("   7. Excluir categoria")
            print("   8. Atualizar categoria")
            print("   9. listar categoria \n")
            print("   10. Inserir produto")
            print("   11. Excluir produto")
            print("   12. Atualizar produto")
            print("   13. listar produto")
            print("   14. reajustar o preço dos produtos\n")
            print("   15. Deslogar\n")
            op = int(input("Digite o número da opção desejada: "))
            if not UI.main_estado(estado, op):
                break
#----------------------------------------------------------------      
# Método para gerenciar o menu do visitante

    @staticmethod
    def main(op):
        #View.cadastrar_admin()    # retorna a interação do visitante
        if op == 1:
            UI.cliente_inserir()
            UI.iniciar_login()
            UI.voltar_menu_visita()
        elif op == 2:
            UI.entrar_sistema()
        elif op == 3:
            UI.sair_sistema()

        else:
            print("Opção inválida. Tente novamente.")
            UI.menu()
                  
# metodo para gerenciar o menu do cliente e admin
    @staticmethod
    def main_estado(estado,op):
        if estado == 1:
            op = UI.menu_estado(None)
            if op == 1:
                UI.listar_compras()
                UI.voltar_menu()
            elif op == 2:
                UI.produto_listar()
                UI.voltar_menu()
            elif op == 3:
                UI.inserir_no_carrinho()
                UI.voltar_menu()
            elif op == 4:
                UI.visualizar_carrinho()
                UI.voltar_menu()
            elif op == 5:
                UI.confirmar_compra()
                UI.voltar_menu()
            elif op == 6:
                UI.listar_carrinho()
                UI.voltar_menu()
            elif op == 7:
                UI.deslogar()
            
            else:
                print("Opção inválida. Tente novamente.")
                UI.menu_estado(estado)

            
        if estado == 2:
            if op == 1:
                UI.listar_compras()
                UI.voltar_menu()
            elif op == 2:
                UI.cliente_inserir()
                UI.voltar_menu()
            elif op == 3:
                UI.cliente_excluir()
                UI.voltar_menu()
            elif op == 4:
                UI.cliente_atualizar()
                UI.voltar_menu()
            elif op == 5:
                UI.cliente_listar()
                UI.voltar_menu()
            elif op == 6:
                UI.categoria_inserir()
                UI.voltar_menu()
            elif op == 7:
                UI.categoria_excluir()
                UI.voltar_menu()
            elif op == 8:
                UI.categoria_atualizar()
                UI.voltar_menu()
            elif op == 9:
                UI.categoria_listar()
                UI.voltar_menu()
            elif op == 10:
                UI.produto_inserir()
                UI.voltar_menu()
            elif op == 11:
                UI.produto_excluir()
                UI.voltar_menu()
            elif op == 12:
                UI.produto_atualizar()
                UI.voltar_menu()
            elif op == 13:
                UI.produto_listar()
                UI.voltar_menu()
            elif op == 14:
                UI.reajustar_preco_produto()
                UI.voltar_menu()
            elif op == 15:
                UI.deslogar()
                
            else:
                print("Opção inválida. Tente novamente.")
                UI.menu_estado(estado)
   

#----------------------------------------------------------------------

 #CRUD de cliente
    @staticmethod
    def cliente_inserir():#Create
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        #x = Cliente(id, nome, email, fone)
        #Clientes.inserir(x)
        View.cliente_inserir(nome, email, fone)

    
    @staticmethod
    def cliente_excluir():#Delete
        UI.cliente_listar()
        id = int(input("\nInforme o ID do cliente que será excluído: \n"))
        View.cliente_excluir(id)


    @staticmethod
    def cliente_atualizar():#Update
        UI.cliente_listar()
        id = int(input("\nInforme o ID do cliente a ser atualizado:\n"))
        nome = input("Informe seu novo nome: ")
        email = input("Informe seu novo email: ")
        fone = input("Informe seu novo telefone: ")
        #c = Cliente(id, nome, email, fone)
        #Clientes.atualizar(c)
        View.cliente_atualizar(id, nome, email, fone)


    @staticmethod
    def cliente_listar():#Read
        print("\n-------------------------------------------")
        print("Estes são todos os clientes cadastrados:")
        print("-------------------------------------------\n")
        #for c in Clientes.listar():
         #   print(c)
        for c in View.cliente_listar():
            print(c)
        
            
        

#----------------------------------------------------------------------

    #CRUD de categoria
    @staticmethod
    def categoria_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para sua categoria: ")
        View.categoria_inserir(desc)

    
    @staticmethod
    def categoria_excluir():#Delete
        UI.categoria_listar()
        id = int(input("Informe o ID da categoria que será excluída: "))
        View.categoria_excluir(id)


    @staticmethod
    def categoria_atualizar():#Update
        UI.categoria_listar()
        id = int(input("Informe o ID da categoria a ser atualizada: "))
        desc = input("Informe sua nova descrição: ")
        View.categoria_atualizar(id, desc)


    @staticmethod
    def categoria_listar():#Read
        print("Estas são todas as categorias existentes:")
        for c in View.categoria_listar():
            print(c)

#----------------------------------------------------------------------

    #CRUD de produto
    @staticmethod
    def produto_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para seu produto: ")
        preco = float(input("Informe seu preço: "))
        estoque = int(input("Informe a quantidade no estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID da categoria desejada: "))
        View.produto_inserir(desc, preco, estoque, id_categoria)

    
    @staticmethod
    def produto_excluir():#Delete
        UI.produto_listar()
        id = int(input("Informe o ID do produto que será excluído: "))
        View.produto_excluir(id)


    @staticmethod
    def produto_atualizar():#Update
        UI.produto_listar()
        id = int(input("Informe o ID do produto a ser atualizado: "))
        desc = input("Informe sua nova descrição: ")
        preco = float(input("Informe seu novo preço: "))
        estoque = int(input("Informe sua nova quantidade em estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID do novo produto: "))
        View.produto_atualizar(id, desc, preco, estoque, id_categoria)


    @staticmethod
    def produto_listar():#Read
        print("Estes são todos os produtos disponíveis:")
        for c in View.produto_listar():
            print(c)

    @staticmethod
    def reajustar_preco_produto():
        print("adicionar metodo de reajustar preço")
        

#----------------------------------------------------------------------

    #CRUD de Venda
    @classmethod
    def iniciar_compra(cls):#Create
        View.iniciar_carrinho(cls)


    @staticmethod
    def listar_carrinho():#Read
        View.listar_carrinho()


    @classmethod
    def visualizar_carrinho(cls):#Read
        cls.carrinho = View.visualizar_carrinho(cls)


    @classmethod
    def inserir_no_carrinho(cls):
        if cls.carrinho != None:
            UI.produto_listar()
            id_produto = int(input("Informe o id do produto desejado: "))
            qtd = int(input("Informe a quantidade desejada: "))
            View.inserir_no_carrinho(cls.carrinho, id_produto, qtd)
        else:
            print("Você precisa criar um carrinho primeiro!")
            return
        
    @classmethod
    def listar_minhas_compras(cls):
        print("Estas são todas suas compras feitas:")
        View.listar_minhas_compras(cls)

    @classmethod
    def confirmar_compra(cls):
        View.confirmar_compra(cls.carrinho)
    

#----------------------------------------------------------------------

    #CRUD de login
    @staticmethod
    def iniciar_login():#Create
        user = input("Insira um nome de usuário: ")
        password = input("Insira uma senha para seu login: ")
        View.login_inserir(user, password)

    
    @staticmethod
    def excluir_login():#Delete
        UI.listar_logins
        id = int(input("Informe o ID do login que será excluído: "))
        View.login_excluir(id)


    @staticmethod
    def atualizar_login():#Update
        UI.listar_logins
        id = input("Insira o ID do login que será atualizado: ")
        user = input("Insira um novo nome de usuário: ")
        password = input("Insira uma nova senha: ")
        View.login_atualizar(id, user, password)


    @staticmethod
    def listar_logins():#Read
        print("Estes são todos os logins feitos:")
        for c in View.login_listar():
            print(c)

    @staticmethod
    def entrar_sistema():
        nome = input("Qual seu nome de usuário:")
        senha = input("Qual sua senha :")
        for usuario in View.login_listar():
            if usuario.get_user() == nome and usuario.get_password() == senha:
                if nome == "admin" and senha == "admin":
                    estado = 2
                else:
                    estado = 1
                UI.menu_estado(estado)
                return  # Interrompe após login bem-sucedido

        print("\nNome ou senha inválidos, tente novamente.\n")
        UI.menu()  # Volta para o menu de login

    @staticmethod
    def deslogar():
        print("Deslogando...")
        estado = 0
        UI.main(estado)

    @staticmethod
    def sair_sistema():
        print("saindo do sistema...")
        sys.exit()

#admin 
    @staticmethod
    def listar_compras():
        View.listar_carrinho()

    @staticmethod
    def voltar_menu():
        resposta = str(input("\nDeseja voltar ao menu? (s/n)\n"))
        if resposta == "s" :
            UI.menu_estado(2)
        elif resposta == "n":
            UI.sair_sistema()
        else:
            print("\nResposta invalida")
            UI.voltar_menu()
    
    @staticmethod
    def voltar_menu_visita():
            print("\nConta criada com sucesso")
            UI.menu()

UI.menu()
        