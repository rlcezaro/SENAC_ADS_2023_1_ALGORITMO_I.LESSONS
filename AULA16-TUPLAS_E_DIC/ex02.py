# Construa um algoritmo que peça ao usuário para informar o nome, a 
# nota01 e a nota02 de um aluno. Guarde estas informações em um 
# dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2] 
# e adicione ao dicionário. Ao final, imprima todos os dados do 
# dicionário.

aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['nota01'] = float(input('Digite a nota 01: '))
aluno['nota02'] = float(input('Digite a nota 02: '))
aluno['media'] = (aluno['nota01'] + aluno['nota02']) / 2
print(aluno,'\n')