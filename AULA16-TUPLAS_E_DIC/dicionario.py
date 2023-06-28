filho1 = {'nome': 'Julia', 'idade': 14} # Dicionário com chave e valor
filho2 = {'nome': 'Nicolas', 'idade': 21}
filho3 = {'nome': 'Fernando', 'idade': 65}

print(filho1) # Imprimindo o dicionário
print("Nome: ", filho1['nome']) # Acessando o valor da chave 'nome'
print(filho1.keys()) # Imprimindo as chaves do dicionário
print(filho1.values()) # Imprimindo os valores do dicionário

print("----------------------------------")

for chave, valor in filho1.items(): # Imprimindo as chaves e valores do dicionário
    print(chave, valor) # Imprimindo as chaves e valores do dicionário

for chave in filho1.keys(): # Imprimindo as chaves do dicionário
    print(chave, " - ",filho1[chave]) # Imprimindo as chaves e valores do dicionário

print("----------------------------------")
prole = filho1, filho2 # Tupla de dicionários
print(prole) # Imprimindo a tupla de dicionários
print(prole[0]) # Imprimindo o primeiro dicionário da tupla
# prole[0]=filho3 # Erro, tuplas são imutáveis
filho1['nome']='Juliana' # Alterando o valor da chave 'nome' do dicionário filho1
print(prole) # Imprimindo a tupla de dicionários
filho2['nome']='Nicolau' # Alterando o valor da chave 'nome' do dicionário filho2
print(prole) # Imprimindo a tupla de dicionários