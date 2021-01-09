li = list()
c = 0
while True:
    n = int(input('Digite um valor: '))
    if n in li:
        print('Valor duplicado. Não adicionado.')
    else:
        li.append(n)
        print('Valor adicionado com sucesso.')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
li.sort()
print(f'Você digitou os valores {li}.')
