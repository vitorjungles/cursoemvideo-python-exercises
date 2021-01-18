def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('-'*30)
n = str(input('Nome do Jogador: ')).strip().capitalize()
g = str(input('Número de Gols: '))
if n == g == '':
    print(ficha())
elif n == '' and g.isnumeric():
    g = int(g)
    print(ficha(gols=g))
elif (n != '' and g == '') or (n != '' and not g.isnumeric()):
    print(ficha(nome=n))
else:
    g = int(g)
    print(ficha(n, g))
