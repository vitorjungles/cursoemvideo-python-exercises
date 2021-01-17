from time import sleep


def contador(i, f, p):
    print('-='*20)
    if i > f:
        if p == 0:
            p = -1
        if p < 0:
            f -= 1
        else:
            f -= 1
            p = p-p-p
    else:
        if p == 0:
            p = 1
        if p < 0:
            p *= -1
        f += 1
    print(f'Contagem de {i} até {f-1 if i < f and f > i else f*+1+1} de {p*-1 if p < 0 else p} em {p*-1 if p < 0 else p}:')
    sleep(1)
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
