# Construa um algoritmo de busca contendo um vetor de números inteiros de 20 posições.
# O algoritmo deve ter duas funções, uma para busca sequencial e outra para busca binária.
# Coloque um contador em cada função para contar as iterações de cada função.
# Peça ao usuário que informe o valor que deseja procurar.
# Então informe ao usuário se este valor existe no vetor e quantas iterações foram necessárias em cada função.
# Caso não encontre no vetor mostrar uma mensagem informando que não foi encontrado e quantas iterações foram necessárias.

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15, 16, 17, 18, 19, 20]
print(vetor)
print("Digite o valor que deseja procurar: ")
valor = int(input())
cont = 0
for i in vetor:
    if i == valor:
        print("O valor está na posição: ", cont)
    cont += 1 # conta as iterações

print("Digite o valor que deseja procurar: ")
valor = int(input())
inicio = 0
fim = len(vetor) - 1 # tamanho do vetor - 1 (posição do último elemento)
meio = (inicio + fim) // 2
cont = 0

while inicio <= fim:
    meio = (inicio + fim) // 2 # calcula o meio do vetor
    if vetor[meio] == valor:
        print("O valor está na posição: ", meio)
        break
    elif vetor[meio] < valor: # se o valor do meio for menor que o valor procurado, o inicio passa a ser o meio + 1
        inicio = meio + 1
    else:
        fim = meio - 1
    cont += 1

if inicio > fim:
    print("Valor não encontrado")

print("Foram necessárias ", cont, " iterações")

# 2. Faça um algoritmo que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
# mostrar apenas uma vez cada valor repetido.
# imprimir quantas iterações foram necessárias para encontrar os valores repetidos.

vetor = [1, 2, 3, 4, 5, 3, 6, 7, 8, 7, 9, 1]
print(vetor)
cont = 0
for i in range(len(vetor)):
    for j in range(i+1, len(vetor)): # i+1 para não comparar o mesmo valor
        if vetor[i] == vetor[j]: # se o valor do vetor na posição i for igual ao valor do vetor na posição j
            print("O valor ", vetor[i], " está na posição: ", i, " e ", j) # imprime o valor e a posição
            cont += 1
print("Foram necessárias ", cont, " iterações")
    