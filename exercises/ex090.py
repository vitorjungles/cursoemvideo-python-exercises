al = {'nome': str(input('Nome: ')).strip().capitalize()}
al['média'] = float(input(f'Média de {al["nome"]}: '))
if al['média'] >= 7:
    al['situação'] = 'Aprovado'
elif 5 <= al['média'] < 7:
    al['situação'] = 'Recuperação'
else:
    al['situação'] = 'Reprovado'
print('-='*30)
for k, v in al.items():
    print(f'{"-":>3} {k} é igual a {v}.')
