from random import randint
c = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    n = int(input('Digite um número: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    PC = randint(1, 10)
    print('--'*15)
    print(f'Você jogou {n} e o computador {PC}. Total de {n + PC}', end=' ')
    print('DEU PAR' if (n + PC) % 2 == 0 else 'DEU ÍMPAR')
    print('--'*15)
    if pi == 'I' and (n + PC) % 2 == 0:
        print('Você PERDEU!')
        print('=-'*15)
        break
    elif pi == 'P' and (n + PC) % 2 != 0:
        print('Você PERDEU!')
        print('=-'*15)
        break
    else:
        c += 1
        print('Você GANHOU!')
        print('Vamos jogar outra vez...')
        print('=-'*15)
print(f'GAME OVER! VEZES VENCIDAS: {c}.')
