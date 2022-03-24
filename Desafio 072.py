n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartose', 'quinse', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 10: '))
    while num > 20 or num < 0:
        print('\33[;31mDigito Inválido\33[m\nTente novamente')
        num = int(input('Digite um número entre 0 e 10: '))
    ext = n[num]
    print(f'Você digitou o número \33[;33m{ext}\33[m')
    perg = input('Deseja continuar? [N/S] ').upper()
    if perg == 'N':
        break
