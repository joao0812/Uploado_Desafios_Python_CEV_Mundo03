from random import randint
from time import sleep

jogo = {}
maior = menor = 0
winner = looser = ' '

num_player = int(input('Quantidade de jogadores\n➙ ')) # Define a quantidade de jogadores
for c in range(1, num_player+1):
    jogo[f'Jogador{c}'] = str(input(f'P{c} ➙ ')).capitalize() # Define o nome do jogador 1 até o a quantidade extipulada
    jogo[f'Dado{c}'] = randint(1, 6) # Jogada
#   print(f'{jogo[f"Jogador{c}"]} ➙ {jogo[f"Dado{c}"]}')
# Verifica o maior e o menor valor e quem tirou esses valores, juntando os nomes em caso de valores iguais
    if c == 1:
        maior = menor = jogo[f'Dado{c}']
        winner = jogo[f'Jogador{c}']
        looser = jogo[f'Jogador{c}']
    else:
        if jogo[f'Dado{c}'] > maior:
            maior = jogo[f'Dado{c}']
            winner = jogo[f'Jogador{c}']
        elif jogo[f'Dado{c}'] == maior:
            winner += ',' + jogo[f'Jogador{c}']
        if jogo[f'Dado{c}'] < menor:
            menor = jogo[f'Dado{c}']
            looser = jogo[f'Jogador{c}']
        elif jogo[f'Dado{c}'] == menor:
            looser += ', ' + jogo[f'Jogador{c}']

print('-='*20)
print('{:^40}'.format('RESULTADO'))
print('-='*20)

for v in range(1, num_player+1):
    sleep(0.8)
    print(f'{jogo[f"Jogador{v}"]:<10} ➙ {jogo[f"Dado{v}"]}')

sleep(0.8)
print('-='*20)
print('{:^40}'.format('RANKIN'))
print('-='*20)
# Percorre o dicionário, pegando Dado por Dado e comparando com 6 até 1
for x in range(6, 0, -1):
    for y in range(1,  num_player+1):
        if jogo[f'Dado{y}'] == x:
            sleep(0.8)
            print(f'{jogo[f"Jogador{y}"]:<10} ➙ {jogo[f"Dado{y}"]}')

sleep(0.8)
print('-='*20)
print('{:^40}'.format('\33[;34mFIM DE JOGO\33[m'))
print('-='*20)
sleep(0.8)
print(f'\33[;32mVencedor\33[m ➙ {winner:-<25} {maior}')
sleep(0.8)
print(f'\33[;33mPerdedor\33[m ➙ {looser:-<25} {menor}')