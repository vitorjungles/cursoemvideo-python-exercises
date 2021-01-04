from time import sleep
print('-='*32)
print('Vamos analisar um triângulo? Digite o comprimento de três retas:')
print('-='*32)
r1 = float(input('1ª reta: '))
r2 = float(input('2ª reta: '))
r3 = float(input('3ª reta: '))
print('ANALISANDO...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR um triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo!')
