from random import randint
from time import sleep
num = cont = 0
jogo = []
jogo_ant = []
print('-'*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-'*30)
n1 = int(input('Deseja sortear quantos jogos?\n➙ '))

print('{:=^30}'.format(f'SOTEANDO {n1} JOGOS'))
for c in range(1, n1+1):
    sleep(0.8)
    print(f'Jogo {c}: ', end='')
    while cont < 6:
        num = randint(1, 60)
        if jogo_ant.count(num) == 0:
            jogo.append(num)
            jogo_ant.append(num)
            cont += 1

    print(jogo)
    jogo.clear()
    cont = 0
