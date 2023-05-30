from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

# Criando uma instância da lista duplamente encadeada
lista = ListaDuplamenteEncadeada()
# Inserindo alguns elementos em ordem alfabética
lista.inserir("Ana")
lista.inserir("Carlos")
lista.inserir("Bia")
lista.inserir("Daniel")
# Imprimindo os elementos da lista
print("Elementos da lista:")
lista.imprimir()
# Imprimindo os elementos na ordem inversa
print("Elementos na ordem inversa:")
lista.imprimir_inverso()
