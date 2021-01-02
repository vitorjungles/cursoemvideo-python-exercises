from random import choice
print('Será feito um sorteio entre quatro alunos, BOA SORTE A TODOS! ')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
sort = choice(lista)
print('O aluno escolhido foi {}! '.format(sort))
