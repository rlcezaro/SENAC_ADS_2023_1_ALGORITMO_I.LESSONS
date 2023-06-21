from no import No


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            self.fim.proximo = nodo
            nodo.anterior = self.fim
            self.fim = nodo
        self.tamanho += 1
        self.imprimir()
    
    def remover(self, valor):
        tamAtual = self.tamanho
        if self.inicio == None:
            print("Lista Vazia")
            # Lista contendo so um elemento e esse é igual ao valor v
        elif self.inicio.proximo == None and self.inicio.dado == valor:
            self.inicio = None
            self.tamanho = 0

        else:
            # Lista contendo varios elementos e o valor esta na primeira posicao
            if self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            # Lista com varios elementos e o valor nao esta no primeiro
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if aux.dado == valor:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamAtual == self.tamanho:
            print("Valor não encontrado")
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

    def imprimirReverso(self):
        print("--------------------------------")
        if self.inicio == None:
            print("Lista vazia!")
        else:
            aux = self.fim
            while aux:
                print(aux.dado)
                aux = aux.anterior
            print("Tamanho: " + str(self.tamanho))

    