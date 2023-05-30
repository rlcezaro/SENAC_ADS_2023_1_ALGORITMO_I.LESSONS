from no import No


class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("--------------------------------")
        if self.inicio == None:
            print("Lista vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.proximo
            print("Tamanho: " + str(self.tamanho))

    def removerDoFim(self):
        if self.inicio == None:
            print("Lista vazia!")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.tamanho = 0
        else:
            anterior = self.inicio
            aux = self.inicio
            while aux.proximo:
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None
            self.tamanho -= 1
            self.imprimir()
