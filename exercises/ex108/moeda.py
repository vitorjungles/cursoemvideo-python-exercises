def aumentar(n=0, p=0):
    return n+(n/100*p)


def diminuir(n=0, p=0):
    return n-(n/100*p)


def dobro(n=0):
    return n*2


def metade(n=0):
    return n/2


def moeda(v=0.00, si='R$'):
    return f'{si}{v:.2f}'.replace(".", ",")
