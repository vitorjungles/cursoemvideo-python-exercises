from time import sleep
print('-=-'*12)
print('ANALISADOR DE AUMENTOS')
print('-=-'*12)
sal = float(input('Qual é o salário do funcionário? R$'))
print('ANALISANDO...')
sleep(3)
if sal > 1250:
    print(f'O salário que era R${sal:.2f} teve 10% de aumento e passou a ser R${sal + (sal / 100 * 10):.2f}.')
else:
    print(f'O salário que era R${sal:.2f} teve 15% de aumento e passou a ser R${sal + (sal / 100 * 15):.2f}.')
