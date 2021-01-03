vel = int(input('Digite a velocidade atual de um carro: '))
if vel > 80:
    print(f'A velocidade está acima do limite permitido que é de 80Km/h.\nInfelizmente você foi multado em uma taxa de R${(vel - 80)*7:.2f}.')
else:
    print('A velocidade está dentro do limite permitido.')
