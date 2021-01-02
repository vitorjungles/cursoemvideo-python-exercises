from datetime import date
print('=' * 35)
print('Classificador de atletas de natação')
print('=' * 35)
nasc = int(input('Digite o ano de nascimento do atleta: '))
datapc = date.today().year
anos = datapc - nasc
print(f'O atleta tem {anos} anos.')
if anos <= 9:
    print('Sua classificação é MIRIM.')
elif anos <= 14:
    print('Sua classificação é INFANTIL.')
elif anos <= 19:
    print('Sua classificação é JUNIOR.')
elif anos <= 25:
    print('Sua classificação é SÊNIOR.')
elif anos > 25:
    print('Sua classificação é MASTER.')
