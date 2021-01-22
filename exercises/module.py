from time import sleep


def colors(txt='None', cor='default'):
    cores = {'amarelo': '\033[0;33m', 'azul': '\033[0;34m', 'default': '\033[0m', 'vermelho': '\033[0;31m'}
    return f'{cores[cor]}{txt}\033[m'


def title(txt='None'):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)


def options():
    print(f'{colors("1", "amarelo")} - {colors("Ver pessoas cadastradas", "azul")}')
    print(f'{colors("2", "amarelo")} - {colors("Cadastrar nova Pessoa", "azul")}')
    print(f'{colors("3", "amarelo")} - {colors("Sair do Sistema", "azul")}')
    print('-' * 42)


def menu():
    while ValueError:
        try:
            title('MENU PRINCIPAL')
            options()
            op = int(input(colors('Sua opção: ', 'amarelo')))
        except ValueError:
            print(colors('ERRO! Digite uma opção válida!', 'vermelho'))
            sleep(2)
        else:
            return op


def write():
    title('NOVO CADASTRO')
    p = {'nome': str(input('Nome: ')).strip()}
    while ValueError:
        try:
            p['idade'] = int(input('Idade: '))
        except ValueError:
            print(colors('ERRO: por favor, digite um número inteiro válido.', 'vermelho'))
        else:
            with open("register.txt", "a") as i:
                with open("register.txt", "r") as f:
                    txt = f.read()
                    i.write(f'{p["nome"]:<31}{p["idade"]} anos' if len(txt) == 0 else f'\n{p["nome"]:<31}{p["idade"]} anos')
            print(f'Novo registro de {p["nome"]} adicionado.')
            break


def read():
    title('PESSOAS CADASTRADAS')
    with open("register.txt", "r") as f:
        print(f.read())
