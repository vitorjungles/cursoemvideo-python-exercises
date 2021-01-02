from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
opcao = 0
while opcao != 5:
    print('-=' * 20)
    print("""Com os valores {} e {} você pretende: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""".format(num1, num2))
    print('-=' * 20)
    opcao = int(input('>>>>> Sua opção: '))
    if opcao == 1:
        print('A SOMA entre os valores {} e {} é {}. '.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A MULTIPLICAÇÃO entre os valores {} e {} é {}. '.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O MAIOR número entre os valores {} e {} é {}. '.format(num1, num2, num1))
        if num2 > num1:
            print('O MAIOR número entre os valores {} e {} é {}. '.format(num1, num2, num2))
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro: '))
    elif opcao > 5 or opcao == 0:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE! ')
    sleep(2)
print('Saindo...')
print('-=' * 20)
sleep(2)
print('Você escolheu sair do programa.')
print('Até a próxima! ')
