class Produto:
    def __init__(self, name, preco, categoria):
        self.id = None
        self.nome = name
        self.preco = preco
        self.cat = categoria

    def imprimir(self):
        print("------------------------------------------------------")
        print("Nome Produto: ", self.nome)
        print("Preço: ", self.preco)
        print("Categoria: ", self.cat.nome)
