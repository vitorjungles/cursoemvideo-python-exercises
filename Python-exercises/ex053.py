print('=' * 23)
print('DETECTOR DE PALÍNDROMOS')
print('=' * 23)
print('PALÍNDROMOS SÃO FRASES QUE PODEM SER LIDAS DE TRÁS PARA FRENTE SEM ALTERAÇÃO ALGUMA. ')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}. '.format(junto, inverso))
if inverso == junto:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
