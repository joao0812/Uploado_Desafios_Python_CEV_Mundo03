lista = []
matriz = []
soma_par = soma_coluna3 = 0
for c in range(0, 3):
    for i in range(0, 3):
        n1 = int(input(f'Digite um valor para [{c},{i}]: '))
        lista.append(n1)
        if n1 % 2 == 0:
            soma_par += n1
    matriz.append(lista[:])
    lista.clear()
for c in range(0, 3):
    soma_coluna3 += matriz[c][2]

print('-'*40)
print(f'''{(matriz[0])}
{matriz[1]}
{matriz[2]}''')
print('-'*40)
print(f'A soma dos valores pares vale: {soma_par}')
print(f'A soma dos valores da coluna 3 vale: {soma_coluna3}')
print(f'O maior valor da segunda linha vale: {max(matriz[1])}')