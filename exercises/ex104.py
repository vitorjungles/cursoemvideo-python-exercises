def leiaint(txt):
    print('-'*30)
    a = str(input(txt))
    while not a.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        a = str(input(txt))
    a = int(a)
    return a


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
