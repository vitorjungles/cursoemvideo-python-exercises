from datetime import date
print('=' * 25)
print('Verificador de maioridade')
print('=' * 25)
print('Irei verificar a idade de 7 pessoas e indicar se são maiores de idade ou não.')
contmen = contmai = 0
anopc = date.today().year
for c in range(1, 8):
    ano = int(input('Insira a data de nascimento da {}ª pessoa: '.format(c)))
    idade = anopc - ano
    if idade < 21:
        contmen += 1
    elif idade >= 21:
        contmai += 1
print(f'Desse grupo de pessoas {contmai} são maiores de idade, pois já atingiram 21 anos.')
print(f'E também há {contmen} pessoas menores de idade, pois ainda não atingiram 21 anos.')
