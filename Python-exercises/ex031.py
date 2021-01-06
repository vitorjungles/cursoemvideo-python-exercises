d = float(input('Qual é a distância da sua viagem? '))
print(f'A distância da sua viagem será de {d}Km.')
if d <= 200:
    print(f'O valor da sua passagem será de R${d*0.50:.2f}.')
else:
    print(f'O valor da sua passagem será de R${d*0.45:.2f}.')
