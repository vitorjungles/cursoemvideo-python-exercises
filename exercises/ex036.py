vc = float(input('Qual é o valor da casa a ser financiada? R$'))
sc = float(input('Qual é o salário do comprador? R$'))
qa = int(input('Em quantos anos o comprador deseja para financiar a casa? '))
vp = vc/(qa*12)
salpor = (sc/10)*3
if vp > salpor:
    print(f'Para pagar uma casa de R${vc:.2f} em {qa} anos a prestação será de R${vp:.2f}.')
    print('Empréstimo IMPOSSÍVEL!')
elif vp <= salpor:
    print(f'Para pagar uma casa de R${vc:.2f} em {qa} anos a prestação será de R${vp:.2f}.')
    print('Empréstimo POSSÍVEL!')
