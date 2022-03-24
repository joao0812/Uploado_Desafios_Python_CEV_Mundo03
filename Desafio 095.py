dici = {}
jogadores = []
gols = []
soma = num = 0
while True:
    dici['Nome'] = str(input('Nome do jogador: ')).capitalize()

    partidas = int(input(f'Quantas partidas {dici["Nome"]} jogou\n➙ '))
    for c in range(1, partidas+1):
        quant_gols = int(input(f'Quantos gols foram feitos na partida {c}: '))
        soma += quant_gols
        gols.append(quant_gols)

    dici['Total'] = soma
    dici['Gols'] = gols[:]

    jogadores.append(dici.copy())
#   print(dici)
#   print(jogadores)
#   print(len(jogadores))
    perg = str(input('Deseja continuar? [S/N] ')).upper()
    if perg == 'N':
        break
    gols.clear()
    soma = 0

print('-'*40)
print(f'{"Nº":<3} {"Jogador":<15} {"Gols":<12} Total')

for l in range(0, len(jogadores)):
    print(f'{l:<5}', end='')
    print(f'{jogadores[l]["Nome"]:<15}', end='')
    print(f'{jogadores[l]["Gols"]}', end='')
    print('{:<10}'.format(' '), end='')
    print(f'{jogadores[l]["Total"]}')

while True:
    num = int(input('Mostrar dados de qual Jogador? [999 p/ parar] '))
    if num == 999:
        break
    elif num > len(jogadores):
        print('\33[;31mDIGITO INVÁLIDO\33[m - Tente novamenete')
    else:
        print(f'{jogadores[num]["Nome"]:=^40}')
        for c in range(0, len(jogadores[num]['Gols'])):
            print(f'Partida {c+1:-<20} {jogadores[num]["Gols"][c]}')

print('\33[;32mCONCLUÍDO\33[m')