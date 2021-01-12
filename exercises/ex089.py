li = [[]]
co = cont = 1
while True:
    li.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    li[0].append(n1)
    n2 = float(input('Nota 2: '))
    li[0].append(n2)
    m = (n1+n2)/2
    li.append(m)
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'N°{"NOME":>5}{"MÉDIA":>15}')
print('-'*26)
for c in li:
    if type(c) == str:
        print(f'{cont-1:<3}{c:<15}{li[co]:>4.1f}')
        cont += 1
    co += 1
while True:
    print('-'*35)
    al = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if al == 999:
        break
    print(f'Notas de {li[(2*al)+1]} são {li[0][al+al]} e {li[0][(al+al)+1]}.')
print('FINALIZANDO...', f'\n{"<"*3} VOLTE SEMPRE {">"*3}')
