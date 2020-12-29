salário = float(input('Qual é o salário do Funcionário? R$'))
newvalor = salário + (salário / 100 * 15)
print('O salário dele teve um aumento de 15%, ou seja, de R${:.2f} ele passará a ser R${:.2f}. '.format(salário, newvalor))
