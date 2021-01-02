vel = int(input('Digite a velocidade atual de um carro: '))
if vel > 80:
    print('A velocidade está acima do limite permitido que é de 80Km/h! \nInfelizmente você foi multado em uma taxa de R${:.2f}!'.format((vel - 80)*7))
else:
    print('Continue assim, a velocidade está dentro do valor permitido.')
