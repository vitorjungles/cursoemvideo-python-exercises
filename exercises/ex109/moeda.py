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
