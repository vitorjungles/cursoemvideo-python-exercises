print('='*29)
print('Verificador de números primos')
print('='*29)
num = int(input('Digite um número inteiro para verificar se é primo: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
