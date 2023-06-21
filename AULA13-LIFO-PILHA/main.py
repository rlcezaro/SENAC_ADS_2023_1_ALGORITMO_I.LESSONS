from livro import Livro # Importa a classe livro do arquivo livro.py
from pilha import Pilha # Importa a classe pilha do arquivo pilha.py

pilha = Pilha() # Cria uma instância da classe pilha

# Cria nove instâncias da classe livro com diferentes atributos
livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)
livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 263)
livro3 = Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 576)
livro4 = Livro("Dom Quixote", "Miguel de Cervantes", 1056)
livro5 = Livro("O Alquimista", "Paulo Coelho", 208)
livro6 = Livro("A Revolução dos Bichos", "George Orwell", 144)

# Adiciona os livros na pilha usando o método empilhar
pilha.empilhar(livro1)
pilha.empilhar(livro2)
pilha.empilhar(livro3)
pilha.empilhar(livro4)
pilha.empilhar(livro5)
pilha.empilhar(livro6)

# Imprime os livros da pilha usando o método imprimir
print("Lista inicial:")
pilha.imprimir()

print("Desempilhando...") # Imprime uma mensagem indicando que vai desempilhar

# Remove um livro do topo da pilha usando o método desempilhar e imprime o livro removido
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")
# Imprime os livros da pilha novamente
print("Lista atualizada:")
pilha.imprimir()

print("Desempilhando...") # Imprime uma mensagem indicando que vai desempilhar

# Remove um livro do topo da pilha usando o método desempilhar e imprime o livro removido
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")
# Imprime os livros da pilha novamente
print("Lista atualizada:")
pilha.imprimir()
print("--------------------")
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")
livro_removido = pilha.desempilhar()
print(f"Livro removido: {livro_removido}")
print("--------------------")