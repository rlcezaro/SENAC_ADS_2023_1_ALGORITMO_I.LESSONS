# from torre import Torre


class Apartamento:
    def __init__(self, id, numero, torre, vaga):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def cadastrar(self):
        # imprima uma mensagem de confirmação
        print("Apartamento cadastrado com sucesso!")

    def imprimir(self):
        # imprima os dados do apartamento formatados
        print(f"Apartamento {self.id}")
        print(f"Número: {self.numero}")
        print(f"Torre: {self.torre.nome}")
        print(f"Endereço: {self.torre.endereco}")
        if self.vaga > 0:
            print(f"Vaga de garagem: {self.vaga}")
        else:
            print("Sem vaga de garagem")
