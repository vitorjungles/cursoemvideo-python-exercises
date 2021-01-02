from random import randint
from time import sleep
palpite = 0
print('-=-'*18)
print('Vou escolher um número entre 0 e 10. Tente adivinhar...')
print('-=-'*18)
print('Obs: EU SÓ VOU PARAR QUANDO VOCÊ ACERTAR! ')
acertou = False
num1 = 20
num2 = randint(0, 10)
while not acertou:
    num1 = int(input('Que número escolhi? '))
    print('PROCESSANDO...')
    sleep(1)
    palpite += 1
    if num1 == num2:
        acertou = True
    else:
        if num1 < num2:
            print('Mais... Tente mais uma vez. ')
        elif num1 > num2:
            print('Menos... Tente mais uma vez. ')
print('PARABÉNS, VOCÊ ACERTOU! VOU PARAR AQUI! ')
if palpite != 1:
    print('Para ocorrer o acerto, foram necessárias {} tentativas! '.format(palpite))
else:
    print('Para ocorrer o acerto, foi necessário {} tentativa! '.format(palpite))
