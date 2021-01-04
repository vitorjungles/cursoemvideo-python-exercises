print('=' * 21)
print('Calculadora de preços')
print('=' * 21)
valor = float(input('Qual é o valor da compra? R$'))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
pagamento = int(input('Sua opção: '))
avista = valor - (valor / 100 * 10)
avistacartao = valor - (valor / 100 * 5)
duasvezes = valor / 2
if pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    tresvezes = valor + (valor / 100 * 20)
    print(f'Sua compra será parcelada em {parcelas}x de R${tresvezes / parcelas:.2f} COM JUROS.')
    print(f'Sua compra de R${valor:.2f} vai custar R${tresvezes:.2f} no total.')
elif pagamento == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${avista:.2f} no total.')
elif pagamento == 2:
    print(f'Sua compra de R${valor:.2f} vai custar R${avistacartao:.2f} no total.')
elif pagamento == 3:
    print(f'Sua compra será parcelada em 2x de R${duasvezes:.2f} SEM JUROS.')
    print(f'Sua compra vai custar R${valor:.2f} no total.')
else:
    total = 0
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
