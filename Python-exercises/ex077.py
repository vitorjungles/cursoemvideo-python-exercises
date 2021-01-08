palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} temos', end=' ')
    for i in range(0, len(palavras[c])):
        if palavras[c][i] in 'aeiou':
            print(palavras[c][i], end=' ')
