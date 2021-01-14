d = {'nome': str(input('Nome do Jogador: ')).strip().capitalize(), 'gols': [], 'total': 0}
q = int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range(0, q):
    d['gols'].append(int(input(f'   Quantos gols na partida {c}? ')))
    d['total'] += d['gols'][c]
print('-='*30)
print(d)
print('-='*30)
for k, v in d.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {d["nome"]} jogou {len(d["gols"])} partidas.')
for pos, c in enumerate(d["gols"]):
    print(f'{"=>":>6} Na partida {pos}, fez {c} gols.')
print(f'Foi um total de {d["total"]} gols.')
