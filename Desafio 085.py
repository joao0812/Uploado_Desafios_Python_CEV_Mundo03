lista = []
cont_par = cont_imp = 0
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista.append(valor)
        cont_par += 1
    else:
        lista.insert(0, valor)
        cont_imp += 1

print(lista)
print(f'Lista PAR: {sorted(lista[-cont_par:])}')
print(f'Lista ÍMPAR: {sorted(lista[:cont_imp])}')