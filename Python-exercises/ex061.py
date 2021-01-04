texto = str('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 59)
print(f"{texto:^60}")
print('=' * 59)
num = int(input('1° Termo: '))
razao = int(input('Razão: '))
termo = num
c = 1
while c <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    c += 1
print('ACABOU')
