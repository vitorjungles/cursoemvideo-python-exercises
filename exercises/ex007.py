n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
med = (n1+n2)/2
print(f'A média entre a nota {n1} e a nota {n2} é {med:.1f}.')
if med >= 6:
    print('Você está aprovado!')
else:
    print('Você está reprovado!')
