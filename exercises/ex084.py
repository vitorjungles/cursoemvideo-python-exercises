li = []
p = []
maior = menor = 0.0
while True:
    li.append(str(input('Nome: ')))
    li.append(float(input('Peso: ')))
    p.append(li[:])
    li.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(p)} pessoas.')
for c in range(0, len(p)):
    if c == 0 or p[c][1] > maior:
        maior = p[c][1]
    if c == 0 or p[c][1] < menor:
        menor = p[c][1]
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in range(0, len(p)):
    if p[c][1] == maior:
        print(p[c][0], end=', ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for c in range(0, len(p)):
    if p[c][1] == menor:
        print(p[c][0], end=', ')
