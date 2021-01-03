salário = float(input('Qual é o salário do Funcionário? R$'))
newvalor = salário + (salário / 100 * 15)
print(f'O salário dele teve um aumento de 15%, ou seja, de R${salário:.2f} ele passará a ser R${newvalor:.2f}.')
