num = int(input('Digite um número para visualizar sua Tabuada: '))
ig = '=' * 12
print(f'A Tabuada do número {num} é:')
print(ig)
for c in range(0, 11):
    print(f'{num} x  {c} = {num*c}')
print(ig)
print('Acabou')
