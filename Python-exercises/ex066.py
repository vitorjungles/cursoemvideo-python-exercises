c = s = n = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n != 999:
        c += 1
        s += n
    else:
        break
print(f'Foram digitados {c} números e a soma entre eles é {s}.')
