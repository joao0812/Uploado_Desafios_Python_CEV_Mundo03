from time import sleep


def maior(* num):
    print('-='*20)
    sleep(0.4)
    print(f'Foram informados \33[;33m{len(num)}\33[m ➙ ', end='')
    for c in range(0, len(num)):
        sleep(0.3)
        print(f'{num[c]}', end=' ')
    print()
    sleep(0.3)
    if len(num) > 0:
        print(f'O maior valor vale ➙ ', end='')
        sleep(0.5)
        print(f'\33[;33m{max(num)}\33[m')
    else:
        print('O maior valor vale ➙ ', end='')
        sleep(0.5)
        print('\33[;33m0\33[m')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
