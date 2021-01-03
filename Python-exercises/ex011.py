larg = float(input('Digite a largura de uma parede qualquer (em metros): '))
alt = float(input('Digite a altura de uma parede qualquer (em metros): '))
area = larg * alt
print(f'A sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
tinta = area / 2
print(f'A quantidade de tinta necessária para pintar essa parede é de {tinta}L de tinta.')
