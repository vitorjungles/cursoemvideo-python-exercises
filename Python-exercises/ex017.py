from math import hypot
catop = float(input('Qual é o comprimento do cateto oposto de um triângulo retângulo? '))
catadj = float(input('E do cateto adjacente? '))
hip = hypot(catop, catadj)
print(f'A hipotenusa dos catetos {catop} e {catadj} é {hip:.2f}.')
