li = []
par = []
im = []
c = 0
while True:
    li.append(int(input('Digite um valor: ')))
    if li[c] % 2 == 0:
        par.append(li[c])
    else:
        im.append(li[c])
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    c += 1
    if r == 'N':
        break
print('-='*30)
print(f'A lista completa é {li}.')
print(f'A lista de pares é {par}.')
print(f'A lista de ímpares é {im}.')
