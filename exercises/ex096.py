def area(lar, co):
    a = lar*co
    print(f'A área de um terreno {lar}x{co} é de {a}m².')


print('Controle de Terrenos')
print('-'*20)
la = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(la, c)
