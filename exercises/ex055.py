maior = menor = 0
print('='*22)
print('Leitor de peso (em Kg)')
print('='*22)
print('Irei ler o peso de 5 pessoas e verificar qual é o maior e o menor peso.')
for c in range(1, 6):
    peso = float(input(f'Insira o peso da {c}ª pessoa (em Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg.')
print(f'O menor peso foi {menor}Kg.')
