idadehomemvelho = 0
mulheres = 0
somaidade = 0
nomehomemvelho = ''
print('=' * 60)
print('Análise do nome, da idade e do sexo de um grupo de 4 pessoas')
print('=' * 60)
print('Nessa análise irei mostrar:\nA Média de IDADE do grupo, qual é o NOME do HOMEM mais VELHO e quantas MULHERES têm MENOS de 20 anos. ')
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if c == 1 and sexo == 'M':
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo == 'M' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
print('A MÉDIA de IDADE do grupo é de {} anos.'.format(somaidade / 4))
print('O HOMEM mais VELHO tem {} anos e seu NOME é {}.'.format(idadehomemvelho, nomehomemvelho))
print('Das 4 pessoas analisadas, há {} MULHERES com MENOS de 20 anos.'.format(mulheres))
