from random import randint

numeros = []


def sorteia():
    print('Números sorteados ➙ ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
    print()


def somaPar(num):
    print(f'Soma dos números pares de {num} ➙ ', end='')
    soma = 0
    for c in num:
        if c%2 == 0:
            soma += c
    print(soma)


sorteia()
somaPar(numeros)


