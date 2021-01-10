print('='*32)
print('TERMOS DA SEQUÊNCIA DE FIBONACCI')
print('='*32)
n = int(input('Quantos Termos quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print('~'*40)
print(f'{t1} → {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → ACABOU')
print('~'*40)
