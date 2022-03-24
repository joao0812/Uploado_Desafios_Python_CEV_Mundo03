gols = []
soma = 0

jogador = str(input('Nome do jogador: '))

dici = {'Nome': jogador}
partidas = int(input(f'Quantas partidas {jogador} jogou\n➙ '))

for c in range(1, partidas+1):
    quant_gols = int(input(f'Quantos gols foram feitos na partida {c}: '))
    soma += quant_gols
    gols.append(quant_gols)
dici['Gols'] = gols
dici['Total'] = soma
print('-'*40)
for k, v in dici.items():
    print(f'{k} ➙ {v}')
print('-'*40)
print(f'O jogador {jogador} jogou {partidas} partidas: ')
for i, v in enumerate(gols):
    print('{:^30}'.format(f'Na partida {i+1} ➙ {v} gols'))
print(f'Total de {soma} gols')