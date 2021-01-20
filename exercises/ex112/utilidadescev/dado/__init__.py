def leiadinheiro(txt):
    v = input(txt).strip()
    while not v.replace(',', '').replace('.', '').isnumeric():
        print(f'\033[0;31mERRO: "{v}" é um preço inválido!\033[m')
        v = input(txt).strip()
    return v
