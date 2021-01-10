li = [[], []]
for c in range(0, 7):
    n = (int(input(f'Digite o {c+1}º valor: ')))
    if n % 2 == 0:
        li[0].append(n)
    else:
        li[1].append(n)
li[0].sort()
li[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {li[0]}.')
print(f'Os valores ímpares digitados foram: {li[1]}.')
