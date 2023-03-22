"""
Construir um algoritmo que contenha 3 listas, cada lista contendo:
• Nomes de produtos
• Preços de cada produto
• Quantidades de cada produto
• Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas. As funções devem receber
um parâmetro que será usado para acessar a posição dos itens das listas
que serão impressos ou retirados.
"""

lista_carnes = [('costela', 30.35, 20),
                ('picanha', 85.70, 15), ('file', 90.5, 18)]
lista_feira = [('cebola', 15, 50), ('tomate', 12.35, 100), ('alho', 30.50, 75)]
lista_mercado = [('arroz', 25, 200), ('feijao', 10, 50),
                 ('macarrao', 4.5, 30), ('sal', 3.5, 20)]

while True:
    print('Lista de carnes: \n', lista_carnes)
    print('Lista da feira: \n', lista_feira)
    print('Lista do mercado: \n', lista_mercado)
    escolha = input(
        '''
    
    Escolha uma lista para imprimir um item ou remover:
    1- Mostrar lista de carnes
    2- Mostrar lista da feira
    3- Mostrar mercado
    Escolha: '''
    )

    if escolha == '1':
        pass
    if escolha == '2':
        pass
    if escolha == '3':
        pass
