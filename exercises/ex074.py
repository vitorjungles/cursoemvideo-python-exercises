from random import randint
maior = menor = 0
t = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for c in range(0, len(t)):
    if c == 0:
        maior = t[c]
        menor = t[c]
    if t[c] > maior:
        maior = t[c]
    if t[c] < menor:
        menor = t[c]
    print(t[c], end=' ')
print(f'\nO maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')
