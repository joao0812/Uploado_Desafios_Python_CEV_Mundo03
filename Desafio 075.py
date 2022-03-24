par = aux = aux2 = 0
num_par = valores = ''

n1 = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
          int(input('Digite um número: ')), int(input('Digite um número: ')))

for c in range(0, 5):
    if n1[c] % 2 == 0:
        par += 1
        num_par += str(n1[c]) + ' '

print(f'Números digitados: {n1}')
print(f'Quantidade de 9: {n1.count(9)}')
if 3 in n1:
    index = n1.index(3) + 1
    print(f'O número 3 aparece primeiro na posição: {index}ª')
else:
    print('O número 3 não foi digitado')
print(f'Quantidade de números pares: {par} ➙ {num_par}')
