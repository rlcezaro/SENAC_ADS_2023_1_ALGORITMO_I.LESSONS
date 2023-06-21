class Livro:
    # Construtor da classe livro
    def __init__(self, titulo, autor, nr_pags):
        # Atributos da classe livro
        self.titulo = titulo # Título do livro
        self.autor = autor # Autor do livro
        self.nr_pags = nr_pags # Número de páginas do livro
        self.proximo = None # Referência para o próximo livro na pilha

    # Método para retornar uma representação em string do livro
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.nr_pags} páginas)"
