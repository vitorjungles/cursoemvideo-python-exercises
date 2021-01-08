t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
op = ' '
while op != 'N':
    n = int(input('Digite um numero entre 0 e 20: '))
    while not (0 <= n <= 20):
        n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Você digitou o número {t[n]}.')
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
