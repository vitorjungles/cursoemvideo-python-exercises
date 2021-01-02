from random import randint
from time import sleep
print('-=-'*20)
print('Vou escolher um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num1 = int(input('Que número escolhi? '))
print('PROCESSANDO...')
sleep(3)
num2 = randint(0, 5)
if num1 == num2:
    print(f'Parabéns, você venceu! O número {num2} foi o que escolhi!.')
else:
    print(f'Infelizmente você perdeu. O número que escolhi foi {num2} e não {num1}.')
