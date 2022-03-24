lista = []
menor = 0

for c in range(0, 5):
    n1 = int(input('Digite um número: '))
    if c == 0:
        lista.append(n1)
        menor = n1
    elif n1 <= menor:
        lista.insert(lista.index(min(lista)), n1)
        menor = n1
    elif n1 >= menor:
        lista.append(n1)

    print(lista)
print('\33[;32mCONCLUÍDO\33[m')

