from math import hypot
catop = float(input('Qual é o comprimento do cateto oposto de um triângulo retângulo? '))
catadj = float(input('E do cateto adjacente? '))
hip = hypot(catop, catadj)
print('A hipotenusa dos catetos {} e {} é {:.2f}. '.format(catop, catadj, hip))
