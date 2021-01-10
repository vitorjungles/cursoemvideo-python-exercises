cont = soma = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro [999 para parar]: '))
if cont == 1:
    print(f'Foi digitado {cont} número inteiro e sua soma foi {soma}.')
else:
    print(f'Foram digitados {cont} números inteiros e a soma entre eles foi {soma}.')
