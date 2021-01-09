li = [str(input('Digite a expressão: '))]
lif = li[0].strip()
posia = []
posif = []
v = bool
for pos, c in enumerate(lif):
    if lif[pos] == '(':
        posia.append(pos)
    if lif[pos] == ')':
        posif.append(pos)
if len(posia) != len(posif):
    print('Sua expressão está errada.')
    v = False
else:
    pos = 0
    for c in range(len(posia)):
        if posia[pos] < posif[pos]:
            v = True
        else:
            v = False
print(posia, posif)
if v == True:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')