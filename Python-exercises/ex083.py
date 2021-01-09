li = [str(input('Digite a expressão: '))]
if li[0].count('(') == li[0].count(')'):
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
