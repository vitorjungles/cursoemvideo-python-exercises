def colors(txt='None', cor='default'):
    cores = {'verde': '\033[0;32m', 'amarelo': '\033[0;33m', 'azul': '\033[0;34m', 'default': '\033[0m', 'vermelho': '\033[0;31m'}
    return f'{cores[cor]}{txt}\033[m'


def title(txt='None'):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)


def options(lst):
    for c in range(0, len(lst)):
        print(f'{colors(f"{c+1}", "amarelo")} - {colors(lst[c], "azul")}')
    print('-'*42)


def interface():
    title('MENU PRINCIPAL')
    options(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    while True:
        try:
            op = int(input(colors('Sua Opção: ', 'verde')))
        except (ValueError, TypeError):
            print(colors('ERRO: por favor, digite um número inteiro válido.', 'vermelho'))
        except KeyboardInterrupt:
            print(colors('\nUsuário preferiu não digitar esse número.', 'vermelho'))
            return 0
        else:
            return op
