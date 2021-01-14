c = m = 0
li = []
while True:
    li.append({'nome': str(input('Nome: ')).strip().capitalize()})
    li[c]['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while li[c]['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        li[c]['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    li[c]['idade'] = int(input('Idade: '))
    m += li[c]['idade']
    c += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        print('ERRO! Responda apenas com S ou N.')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(li)} pessoas cadastradas.')
m /= len(li)
print(f'B) A média de idade é de {m:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in li:
    if c['sexo'] == 'F':
        print(c['nome'], end=', ')
print('\nD) Lista das pessoas que estão acima da média: ')
for c in li:
    if c['idade'] > m:
        print('    ', end='')
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<< ENCERRADO >>')
