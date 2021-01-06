from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
opcao = 0
while opcao != 5:
    print('-='*20)
    print(f'Com os valores {num1} e {num2} você pretende:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    print('-='*20)
    opcao = int(input('>>>>> Sua opção: '))
    if opcao == 1:
        print(f'A SOMA entre os valores {num1} e {num2} é {num1+num2}.')
    elif opcao == 2:
        print(f'A MULTIPLICAÇÃO entre os valores {num1} e {num2} é {num1*num2}.')
    elif opcao == 3:
        if num1 > num2:
            print(f'O MAIOR número entre os valores {num1} e {num2} é {num1}.')
        if num2 > num1:
            print(f'O MAIOR número entre os valores {num1} e {num2} é {num2}.')
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro: '))
    elif opcao > 5 or opcao == 0:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
    sleep(2)
print('Saindo...')
print('-='*20)
sleep(2)
print('Você escolheu sair do programa.')
print('Até a próxima!')
