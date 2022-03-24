lista = []
while True:
    n1 = int(input('Digite um número: '))
    if n1 not in lista:
        lista.append(n1)
        perg = input('Deseja digitar outro número? [S/N] ').upper()
        if perg == 'N':
            break
    else:
        print(f'\33[;31mATENÇÃO\33[m Número \33[;33m{n1}\33[m já digitado')
        perg = input('Deseja digitar outro número? [S/N] ').upper()
        if perg == 'N':
            break
print('-' * 40)
print(f'Valores digitados em ordem crescente: {sorted(lista)}')