class Pessoa:
    def __init__(self, name, fone, city):
        self.id = None
        self.nome = name
        self.fone = fone
        self.cidade = city

    def imprimir(self):
        print("------------------------------------------------------")
        print("Nome: ", self.nome)
        print("Telefone: ", self.fone)
        print("Cidade: ", self.cidade.nome)
