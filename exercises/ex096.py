def area(larg, co):
    ar = larg*co
    print(f'A área de um terreno {la}x{c} é de {ar}m².')


print('Controle de Terrenos')
print('-'*20)
la = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(la, c)
