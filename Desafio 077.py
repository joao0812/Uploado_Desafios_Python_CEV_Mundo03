palavras = ('banana', 'pera', 'maça', 'melancia', 'morango')
aux = ''
# print(palavras[0][0])

for c in range(0, len(palavras)):
    print(f'A palavra \33[;33m{palavras[c]}\33[m tem as vogais: ', end='')
    for i in range(0, len(palavras[c])):
        if palavras[c][i] in 'aeiou':
            aux += palavras[c][i] + ' '
    print(aux)
    aux = ' '


