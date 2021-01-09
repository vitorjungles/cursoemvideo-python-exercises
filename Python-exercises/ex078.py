li = []
for c in range(0, 5):
    li.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-'*30)
print(f'Você digitou os valores {li}.')
print(f'O maior valor digitado foi {max(li)} nas posições ', end='')
for p, i in enumerate(li):
    if i == max(li):
        print(p, end='... ')
print(f'\nO menor valor digitado foi {min(li)} nas posições ', end='')
for p, i in enumerate(li):
    if i == min(li):
        print(p, end='... ')
