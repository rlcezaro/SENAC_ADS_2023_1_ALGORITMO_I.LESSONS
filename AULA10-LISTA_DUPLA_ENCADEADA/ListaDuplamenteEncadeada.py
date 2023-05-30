from No import No

# Definindo a classe ListaDuplamenteEncadeada para representar a lista
class ListaDuplamenteEncadeada:
    # Inicializando a lista com um no cabeca e um no cauda
    def __init__(self):
        self.cabeca = No(None)  # O no cabeca não tem valor
        self.cauda = No(None)  # O no cauda não tem valor
        self.cabeca.proximo = self.cauda  # O próximo do cabeca é o cauda
        self.cauda.anterior = self.cabeca  # O anterior do cauda é o cabeca
        self.tamanho = 0  # O tamanho da lista é zero

    # Definindo a função para inserir elementos em ordem alfabética
    def inserir(self, valor):
        # Criando um novo no com o valor dado
        novo_no = No(valor)
        # Percorrendo a lista a partir do cabeca
        atual = self.cabeca
        # Enquanto o próximo do atual não for o cauda e o valor do próximo for menor que o valor dado
        while atual.proximo != self.cauda and atual.proximo.valor < valor:
            # Avançando o atual para o próximo
            atual = atual.proximo
        # Inserindo o novo no entre o atual e o próximo do atual
        novo_no.proximo = atual.proximo  # O próximo do novo no é o próximo do atual
        novo_no.anterior = atual  # O anterior do novo no é o atual
        atual.proximo.anterior = novo_no  # O anterior do próximo do atual é o novo no
        atual.proximo = novo_no  # O próximo do atual é o novo no
        # Incrementando o tamanho da lista
        self.tamanho += 1

    # Definindo a função para imprimir os elementos da lista
    def imprimir(self):
        # Percorrendo a lista a partir do primeiro elemento (o próximo do cabeca)
        atual = self.cabeca.proximo
        # Enquanto o atual não for o cauda
        while atual != self.cauda:
            # Imprimindo o valor do atual
            print(atual.valor)
            # Avançando o atual para o próximo
            atual = atual.proximo

    # Definindo a função para imprimir os elementos na ordem inversa
    def imprimir_inverso(self):
        # Percorrendo a lista a partir do último elemento (o anterior do cauda)
        atual = self.cauda.anterior
        # Enquanto o atual não for o cabeca
        while atual != self.cabeca:
            # Imprimindo o valor do atual
            print(atual.valor)
            # Retrocedendo o atual para o anterior
            atual = atual.anterior
