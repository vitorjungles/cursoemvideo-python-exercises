print('='*30)
print('Conversor de números inteiros')
print('='*30)
num = int(input('Número inteiro a ser convertido: '))
print('Escolha a base que deseja converter, sendo:\n[ 1 ] para BINÁRIO\n[ 2 ] para OCTAL\n[ 3 ] para HEXADECIMAL')
bases = int(input('Opção escolhida: '))
if bases == 1:
    print(f'O número {num} em BINÁRIO é: {bin(num)[2:]}.')
elif bases == 2:
    print(f'O número {num} em OCTAL é: {oct(num)[2:]}.')
elif bases == 3:
    print(f'O número {num} em HEXADECIMAL é: {hex(num)[2:]}.')
else:
    print('Caractere desconhecido. Tente novamente.')
