def aumentar(n=0, p=0, form=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar
    :param p: qual é a porcentagem do aumento.
    :param form: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    return moeda(n+(n/100*p)) if form else n+(n/100*p)


def diminuir(n=0, p=0, form=False):
    return moeda(n-(n/100*p)) if form else n-(n/100*p)


def dobro(n=0, form=False):
    return moeda(n*2) if form else n*2


def metade(n=0, form=False):
    return moeda(n/2) if form else n/2


def moeda(v=0.00, si='R$'):
    return f'{si}{v:.2f}'.replace('.', ',')


def resumo(n=0, a=10, r=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}{moeda(n)}')
    print(f'{"Dobro do preço:":<20}{dobro(n, True)}')
    print(f'{"Metade do preço:":<20}{metade(n, True)}')
    print(f'{a}{"% de aumento:":<{20-len(str(a))}}{aumentar(n, a, True)}')
    print(f'{r}{"% de redução:":<{20-len(str(r))}}{diminuir(n, r, True)}')
    print('-'*30)
