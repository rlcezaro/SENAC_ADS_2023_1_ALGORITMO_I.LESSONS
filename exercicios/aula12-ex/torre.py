class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        # imprima uma mensagem de confirmação
        print("Torre cadastrada com sucesso!")

    def imprimir(self):
        # imprima os dados da torre formatados
        print(f"Torre {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
