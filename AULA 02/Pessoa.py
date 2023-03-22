class Pessoa:

    idade = None

    def __init__(self, nome, idade):
        print('objeto instanciado!')
        # self.nome = 'Maria'
        self.nome = nome
        self.idade = idade
        self.fone = input('digite seu fone: ')

    def imprimir(self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        print('Fone: ', self.fone)
