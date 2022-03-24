def leiaInt(num):
    while True:
        if num.isnumeric():
            break
        else:
            print('\33[;31mDIGITO INVÁLIDO\33[m - Tentar Novamente')
            num = input('Digite um número: ')
    return num



print('-'*30)
n1 = input('Digite um número: ')
print(f'Você digitou {leiaInt(n1)}')
print('-'*30)
