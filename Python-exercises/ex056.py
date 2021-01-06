idadehomemvelho = mulheres = somaidade = 0
nomehomemvelho = ''
print('='*60)
print('Análise do nome, da idade e do sexo de um grupo de 4 pessoas')
print('='*60)
print('Nessa análise irei mostrar:\nA Média de IDADE do grupo, qual é o NOME do HOMEM mais VELHO e quantas MULHERES têm MENOS de 20 anos.')
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
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
print(f'A MÉDIA de IDADE do grupo é de {somaidade/4} anos.')
print(f'O HOMEM mais VELHO tem {idadehomemvelho} anos e seu NOME é {nomehomemvelho}.')
print(f'Das 4 pessoas analisadas, há {mulheres} MULHERES com MENOS de 20 anos.')
