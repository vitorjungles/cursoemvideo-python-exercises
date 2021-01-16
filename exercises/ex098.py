from time import sleep


def contador(i, f, p):
    print('-='*20)
    if p > 0:
        print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        print(f'Contagem de {i} até {f} de {p-p-p} em {p-p-p}:')
    if p == 0:
        print(f'Contagem de {i} até {f} de 1 em 1:')
    sleep(1)
    if p == 0:
        for c in range(i, f-1, -1):
            sleep(0.30)
            print(c, end=' ')
    elif i > f and p < 0:
        for c in range(i, f-1, p):
            sleep(0.30)
            print(c, end=' ')
    else:
        if i < f:
            for c in range(i, f+1, p):
                sleep(0.30)
                print(c, end=' ')
        if i > f:
            for c in range(i, f-1, -p):
                sleep(0.30)
                print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
