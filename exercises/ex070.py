c = tot = mil = barato = 0
barato = ''
print('-'*35)
print(f'{"LOJA SUPER BARATÃO":^35}')
print('-'*35)
while True:
    c += 1
    nome = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    tot += preco
    if preco > 1000:
        mil += 1
    if c == 1 or preco < barato:
        barato = preco
        nomebarato = nome
    if op == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^40}')
print(f'O total da compra foi R${tot:.2f}.')
print(f'Temos {mil} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}.')
