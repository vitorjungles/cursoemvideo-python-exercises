print('='*20)
print('Calculador de médias')
print('='*20)
n1 = float(input('Digite a 1ª nota do aluno: '))
n2 = float(input('Digite a 2ª nota do aluno: '))
med = (n1+n2)/2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {med:.1f}.')
if med < 5.0:
    print('Aluno REPROVADO.')
elif 5 <= med < 7:
    print('Aluno convocado para RECUPERAÇÃO.')
elif med >= 7.0:
    print('Aluno APROVADO.')
