print('=' * 20)
print('Calculador de médias')
print('=' * 20)
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
med = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, med))
if med < 5.0:
    print('Aluno REPROVADO.')
elif 5 <= med < 7:
    print('Aluno convocado para RECUPERAÇÃO.')
elif med >= 7.0:
    print('Aluno APROVADO.')
