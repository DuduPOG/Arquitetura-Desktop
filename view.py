from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas
from vendaitem import VendaItem, VendaItens
from login import Login, Logins


class View:

    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "84911223344")

    @staticmethod
    def cliente_inserir(nome, email, fone):
        x = Cliente(0, nome, email, fone)
        Clientes.inserir(x)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        cliente = Clientes.listar_id(id)
        if cliente is not None:
            Clientes.excluir(cliente)
        else:
            print("Cliente não encontrado!")
            return
    
    @staticmethod
    def categoria_inserir(desc):
        c = Categoria(0, desc)
        Categorias.inserir(c)

    @staticmethod
    def categoria_excluir(id):
        categoria = Categorias.listar_id(id)
        if categoria is not None:
            Categorias.excluir(categoria)
        else:
            print("Categoria não encontrada!")
            return

    @staticmethod
    def categoria_atualizar(id, desc):
        c = Categoria(id, desc)
        Categorias.atualizar(c)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    
    @staticmethod
    def produto_inserir(nome, preco, desc, id_categoria):
        p = Produto(0, nome, preco, desc, id_categoria)
        Produtos.inserir(p)

    @staticmethod
    def produto_excluir(id):
        produto = Produtos.listar_id(id)
        if produto is not None:
            Produtos.excluir(produto)
        else:
            print("Produto não encontrado!")
            return

    @staticmethod
    def produto_atualizar(id, nome, preco, desc, id_categoria):
        p = Produto(id, nome, preco, desc, id_categoria)
        Produtos.atualizar(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    
    @staticmethod
    def iniciar_carrinho():
        carrinho = Venda(0)
        Vendas.inserir(carrinho)
        print("\nCarrinho iniciado com sucesso!")
        return carrinho
    
    @staticmethod
    def listar_carrinho():
        print("Estas são todas as Vendas:")
        for c in Vendas.listar():
            print(c)
    
    @staticmethod
    def visualizar_carrinho(carrinho):
        if carrinho is not None:
            print("O produto vai ser inserido nesse carrinho: ", carrinho)
            for item in VendaItens.listar():
                if item.get_id_venda() == carrinho.get_id():
                    id_produto = item.get_id_produto()
                    produto = Produtos.listar_id(id_produto)
                    if produto is not None:
                        descricao = produto.get_desc()
                        print(f"   {descricao} - Quantidade: {item.get_qtd()} - Preço: R$ {item.get_preco():.2f}")
                    else:
                        descricao = "(Produto não encontrado)"
        else:
            print("Você precisar criar um carrinho primeiro!")
            return
    
    @staticmethod
    def inserir_no_carrinho(carrinho, id_produto, qtd):
        produto = Produtos.listar_id(id_produto)
        if produto is None:
            print("Produto não encontrado!")
            return
        preco = float(produto.get_preco())
        vi = VendaItem(0, qtd, preco)
        vi.set_id_venda(carrinho.get_id())
        vi.set_id_produto(id_produto)
        VendaItens.inserir(vi)
        # atualizar o total da venda (carrinho)
        subtotal = qtd * preco
        carrinho.set_total(carrinho.get_total() + subtotal)
        Vendas.atualizar(carrinho)

    @staticmethod
    def listar_minhas_compras(cliente):
        for venda in Vendas.listar():
            if venda.get_id_cliente() == cliente.get_id():
                print(f"Venda ID: {venda.get_id()}, Total: R$ {venda.get_total():.2f}, Status: {'Finalizada' if not venda.get_carrinho() else 'Em aberto'}")

    @staticmethod
    def confirmar_compra(carrinho):
        if carrinho is None:
            print("Nenhum carrinho iniciado!")
            return
        carrinho.set_carrinho(False)
        Vendas.atualizar(carrinho)
        for item in VendaItens.listar():
            if item.get_id_venda() == carrinho.get_id():
                produto = Produtos.listar_id(item.get_id_produto())
                if produto is not None:
                    produto.set_estoque(produto.get_estoque() - item.get_qtd())
                    Produtos.atualizar(produto)

    @staticmethod
    def desconfirmar_compra(carrinho):
        if carrinho.get_carrinho() is True:
            print("Esta compra ainda não foi acabada!")
            return
        carrinho.set_carrinho(True)
        Vendas.atualizar(carrinho)
        for item in VendaItens.listar():
            if item.get_id_venda() == carrinho.get_id():
                produto = Produtos.listar_id(item.get_id_produto())
                if produto is not None:
                    produto.set_estoque(produto.get_estoque() + item.get_qtd())
                    Produtos.atualizar(produto)

    @staticmethod
    def produto_reajustar_preco(produto, novo_preco):
        produto = Produtos.listar_id(produto)
        if produto is not None:
            produto.set_preco(novo_preco)
            Produtos.atualizar(produto)
        else:
            print("Produto não encontrado!")
            return

    @staticmethod
    def login_inserir(email, senha):
        l = Login(0, email, senha)
        Logins.inserir(l)

    @staticmethod
    def login_excluir(id):
        login = Logins.listar_id(id)
        if login is not None:
            Clientes.excluir(login)
        else:
            print("login não encontrado!")
            return
        


    @staticmethod
    def login_atualizar(id, email, senha):
        l = Login(id, email, senha)
        Logins.atualizar(l)

    @staticmethod
    def login_listar():
        return Logins.listar()
    

    pass