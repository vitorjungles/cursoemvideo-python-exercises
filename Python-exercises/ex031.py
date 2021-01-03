d = float(input('Qual é a distância da sua viagem? '))
print(f'A distância da sua viagem será de {d}Km. Portanto:')
if d <= 200:
    print('O valor da sua passagem será de R${:.2f}.'.format(d * 0.50))
else:
    print('O valor da sua passagem será de R${:.2f}.'.format(d * 0.45))
