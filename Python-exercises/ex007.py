nt1 = float(input('Nota 1: '))
nt2 = float(input('Nota 2: '))
med = (nt1+nt2)/2
print('A média entre a nota {} e a nota {} é: {:.1f}. '.format(nt1, nt2, med))
if med >= 6:
    print('Você está aprovado! :) ')
else:
    print('Você está reprovado! :( ')
