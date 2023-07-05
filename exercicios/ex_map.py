def concatenar(nome, acao):
    return f'{nome} está {acao}'

nomes = ['Maria', 'Pedro']

acoes = ['dormindo', 'comendo']

frases = map(concatenar, nomes, acoes)

print(frases)

print(list(frases))