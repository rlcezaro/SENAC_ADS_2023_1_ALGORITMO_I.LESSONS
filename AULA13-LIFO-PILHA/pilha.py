class Pilha:
    # Construtor da classe pilha
    def __init__(self):
        # Atributos da classe pilha
        self.topo = None # Referência para o livro no topo da pilha
        self.tamanho = 0 # Número de livros na pilha

    # Método para verificar se a pilha está vazia
    def vazia(self):
        return self.topo is None

    # Método para adicionar um livro no topo da pilha
    def empilhar(self, livro):
        livro.proximo = self.topo # O próximo do livro é o antigo topo da pilha
        self.topo = livro # O novo topo da pilha é o livro adicionado
        self.tamanho += 1 # Incrementa o tamanho da pilha

    # Método para remover um livro do topo da pilha
    def desempilhar(self):
        if not self.vazia(): # Se a pilha não estiver vazia
            livro = self.topo # Guarda o livro do topo em uma variável
            self.topo = livro.proximo # O novo topo é o próximo do antigo topo
            livro.proximo = None # O próximo do livro removido é nulo
            self.tamanho -= 1 # Decrementa o tamanho da pilha
            return livro # Retorna o livro removido
        else: # Se a pilha estiver vazia
            return None # Retorna nulo

    # Método para imprimir os livros da pilha
    def imprimir(self):
        atual = self.topo # Começa pelo topo da pilha
        while atual is not None: # Enquanto não chegar ao fim da pilha
            print(atual) # Imprime o livro atual            
            atual = atual.proximo # Vai para o próximo livro na pilha
        print(f"Numero de livros: {self.tamanho}") # Imprime o tamanho da pilha
