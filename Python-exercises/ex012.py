preço = float(input('Qual é o preço do produto o qual você quer levar? R$'))
desconto = preço / 100 * 5
newvalor = preço - desconto
print(f'O produto está em liquidação, ou seja, ao invés de custar R${preço:.2f}, com 5% de deconto seu novo valor será R${newvalor:.2f}.')
print(f'Com um desconto no valor de R${desconto:.2f}.')
