from time import sleep
print('-=' * 32)
print('Vamos analisar um triângulo? Digite o comprimento de três retas: ')
print('-=' * 32)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
print('ANALISANDO...')
sleep(3)
# Se o primeiro if for verdadeiro ele reproduzirá os outros ifs, se for falso, ele não reproduzirá chegando ao fim
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO, pois todos os lados são iguais.')
    if r1 != r2 != r3 != r1:
        print('ESCALENO, pois nenhum dos lados são iguais.')
    else:
        print('ISÓSCELES, pois dois lados são iguais.')
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo!')
