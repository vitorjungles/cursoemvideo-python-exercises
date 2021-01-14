li = []
co = 0
while True:
    li.append({'nome': str(input('Nome do Jogador: ')), 'gols': [], 'total': 0})
    q = int(input(f'Quantas partidas {li[co]["nome"]} jogou? '))
    for c in range(0, q):
        li[co]['gols'].append(int(input(f'   Quantos gols na partida {c+1}? ')))
        li[co]['total'] += li[co]['gols'][c]
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    co += 1
    if r == 'N':
        break
print('-='*30)
print(f'Cod{"Nome":>5}{"Gols":>15}{"Total":>16}')
print('-'*40)
for pos, c in enumerate(li):
    print(f'{pos:>3} ', end='')
    for d in c.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-' * 40)
    j = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if j == 999:
        break
    if j > len(li)-1:
        print(f'ERRO! Não existe jogador com código {j}. Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {li[j]["nome"]}:')
        for pos, c in enumerate(li[j]['gols']):
            print(f'{"No":>5} jogo {pos+1} fez {c} gols.')
print('<< VOLTE SEMPRE >>')
