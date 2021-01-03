from random import choice
print('Será feito um sorteio entre quatro alunos. BOA SORTE A TODOS!')
n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 3° aluno: '))
n4 = str(input('Digite o nome do 4° aluno: '))
lista = [n1, n2, n3, n4]
sort = choice(lista)
print(f'O aluno escolhido foi {sort}!')
