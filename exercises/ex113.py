def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


i = leiaint('Digite um número Inteiro: ')
r = leiafloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}.')
