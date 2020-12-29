maior = 0
menor = 0
print('=' * 22)
print('Leitor de peso (em Kg)')
print('=' * 22)
print('Irei ler o peso de 5 pessoas e verificar qual é o maior e o menor peso. ')
for c in range(1, 6):
    peso = float(input('Insira o peso da {}ª pessoa (em Kg): '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg.'.format(maior))
print('O menor peso foi {}Kg.'.format(menor))
