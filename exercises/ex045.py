from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print(f'{" GAME DO PEDRA, PAPEL E TESOURA ":=^50}')
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
opcao = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
pc = randint(0, 2)
print('-='*11)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[opcao]}')
print('-='*11)
if pc == 0:
    if opcao == 0:
        print('EMPATOU!')
    elif opcao == 1:
        print('JOGADOR GANHOU!')
    elif opcao == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('OPÇÃO INVÁLIDA. JOGUE NOVAMENTE!')
elif pc == 1:
    if opcao == 0:
        print('COMPUTADOR GANHOU!')
    elif opcao == 1:
        print('EMPATOU!')
    elif opcao == 2:
        print('JOGADOR GANHOU!')
    else:
        print('OPÇÃO INVÁLIDA. JOGUE NOVAMENTE!')
elif pc == 2:
    if opcao == 0:
        print('JOGADOR GANHOU!')
    elif opcao == 1:
        print('COMPUTADOR GANHOU!')
    elif opcao == 2:
        print('EMPATOU!')
    else:
        print('OPÇÃO INVÁLIDA. JOGUE NOVAMENTE!')
