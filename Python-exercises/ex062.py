texto = str('TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 59)
print(f"{texto:^60}")
print('=' * 59)
num = int(input('1° Termo: '))
razao = int(input('Razão: '))
termo = num
mais = 10
total = 0
c = 1
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        c += 1
    print('PAROU')
    mais = int(input('Quantos termos a mais? '))
print('PA ACABADA COM {} TERMOS! '.format(total))
