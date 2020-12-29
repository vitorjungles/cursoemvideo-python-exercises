s = 0
cont = 0
print('=' * 29)
print('Somando seis números inteiros')
print('=' * 29)
for c in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('Você digitou {} valores PARES e a soma foi {}.'.format(cont, s))
