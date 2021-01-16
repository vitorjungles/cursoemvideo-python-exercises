def escreva(txt):
    tam = len(txt)+4
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)


msg = str(input('Qual mensagem? ')).strip()
escreva(msg)
