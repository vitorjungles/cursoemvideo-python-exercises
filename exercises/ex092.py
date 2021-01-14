from datetime import date
d = {'nome': str(input('Nome: ')).strip().capitalize(), 'nasc': int(input('Ano de Nascimento: '))}
d['idade'] = date.today().year - d['nasc']
del d['nasc']
d['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if d['ctps'] != 0:
    d['contratação'] = int(input('Ano de contratação: '))
    d['salário'] = float(input('Salário: R$'))
    d['aposentadoria'] = (35 - (date.today().year - d['contratação'])) + d['idade']
print('-='*30)
for k, v in d.items():
    print(f'  - {k} tem o valor {v}.')
