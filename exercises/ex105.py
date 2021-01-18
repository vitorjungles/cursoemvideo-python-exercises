def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-'*30)
    maior = menor = m = 0.0
    for c in range(0, len(n)):
        m += n[c]
        if c == 0 or n[c] > maior:
            maior = n[c]
        if c == 0 or n[c] < menor:
            menor = n[c]
    m /= len(n)
    d = {'total': len(n), 'maior': maior, 'menor': menor, 'média': m}
    if sit:
        if m >= 7:
            d['situação'] = 'BOA'
        elif m >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
