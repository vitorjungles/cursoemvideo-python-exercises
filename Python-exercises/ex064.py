cont = soma = 0
n = int(input('Digite um número inteiro [999 para finalizar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro [999 para finalizar]: '))
if cont == 1:
    print('Foi digitado {} número inteiro e sua soma foi {}.'.format(cont, soma))
else:
    print('Foram digitados {} números inteiros e a soma entre eles foi {}.'.format(cont, soma))
