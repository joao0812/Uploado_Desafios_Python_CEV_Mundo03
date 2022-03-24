from time import sleep

def manual(termo):
    print('\33[;;40m')
    sleep(1)
    help(f'{termo}')
    print('\33[m', end='')


def escreva1(txt):
    org = len(txt) + 2
    print('\33[1;30;42m~' * org)
    print(f'{txt:^{org}}')
    print('~' * org)
    print('\33[m', end='')


def escreva2(txt):
    org = len(txt) + 2
    print('\33[1;30;44m~' * org)
    print(f'{txt:^{org}}')
    print('~' * org)
    print('\33[m', end='')


def exit(txt):
    org = len(txt) + 2
    print('\33[1;30;41m~' * org)
    print(f'{txt:^{org}}')
    print('~' * org)
    print('\33[m', end='')


while True:
    escreva1('SISTEMA DE AJUAD PyHELP')
    sleep(0.3)
    resp = input('Funçao da biblioteca ["Sair" p/ sair] ➙ ').capitalize()
    if resp == 'Sair':
        break
    sleep(0.2)
    escreva2(f'Acessando o manual do comando "{resp}"')
    manual(resp)
exit('ATÉ LOGO')