texto = str('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('=' * 59)
print(f"{texto:^60}")
print('=' * 59)
num = int(input('1° Termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print(c, end=' → ')
print('ACABOU')
