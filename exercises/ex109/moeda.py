def aumentar(n, p=0, form=True):
    if form:
        return moeda(n+((n/100)*p))
    else:
        return n+((n/100)*p)


def diminuir(n, p=0, form=True):
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
    return f'R${v}'
