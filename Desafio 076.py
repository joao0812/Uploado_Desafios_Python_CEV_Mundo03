from math import ceil
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*42)
print('{:^50}'.format('\33[;33mLISTA DE PREÇOS\33[m'))
print('-'*42)
for c in range(0, 9):
    print(c+1, end=' ')
    print('{:.<30}R$'.format(produtos[c*2]), end=' ')
    print('{:>6.2f}'.format(produtos[(c * 2) + 1]))
print('-'*42)

