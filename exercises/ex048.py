s = cont = 0
print('='*96)
print('Verificando a soma dos números que são ímpares e múltiplos de 3 entre o número 1 e o número 500.')
print('='*96)
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma de todos os {cont} valores é {s}.')