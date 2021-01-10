li = []
while True:
    li.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'Você digitou {len(li)} elementos.')
li.sort(reverse=True)
print(f'Os valores em ordem decrescente são {li}.')
print('O valor 5 faz parte da lista.' if li.count(5) != 0 else 'O valor 5 não faz parte da lista.')
