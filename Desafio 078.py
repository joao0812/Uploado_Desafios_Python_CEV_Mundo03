maior = menor = 0
valor = []
maior_cont = menor_cont = ''
for c in range(0, 5):
    n1 = int(input('Digite um número: '))
    valor.append(n1)
    if c == 0:
        maior = n1
        menor = n1
    if n1 >= maior:
        maior = n1
    if n1 <= menor:
        menor = n1

for i in range(0, len(valor)):
    if valor[i] == maior:
        maior_cont += str(i) + ' '
    if valor[i] == menor:
        menor_cont += str(i) + ' '

print(f'Números digitados: {valor}')
print(f'Maior valor: \33[;33m{maior}\33[m na posição ➙ {maior_cont}')
print(f'Menor valor: \33[;33m{menor}\33[m na posição ➙ {menor_cont}')