from datetime import date
from time import sleep
ano = int(input('Que ano quer analisar? Coloque 0 para anlisar o ano em que você se encontra atualmente: '))
print('ANALISANDO...')
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Você está no ano de {} e esse ano é BISSEXTO.'.format(ano))
else:
    print('Você está no ano de {} e esse ano NÃO é BISSEXTO.'.format(ano))
