ma = [[], [], []]
co = li = 0
for c in range(0, 3):
    while len(ma[c]) < 3:
        ma[c].append(int(input(f'Digite um valor para a posição [{c}, {li}]: ')))
        li += 1
    li = 0
print('-='*30)
for c in range(0, len(ma)):
    for i in range(0, len(ma[c])):
        print(f'[  {ma[c][i]}  ]', end='')
    print('')
