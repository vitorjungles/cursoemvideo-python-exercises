from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    ma = 0
    for c in range(0, len(num)):
        print(num[c], end=' ')
        if c == 0 or num[c] > ma:
            ma = num[c]
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {ma}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
