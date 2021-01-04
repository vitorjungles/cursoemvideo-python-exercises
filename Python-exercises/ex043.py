print('=' * 17)
print('Calculador de IMC')
print('=' * 17)
peso = float(input('Digite seu peso (em Kg): '))
altura = float(input('Digite sua altura (em m): '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}.')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está na faixa do PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA!')
