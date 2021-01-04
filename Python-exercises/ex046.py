from time import sleep
print('=' * 48)
print('Contagem regressiva para o Estourador de Rojões')
print('=' * 48)
print('Quer estourar os Fogos de Artifício?')
resp = str(input('Responda Sim ou Não: ')).upper()
if resp == 'SIM':
    for cont in range(10, -1, -1):
        sleep(1)
        print(cont, '!')
    print('KABUM!!!')
else:
    print('Que pena...')
