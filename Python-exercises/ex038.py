print('='*30)
print('Comparador de números inteiros')
print('='*30)
num1 = int(input('1° número: '))
num2 = int(input('2° número: '))
if num1 > num2:
    print('O 1° número é maior.')
elif num2 > num1:
    print('O 2° número é maior.')
elif num1 == num2:
    print('Os dois números são IGUAIS.')
else:
    print('Valor(es) inválido(s). Tente novamente.')
