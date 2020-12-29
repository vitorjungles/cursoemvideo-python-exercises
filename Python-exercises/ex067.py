while True:
    n = int(input('Digite um número para ver sua Tabuada (número negativo para parar): '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(n, 'x', c, '=', (n * c))
    print('-'*30)
print('PROGRAMA ENCERRADO! VOLTE SEMPRE!')
