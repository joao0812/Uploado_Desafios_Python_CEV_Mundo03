from time import sleep

def contator(i, f, p):
    print('-='*20)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        for c in range(i, f+1, p):
            sleep(0.3)
            print(f'{c}', end=' ')
    else:
        for c in range(i, f-1, -p):
            sleep(0.3)
            print(f'{c}', end=' ')
    print()


contator(1, 10, 1)
contator(10, 0, 2)
print('-='*20)
print('Agora sua vez de escolher os valores')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contator(inicio, fim, passo)
print('\33[;32mCONCLUÍDO\33[m')