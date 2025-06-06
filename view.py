from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas
from vendaitem import VendaItem, VendaItens
from login import Login, Logins


class View:


    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.email == "admin":
                return
        View.cliente_inserir("admin", "admin", "84911223344")


    def cliente_inserir(nome, email, fone):
        x = Cliente(0, nome, email, fone)
        Clientes.inserir(x)
        pass


    def cliente_listar():
        return Clientes.listar()


    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)


    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)
    

    def categoria_inserir(desc):
        c = Categoria(0, desc)
        Categorias.inserir(c)


    def categoria_excluir(id):
        c = Categoria(id, "")
        Categorias.excluir(c)


    def categoria_atualizar(id, desc):
        c = Categoria(id, desc)
        Categorias.atualizar(c)


    def categoria_listar():
        return Categorias.listar()
    

    def produto_inserir(nome, preco, desc, id_categoria):
        p = Produto(0, nome, preco, desc, id_categoria)
        Produtos.inserir(p)


    def produto_excluir(id):
        p = Produto(id, "", "", "", "")
        Produtos.excluir(p)


    def produto_atualizar(id, nome, preco, desc, id_categoria):
        p = Produto(id, nome, preco, desc, id_categoria)
        Produtos.atualizar(p)


    def produto_listar():
        return Produtos.listar()
    

    def iniciar_carrinho(carrinho):
        v = Venda(0)
        Vendas.inserir(v)
        carrinho = v
    

    def listar_carrinho():
        print("Estas são todas as Vendas:")
        for c in Vendas.listar():
            print(c)
    

    def visualizar_carrinho(carrinho):
        if carrinho != None: #if para o verificar as vendas do cliente logado
            print("O produto vai ser inserido nesse carrinho: ", carrinho)
            for item in VendaItens.listar():
                if item.id_venda == carrinho.id:
                    id_produto = item.id_produto
                    descricao = Produtos.listar_id(id_produto).desc
                    print(f"   {descricao} - Quantidade: {item.qtd} - Preço: R$ {item.preco:.2f}")
        else:
            print("Você precisar criar um carrinho primeiro!")
            return
    

    def inserir_no_carrinho(id_carrinho, id_produto, qtd):
        preco = float(Produtos.listar_id(id_produto).preco)
        vi = VendaItem(0, qtd, preco)
        vi.id_venda = id_carrinho
        vi.id_produto = id_produto
        VendaItens.inserir(vi)
        #atualizar o total da venda (carrinho)
        carrinho = Vendas.listar_id(id_carrinho)
        subtotal = qtd * preco
        carrinho.total += subtotal
        Vendas.atualizar(carrinho)


    def confirmar_compra(carrinho):
        if carrinho is None:
            print("Nenhum carrinho iniciado!")
            return
        carrinho.carrinho = False
        Vendas.atualizar(carrinho)
        for item in VendaItens.listar():
            if item.id_venda == carrinho.id:
                produto = Produtos.listar_id(item.id_produto)
                produto.estoque -= item.qtd
                Produtos.atualizar(produto)


    def login_inserir(email, senha):
        l = Login(0, email, senha)
        Logins.inserir(l)


    def login_excluir(id):
        l = Login(id, "", "")
        Logins.excluir(l)


    def login_atualizar(id, email, senha):
        l = Login(id, email, senha)
        Logins.atualizar(l)

    
    def login_listar():
        return Logins.listar()
    

    pass