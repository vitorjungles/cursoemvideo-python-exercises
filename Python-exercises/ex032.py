from datetime import date
from time import sleep
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano em que você se encontra atualmente: '))
print('ANALISANDO...')
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Você está no ano de {ano} e esse ano é BISSEXTO.')
else:
    print(f'Você está no ano de {ano} e esse ano NÃO é BISSEXTO.')
