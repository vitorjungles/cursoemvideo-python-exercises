t = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {t}.')
print(f'O valor 9 apareceu {t.count(9)} vezes.')
print(f'O valor 3 apareceu na {t.index(3)+1}ª posição.' if 3 in t else 'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for c in range(0, 4):
    if t[c] % 2 == 0:
        print(t[c], end=' ')
