from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print(f'{" GAME DO PEDRA, PAPEL E TESOURA ":=^50}')
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
opcao = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
pc = randint(0, 2)
print('-=' * 11)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[opcao]))
print('-=' * 11)
if pc == 0:
    if opcao == 0:
        print('EMPATOU! ')
    elif opcao == 1:
        print('JOGADOR GANHOU! ')
    elif opcao == 2:
        print('COMPUTADOR GANHOU! ')
    else:
        print('OPÇÃO INVÁLIDA. JOGUE NOVAMENTE! ')
elif pc == 1:
    if opcao == 0:
        print('COMPUTADOR GANHOU! ')
    elif opcao == 1:
        print('EMPATOU! ')
    elif opcao == 2:
        print('JOGADOR GANHOU! ')
    else:
        print('OPÇÃO INVÁLIDA. JOGUE NOVAMENTE! ')
elif pc == 2:
    if opcao == 0:
        print('JOGADOR GANHOU! ')
    elif opcao == 1:
        print('COMPUTADOR GANHOU! ')
    elif opcao == 2:
        print('EMPATOU! ')
    else:
        print('OPÇÃO INVÁLIDA. JOGUE NOVAMENTE! ')
