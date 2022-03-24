cont = aux = soma = 0
dici = {}
grupo = []

while True:
    dici['Nome'] = str(input('Nome: ')).capitalize()
    dici['Idade'] = int(input('Idade: '))
    dici['Sexo'] = str(input('Sexo: ')).upper()
    soma += dici['Idade']
    cont += 1
    aux += 1
    grupo.append(dici.copy())
    perg = str(input('Deseja continuar? [S?N]\n➙ ')).upper()
    if perg == 'N':
        break
# print(dici)
# print(grupo)
media = soma/cont

print('-='*30)
print(f'Foram cadastradas {cont} pessoas')
print(f'A média do grupo vale: {media:.2f} anos')
print('Mulheres: ', end='')
for l in range(0, cont):
    if grupo[l]['Sexo'] == 'F':
        print(f'{grupo[l][f"Nome"]}', end=' | ')

print('\nPessoas com idade acima da média: ')
for l in range(0, cont):
    if grupo[l]['Idade'] >= media:
        print(f'-Nome: {grupo[l][f"Nome"]}; Sexo: {grupo[l]["Sexo"]}, Idade: {grupo[l]["Idade"]}')

print('\33[;32mCONCLUÍDO\33[m')
