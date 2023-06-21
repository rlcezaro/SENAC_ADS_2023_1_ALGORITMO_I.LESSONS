from queue import Queue
from apartamento import Apartamento


class FilaDeEspera:
    def __init__(self):
        self.fila = Queue()

    def adicionar_apartamento(self, apartamento):
        # implemente a lógica para adicionar um apartamento na fila
        self.fila.put(apartamento)

    def retirar_apartamento(self):
        # implemente a lógica para retirar um apartamento da fila e informar o número de vaga que ele receberá
        if not self.fila.empty():
            apartamento = self.fila.get()
            # atribua um número de vaga ao apartamento
            return apartamento
        else:
            return None

    def imprimir_fila(self):
        # implemente a lógica para imprimir os apartamentos na fila de espera
        for apartamento in list(self.fila.queue):
            apartamento.imprimir()
