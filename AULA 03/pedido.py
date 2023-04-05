class Pedido:
    def __init__(self, endereco, cliente):
        self.id = None
        self.end = endereco
        self.cliente = cliente
        self.produtos = []

    def addProduto(self, produto):
        self.produtos.append(produto)
        soma = 0
        for prod in self.produtos:
            soma += prod.preco
        return soma

    def imprimir(self):
        print("Pedido: ")
        print("Endereco: ", self.end)
        print("Cliente: ", self.cliente.nome)
        print("Cliente: ", self.cliente.cidade.nome)
        print("Produtos do Pedidos: ")
        if len(self.produtos) == 0:
            print("Pedido vazio: ")
        else:
            soma = 0
            for prod in self.produtos:
                print("Produtos: ", prod.nome)
                print("Preco: ", prod.preco)
                print("Categoria: ", prod.cat.nome)
            print("Total: ", soma)
            print("-------------------")

    # def imprimir(self):

    # def addProdutos(self): float com a soma do valor dos produtos
