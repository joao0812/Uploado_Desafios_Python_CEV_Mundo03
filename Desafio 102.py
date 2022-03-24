
def fatorial(num, show=False):
    """
    :param num: valor a ser calculado
    :param show: decide se vai devolver só o resultado do fatorial ou o cálculo inteiro juntamente com a resposta
    :return: restorna o resultado e/ou o cáculo de num fatorial
    """
    fat = 1
    fat_escr =''
    if show == False:
        for c in range(num, 0, -1):
            fat *= c
        return fat
    else:
        for c in range(num, 0, -1):
            fat *= c
            fat_escr += str(c) + ' X '
        fat_escr.strip()
        fat_escr = fat_escr[:-2]
        fat_escr = fat_escr + '= ' + str(fat)
        return fat_escr



n1 = int(input('Digite um número: '))
ext = str(input('Gostaria de ver o fatorial por Extenso[E] ou apenas o Resultado[R]: ')).upper()
if ext == 'E':
    print(f'{fatorial(n1, True)}')
if ext == 'R':
    print(f'{fatorial(n1)}')

