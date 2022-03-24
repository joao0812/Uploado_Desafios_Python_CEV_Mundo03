def ficha(j='N', g='G'):
    if j == 'N' and g == 'G':
        global jogador, gols
        jogador = '<<desconhecido>>'
        gols = 0
    elif j == 'N':
        jogador = '<<desconhecido>>'
    elif g == 'G':
        gols = 0



jogador = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))

if jogador == '' and gols == '':
    ficha()
elif jogador == '':
    ficha(g=gols)
elif gols == '':
    ficha(j=jogador)
else:
    ficha(jogador, gols)
print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')