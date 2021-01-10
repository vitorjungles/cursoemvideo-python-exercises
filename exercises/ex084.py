li = []
p = []
cont = 0
while True:
    li.append(str(input('Nome: ')))
    li.append(float(input('Peso: ')))
    p.append(li[:])
    r = ' '
    cont += 1
    li.clear()
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(p)} pessoas.')
