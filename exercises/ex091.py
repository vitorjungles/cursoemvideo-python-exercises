from random import randint
from time import sleep
from operator import itemgetter
j = {}
for c in range(1, 5):
    j[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in j.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)
for c in range(0, len(ranking)):
    print(f'{c+1:>4}° lugar: {ranking[c][0]} com {ranking[c][1]}.')
    sleep(1)
