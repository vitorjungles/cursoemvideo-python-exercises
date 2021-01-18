def voto(nasc):
    from datetime import date
    idade = date.today().year-nasc
    if 65 >= idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


print('-'*30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
