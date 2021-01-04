from datetime import date
sexo = str(input('Qual é o seu sexo? '))
sex = sexo.upper()
nasc = int(input('Qual foi o ano em que nasceu? '))
datapc = date.today().year
tempoapos = datapc - nasc
temporestante = tempoapos - 18
if tempoapos < 18 and sex == 'MASCULINO':
    print(f'Quem nasceu em {nasc} tem {tempoapos} anos em {datapc}.')
    print('Você ainda se alistará ao serviço militar.')
    print(f'RESTAM {18 - tempoapos} ANOS PARA O ALISTAMENTO!')
    print(f'Seu alistamento será em {datapc + 18 - tempoapos}.')
elif tempoapos > 18 and sex == 'MASCULINO':
    print(f'Quem nasceu em {nasc} tem {tempoapos} anos em {datapc}.')
    print('Já passou o ano de alistamento militar, portanto, você não se alistará.')
    print(f'JÁ SE PASSARAM {temporestante} ANOS DESDE O ALISTAMENTO.')
    print(f'Seu alistamento foi em {datapc + 18 - tempoapos}.')
elif tempoapos == 18 and sex == 'MASCULINO':
    print(f'Quem nasceu em {nasc} tem {tempoapos} anos em {datapc}.')
    print('ALISTE-SE JÁ AO SERVIÇO MILITAR!')
    print('VOCÊ ESTÁ NO ANO DE ALISTAMENTO!')
else:
    print('O alistamento militar é somente para pessoas do sexo masculino.')
