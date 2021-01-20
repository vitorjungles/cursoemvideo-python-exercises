def aumentar(n, p, form=True):
    if form:
        return moeda(n+((n/100)*p))
    else:
        return n+((n/100)*p)


def diminuir(n, p, form=True):
    if form:
        return moeda(n-((n/100)*p))
    else:
        return n-((n/100)*p)


def dobro(n, form=True):
    if form:
        return moeda(n*2)
    else:
        return n*2


def metade(n, form=True):
    if form:
        return moeda(n/2)
    else:
        return n/2


def moeda(v):
    return f'R${v:.2f}'


def t(s):
    return s.replace(".", ",")


def resumo(n, a=0, r=0):
    if ',' in n:
        n = n.replace(',', '.')
    n = float(n)
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}{t(str(moeda(n)))}')
    print(f'{"Dobro do preço:":<20}{t(str(dobro(n, True)))}')
    print(f'{"Metade do preço:":<20}{t(str(metade(n, True)))}')
    print(f'{"35% de aumento:":<20}{t(str(aumentar(n, a, True)))}')
    print(f'{"22% de redução:":<20}{t(str(diminuir(n, r, True)))}')
    print('-'*30)
