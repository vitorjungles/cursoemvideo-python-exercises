dezoito = h = m = 0
while True:
    print('-'*25)
    print('{:^26}'.format('CADASTRE UMA PESSOA'))
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*25)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    if op == 'N':
        break
print('=='*3, 'FIM DO PROGRAMA', '='*7)
print(f'Total de pessoas com mais de 18 anos: {dezoito}.')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {m} mulheres com menos de 20 anos.')