def write():
    try:
        p = {'nome': str(input('Nome: ')).strip()}
    except KeyboardInterrupt:
        print('\n\033[0;31mUsuário preferiu não digitar esse nome.\033[m')
        p = {'nome': '<desconhecido>'}
    if p['nome'] == '':
        p = {'nome': '<desconhecido>'}
    while True:
        try:
            p['idade'] = int(input('Idade: '))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            p['idade'] = 0
            break
        else:
            break
    with open("register.txt", "at") as i:
        with open("register.txt", "rt") as f:
            txt = f.read()
            i.write(f'{p["nome"]:<31}{p["idade"]} anos' if len(txt) == 0 else f'\n{p["nome"]:<31}{p["idade"]} anos')
        print(f'Novo registro de {p["nome"]} adicionado.')


def createandread():
    try:
        p = open("register.txt", "rt")
        p.close()
    except FileNotFoundError:
        p = open("register.txt", "wt+")
        p.close()
    else:
        with open("register.txt", "rt") as f:
            t = f.read()
        return t


def read():
    print(createandread())
