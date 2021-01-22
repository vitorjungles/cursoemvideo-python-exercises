from pack import menu, file
from time import sleep
while True:
    c = file.createandread()
    r = menu.interface()
    if r == 3:
        menu.title('Saindo do sistema... Até logo!')
        break
    elif r == 2:
        menu.title('NOVO CADASTRO')
        file.write()
    elif r == 1:
        menu.title('PESSOAS CADASTRADAS')
        file.read()
    else:
        print(menu.colors('ERRO! Digite uma opção válida!', 'vermelho'))
    sleep(2)
