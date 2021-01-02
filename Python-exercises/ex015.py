dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
dial = dias * 60
kmrod = Km * 0.15
total = dial + kmrod
print('O total a pagar é de R${:.2f}. '.format(total))
