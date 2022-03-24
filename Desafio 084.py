dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear() #Limpa os dados para que os mesmos n se repitam na lista pessoas
    perg = input('Deseja continuar? [S/N] ').upper()
    if perg == 'N':
        break

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso vale: {maior}Kg ➙ ', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'{c[0]}', end=' ')
print(f'\nO menor peso vale: {menor}Kg ➙ ', end='')
for c in pessoas:
    if c[1] == menor:
        print(f'{c[0]}', end=' ')


