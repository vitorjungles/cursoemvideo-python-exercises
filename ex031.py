d = float(input('Qual é a distância da sua viagem? '))
print('A distância da sua viagem será de {}Km. Portanto: '.format(d))
if d <= 200:
    print('O valor da sua passagem será de R${:.2f}.'.format(d * 0.50))
else:
    print('O valor da sua passagem será de R${:.2f}.'.format(d * 0.45))
