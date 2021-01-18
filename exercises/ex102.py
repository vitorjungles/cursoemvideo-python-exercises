def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-'*30)
    f = cont = n
    for c in range(1, n):
        f *= c
        if show:
            print(f'{cont} x ' if not c == n-1 else f'{cont} x 1 = ', end='')
        cont -= 1
    return f


print(fatorial(5))
