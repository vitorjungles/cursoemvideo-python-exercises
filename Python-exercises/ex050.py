s = cont = 0
print('=' * 29)
print('Somando seis números inteiros')
print('=' * 29)
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número inteiro: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Você digitou {cont} valores PARES e a soma foi {s}.')
