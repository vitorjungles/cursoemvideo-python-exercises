listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30}R$', end='')
    for i in range(c+1, c+2):
        print(f'{listagem[i]:7.2f}')
print('-'*40)