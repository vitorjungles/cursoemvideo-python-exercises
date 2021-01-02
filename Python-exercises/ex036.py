vc = float(input('Qual é o valor da casa a ser financiada? R$'))
sc = float(input('Qual é o salário do comprador? R$'))
qa = int(input('Em quantos anos o comprador deseja para financiar a casa? '))
vp = vc / (qa * 12)
salpor = (sc / 10) * 3
if vp > salpor:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(vc, qa, vp))
    print('Empréstimo IMPOSSÍVEL ! ')
elif vp <= salpor:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(vc, qa, vp))
    print('Empréstimo POSSÍVEL !')
