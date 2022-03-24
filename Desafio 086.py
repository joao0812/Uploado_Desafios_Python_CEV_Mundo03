lista = []
matriz = []
for c in range(0, 3):
    for i in range(0, 3):
        n1 = int(input(f'Digite um valor para [{c},{i}]: '))
        lista.append(n1)
    matriz.append(lista[:])
    lista.clear()
#print(matriz)
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
