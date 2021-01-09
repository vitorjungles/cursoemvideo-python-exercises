li = []
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > max(li):
        li.insert(4, n)
        print('Adicionado ao final da lista.')
    elif n < min(li):
        li.insert(0, n)
        print('Adicionado na posição 0 da lista.')
    elif li[1] > n > min(li) and n < max(li):
        li.insert(1, n)
        print('Adicionado na posição 1 da lista.')
    else:
        li.insert(2, n)
print('-='*30)
print(f'Os valores digitados em ordem foram {li}.')
