li = [str(input('Digite a expressão: '))]
lif = li[0].strip()
posia = []
posif = []
v = False
for pos, c in enumerate(lif):
    if lif[pos] == '(':
        posia.append(pos)
    if lif[pos] == ')':
        posif.append(pos)
if len(posia) == len(posif):
    pos = 0
    for c in range(len(posia)):
        if posia[c] < posif[c]:
            v = True
        else:
            v = False
print('Sua expressão está errada.' if v != True else 'Sua expressão está válida.')
