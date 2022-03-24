from math import ceil
aluno = []
nota = []

# Pegando os valores da lista aluno e nota, e colocando nota em aluno ficando assim: [ [], [ , ] ]
while True:
    aluno.append(input('Nome: ').capitalize())
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:])
    nota.clear()
    perg = input('Deseja Continuar? [S/N]\n➙ ').upper()
    if perg == 'N':
        break
    while perg not in 'SN':
        print('\33[;31mDIGITO INVÁLIDO\33[m - Tentar novamente')
        perg = input('Deseja Continuar? [S/N]\n➙ ').upper()
        if perg == 'N':
            break

print('-='*15)
print('{:^40}'.format('\33[;32mCONCLUÍDO\33[m'))
print('-='*15)
# Organizando oq cada coluna é, orgazinando o print
print('Nº', end=' ')
print('{:^20}'.format('ALUNO'), end=' ')
print('{:>6}'.format('MÉDIA'))
print('¨'*30)
# Mostrando o número do aluno, começando com 0, o nome do aluno e a média dele
for i in range(0, len(aluno), 2):
    media = (aluno[i+1][0] + aluno[i+1][1])/2
    num = ceil(i/2)
    print('{:<10}'.format(num), end='')
    print('{:<11}'.format(aluno[i]), end=' ')
    print('{:>8.2f}'.format(media))
print('-'*30)
# Laço de repetição para indicar quais dos alunos listados se quer ver as notas
while True:
    num_aluno = int(input('Mostrar notas de quais alunos? [999 p/ parar] '))
    if num_aluno == 999:
        break
    print(f'Aluno \33[;33m{aluno[num_aluno*2]}\33[m ➙ {aluno[(num_aluno*2)+1]}')
    print('-'*30)
print('\33[1;32mProcesso finalizado com sucesso\33[m')


