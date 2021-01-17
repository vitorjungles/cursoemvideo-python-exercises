from random import randint
from time import sleep
numeros = []


def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[c], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lst):
    s = 0
    for c in lst:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {numeros}, temos {s}.')


sorteia(numeros)
somapar(numeros)
