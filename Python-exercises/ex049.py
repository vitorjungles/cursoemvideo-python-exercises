num = int(input('Digite um número para visualizar sua Tabuada: '))
ig = '=' * 12
print('A Tabuada do número {} é:'.format(num))
print(ig)
for c in range(0, 11):
    print('{} x  {} = {} '.format(num, c, num*c))
print(ig)
print('Acabou')
