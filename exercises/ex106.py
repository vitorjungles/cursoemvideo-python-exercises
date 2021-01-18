from time import sleep
while True:
    print('\033[0;97;42m~'*27)
    print(f'{"SISTEMA DE AJUDA PyHELP":^27}')
    print('~'*27)
    sleep(1)
    co = str(input('\033[mFunção ou Biblioteca > ')).strip().upper()
    if co == 'FIM':
        txt = '  ATÉ LOGO'
        print('\033[0;97;41m~'*(len(txt)+2))
        print(txt)
        print(f'{"~"*(len(txt)+2)}')
        break
    else:
        txt = f"{'  Acessando o manual do comando':^30} '{co.lower()}'"
        print('\033[0;97;44m~'*(len(txt)+2))
        print(txt)
        print(f'{"~"*(len(txt)+2)}')
        sleep(1)
        print('\033[0;30;107m')
        help(co.lower())
        sleep(1)
