print('=='*15)
print(f'{"BANCO CEV":^30}')
print('=='*15)
valor = float(input('Que valor você quer sacar? R$'))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    if valor >= 50:
        ced50 += 1
        valor -= 50
        if valor < 50:
            print(f'Total de {ced50} cédulas de R$50.')
    elif valor >= 20:
        ced20 += 1
        valor -= 20
        if valor < 20:
            print(f'Total de {ced20} cédulas de R$20.')
    elif valor >= 10:
        ced10 += 1
        valor -= 10
        if valor < 10:
            print(f'Total de {ced10} cédulas de R$10.')
    elif valor >= 1:
        ced1 += 1
        valor -= 1
        if valor < 1:
            print(f'Total de {ced1} cédulas de R$1.')
    else:
        break
print('=='*15)
print('Volte sempre ao BANCO CEV! Tenha um ótimo dia!')
