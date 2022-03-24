lista = []
lista_imp = []
lista_par = []

while True:
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    if n1 % 2 == 0:
        lista_par.append(n1)
    else:
        lista_imp.append(n1)
    perg = input('Deseja continuar? [S/N] ').upper()
    if perg == 'N':
        break
    while perg not in 'S':
        print('\33[;31mDIGITO INVÁLIDO\33[m. Tente novamente')
        perg = input('Deseja continuar: [S/N] ').upper()
        if perg == 'N':
            break
print(f'Lista ORIGINAL: {lista}')
print(f'Lista PAR: {lista_par}')
print(f'Lista ÍMPAR: {lista_imp}')