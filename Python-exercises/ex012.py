preço = float(input('Qual é o preço do produto o qual você quer levar? R$'))
desconto = preço / 100 * 5
newvalor = preço - desconto
print('O produto está em liquidação, ou seja, ao invés de custar R${:.2f}, com 5% de deconto seu novo valor será R${:.2f}. '.format(preço, newvalor))
print('Com um desconto no valor de R${:.2f}. '.format(desconto))
