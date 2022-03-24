cont = 0
lista = []
while True:
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    cont += 1
    perg = input('Deseja continuar: [S/N] ').upper()
    if perg == 'N':
        break
    while perg not in 'S':
        print('\33[;31mDIGITO INVÁLIDO\33[m. Tente novamente')
        perg = input('Deseja continuar: [S/N] ').upper()
        if perg == 'N':
            break
print(f'Números digitados: {lista}')
print(f'Total de números digitados: {cont}')
if lista.count(5) >= 1:
    print(f'Na sua lista teve um total de \33[;33m{lista.count(5)}\33[m números 5, tendo o primeiro na posição {lista.index(5)}')
else:
    print('A lista não possui o número 5')
decrescente = lista.sort(reverse=True)
print(f'Lista em ordem descrescente: {decrescente}')

