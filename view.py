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
    def iniciar_carrinho(carrinho):
        v = Venda(0)
        Vendas.inserir(v)
        carrinho = v
    
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
    def login_inserir(email, senha):
        l = Login(0, email, senha)
        Logins.inserir(l)

    @staticmethod
    def login_excluir(id):
        l = Login(id, "", "")
        Logins.excluir(l)

    @staticmethod
    def login_atualizar(id, email, senha):
        l = Login(id, email, senha)
        Logins.atualizar(l)

    @staticmethod
    def login_listar():
        return Logins.listar()
    

    pass