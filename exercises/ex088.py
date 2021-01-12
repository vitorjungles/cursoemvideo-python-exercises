from time import sleep
from random import randint
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
j = int(input('Quantos jogos quer sortear? '))
print(f'{"-="*3}  SORTEANDO {j} JOGOS  {"-="*3}')
li = []
for c in range(0, j):
    li += [[]]
    for i in range(0, 6):
        s = randint(1, 60)
        while s in li[c]:
            s = randint(1, 60)
        li[c].append(s)
for c in range(len(li)):
    li[c].sort()
    print(f'Jogo {c+1}: {li[c]}')
    sleep(1)
print(f'{"-="*5}{" < BOA SORTE! > "}{"-="*5}')
