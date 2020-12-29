print('=' * 21)
print('Calculadora de preços ')
print('=' * 21)
valor = float(input('Qual é o valor da compra? R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
pagamento = int(input('Sua opção: '))
avista = valor - (valor / 100 * 10)
avistacartao = valor - (valor / 100 * 5)
duasvezes = valor / 2
if pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    tresvezes = valor + (valor / 100 * 20)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, tresvezes / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(valor, tresvezes))
elif pagamento == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(valor, avista))
elif pagamento == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(valor, avistacartao))
elif pagamento == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(duasvezes))
    print('Sua compra vai custar R${:.2f} no total.'.format(valor))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
