larg = float(input('Digite a largura de uma parede qualquer (em metros): '))
alt = float(input('Digite a altura de uma parede qualquer (em metros): '))
área = larg * alt
print('A sua parede tem a dimensão de {}x{} e sua área é de: {}m². '.format(larg, alt, área))
tinta = área / 2
print('A quantidade de tinta necessária para pintar essa parede é de: {}L de tinta. '.format(tinta))
