print('-=' * 30)
print('CALCULADORA DE MÉDIAS E DO MAIOR E DO MENOR VALOR DIGITADOS')
print('-=' * 30)
opcao = ''
soma = cont = maior = menor = 0
while opcao in 'Ss':
    n = int(input('Digite um número inteiro: '))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
media = soma / cont
if cont == 1:
    print('{} número foi digitado e sua média foi {}.'.format(cont, media))
else:
    print('{} números foram digitados e a média entre eles foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
print('Você escolheu sair do programa, volte sempre! ')
