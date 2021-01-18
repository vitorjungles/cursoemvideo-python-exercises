from time import sleep


def t(msg, c='\033[m'):
    print(f'{c}~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))
    print('\033[0;30;107m', end='')
    sleep(1)


while True:
    t('SISTEMA DE AJUDA PyHELP', '\033[0;97;42m')
    co = str(input('\033[mFunção ou Biblioteca > ')).strip().upper()
    if co == 'FIM':
        t('ATÉ LOGO!', '\033[0;97;41m')
        break
    else:
        t(f"Acessando o manual do comando '{co.lower()}'", '\033[0;97;44m')
        help(co.lower())
        sleep(2)
