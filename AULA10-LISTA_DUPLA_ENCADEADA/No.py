# Definindo a classe No para representar um elemento da lista
class No:
    # Inicializando o no com um valor e dois ponteiros
    def __init__(self, valor):
        self.valor = valor  # O valor do no
        self.proximo = None  # O ponteiro para o próximo no
        self.anterior = None  # O ponteiro para o no anterior
