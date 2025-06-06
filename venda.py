from datetime import datetime
import json

class Venda:

    def __init__(self, id):
        self.id = id
        self.data = datetime.now()
        self.carrinho = True
        self.total = 0
        self.id_cliente = 0


    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
        dic["carrinho"] = self.__carrinho
        dic["total"] = self.__total
        dic["id_cliente"] = self.__id_cliente
        return dic

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime("%d/%m/%Y %H:%M")} - {self.__carrinho} - {self.__total} - {self.__id_cliente}"
    

class Vendas:

    objetos = []


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            maior = max(cliente.id for cliente in cls.objetos)
            obj.id = maior + 1
        else:
            obj.id = 0
        cls.objetos.append(obj)
        cls.salvar()


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
    
    
    @classmethod
    def abrir(cls):
        cls.objetos = []    
        with open("vendas.json", mode="r") as arquivo:
            s = json.load(arquivo)
            for dic in s: 
                c = Venda(dic["id"])
                c.data = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
                c.carrinho = dic["carrinho"]
                c.total = dic["total"]
                c.id_cliente = dic["id_cliente"]
                cls.objetos.append(c)


    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Venda.to_json)