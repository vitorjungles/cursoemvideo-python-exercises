ma = [[], [], []]
sp = ms = ster = 0
for c in range(0, 3):
    while len(ma[c]) < 3:
        ma[c].append(int(input(f'Digite um valor para a posição [{c}, {len(ma[c])}]: ')))
print('-='*30)
for c in range(0, len(ma)):
    for i in range(0, len(ma[c])):
        if ma[c][i] % 2 == 0:
            sp += ma[c][i]
        if c == 1:
            if ma[c][i] > ms:
                ms = ma[c][i]
        if i == 2:
            ster += ma[c][i]
        print(f'[{ma[c][i]:^5}]', end='')
    print('')
print('-='*30)
print(f'A soma dos valores pares é {sp}.')
print(f'A soma dos valores da 3ª coluna é {ster}.')
print(f'O maior valor da 2ª linha é {ms}.')
