from random import randint
from time import sleep
print('-=-'*20)
print('Vou escolher um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
num1 = int(input('Que número escolhi? '))
print('PROCESSANDO...')
sleep(3)
num2 = randint(0, 5)
if num1 == num2:
    print('Parabéns, você venceu! O número {} foi o que escolhi!.'.format(num2))
else:
    print('Infelizmente você perdeu. O número que escolhi foi {} e não {}'.format(num2, num1))
