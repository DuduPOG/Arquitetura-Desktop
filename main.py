from view import View

#abrir conta
#sair do sistema (UI)


class UI:
    carrinho = None #atributo de classe
    #user = None
    @staticmethod
    def menu():
        #dividir a UI em cliente, admin e visitante
        s = f"\nQual das seguintes opções você deseja executar?\n"
        s += f"\n          1. Inserir cliente;\n"
        s += f"          2. Excluir cliente;\n"
        s += f"          3. Atualizar cliente;\n"
        s += f"          4. Listar clientes;\n"
        s += f"\n          5. Inserir categoria;\n"
        s += f"          6. Excluir categoria;\n"
        s += f"          7. Atualizar categoria;\n"
        s += f"          8. Listar categorias;\n"
        s += f"\n          9. Inserir produto;\n"
        s += f"          10. Excluir produto;\n"
        s += f"          11. Atualizar produto;\n"
        s += f"          12. Listar produtos;\n"
        s += f"\n          13. Iniciar carrinho de compras;\n"
        s += f"          14. Listar os itens do pedido\n"
        s += f"          15. Inserir produto no carrinho;\n"
        s += f"          16. Visualizar carrinho;\n"
        s += f"          17. Confirmar compra;\n"
        s += f"\n          20. Iniciar Login;\n"
        s += f"          21. Excluir Login;\n"
        s += f"          22. Atualizar Login;\n"
        s += f"          23. Listar Logins;\n"
        s += f"\n          100. Encerrar o programa.\n"
        return int(input(f"{s}\nInsira sua escolha: "))
    
    
    @staticmethod
    def main():
        View.cadastrar_admin()
        op = 0
        while op != 100:
            op = UI.menu()
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_excluir()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_listar()
            elif op == 5:
                UI.categoria_inserir()
            elif op == 6:
                UI.categoria_excluir()
            elif op == 7:
                UI.categoria_atualizar()
            elif op == 8:
                UI.categoria_listar()
            elif op == 9:
                UI.produto_inserir()
            elif op == 10:
                UI.produto_excluir()
            elif op == 11:
                UI.produto_atualizar()
            elif op == 12:
                UI.produto_listar()
            elif op == 13:
                UI.iniciar_compra()
            elif op == 14:
                UI.listar_compras()
            elif op == 15:
                UI.inserir_no_carrinho()
            elif op == 16:
                UI.visualizar_carrinho()
            elif op == 17:
                UI.confirmar_compra()
            elif op == 20:
                UI.iniciar_login()
            elif op == 21:
                UI.excluir_login()
            elif op == 22:
                UI.atualizar_login()
            elif op == 23:
                UI.listar_logins()



    #CRUD de cliente
    @staticmethod
    def cliente_inserir():#Create
        nome = input("Informe seu nome: ")
        email = input("Informe seu email: ")
        fone = input("Informe seu telefone: ")
        #x = Cliente(id, nome, email, fone)
        #Clientes.inserir(x)
        View.cliente_inserir(nome, email, fone)

    
    @staticmethod
    def cliente_excluir():#Delete
        UI.cliente_listar
        id = int(input("Informe o ID do cliente que será excluído: "))
        #c = Cliente(id, "", "", "")
        #Clientes.excluir(c)
        View.cliente_excluir(id)


    @staticmethod
    def cliente_atualizar():#Update
        UI.cliente_listar
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe seu novo nome: ")
        email = input("Informe seu novo email: ")
        fone = input("Informe seu novo telefone: ")
        #c = Cliente(id, nome, email, fone)
        #Clientes.atualizar(c)
        View.cliente_atualizar(id, nome, email, fone)


    @staticmethod
    def cliente_listar():#Read
        print("Estes são todos os clientes cadastrados:")
        #for c in Clientes.listar():
         #   print(c)
        for c in View.cliente_listar():
            print(c)


    #CRUD de categoria
    @staticmethod
    def categoria_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para sua categoria: ")
        View.categoria_inserir(desc)

    
    @staticmethod
    def categoria_excluir():#Delete
        UI.categoria_listar
        id = int(input("Informe o ID da categoria que será excluída: "))
        View.categoria_excluir(id)


    @staticmethod
    def categoria_atualizar():#Update
        UI.categoria_listar
        id = int(input("Informe o ID da categoria a ser atualizada: "))
        desc = input("Informe sua nova descrição: ")
        View.categoria_atualizar(id, desc)


    @staticmethod
    def categoria_listar():#Read
        print("Estas são todas as categorias existentes:")
        for c in View.categoria_listar():
            print(c)


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
        UI.produto_listar
        id = int(input("Informe o ID do produto que será excluído: "))
        View.produto_excluir(id)


    @staticmethod
    def produto_atualizar():#Update
        UI.produto_listar
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


    #CRUD de Venda
    @classmethod
    def iniciar_compra(cls):#Create
        View.iniciar_carrinho(cls)


    @staticmethod
    def listar_compras():#Read
        View.listar_carrinho()


    @classmethod
    def visualizar_carrinho(cls):#Read
        View.visualizar_carrinho(cls)


    @classmethod
    def inserir_no_carrinho(cls):
        if cls.carrinho != None:
            UI.produto_listar()
            id_produto = int(input("Informe o id do produto desejado: "))
            qtd = int(input("Informe a quantidade desejada: "))
            View.inserir_no_carrinho(cls.carrinho, id_produto, qtd)
            """
            preco = float(Produtos.listar_id(id_produto).preco)
            vi = VendaItem(0, qtd, preco)
            vi.id_venda = cls.carrinho.id
            vi.id_produto = id_produto
            VendaItens.inserir(vi)
            #atualizar o total da venda (carrinho)
            subtotal = qtd * preco
            cls.carrinho.total += subtotal
            Vendas.atualizar(cls.carrinho)
            """
        else:
            print("Você precisa criar um carrinho primeiro!")
            return

    @classmethod
    def confirmar_compra(cls):
        View.confirmar_compra(cls.carrinho)
    # dever de casa, na venda (carrinho), colocar o atributo carrinho para False
    #percorrer os itens da venda (vendaitem.qtd) e baixar o estoque no cadastro de produto (produto.estoque)


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


UI.main()