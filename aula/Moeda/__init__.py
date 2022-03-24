def metade(n=0, show=False):
    n = float(n)
    n = n/2
    if show:
        return reais(n)
    else:
        return n


def dobro(n=0, show=False):
    n = float(n)
    n = n * 2
    if show:
        return reais(n)
    else:
        return n


def aumentaPorcento(v=0, p=0, show=False):
    v = float(v)
    v = v * (1 + (p/100))
    if show:
        return reais(v)
    else:
        return v



def diminuiPorcento(v=0, p=0, show=False):
    v = float(v)
    v = v * (1 - (p/100))
    if show:
        return reais(v)
    else:
        return v


def reais(termo=''):
    if termo == '':
        aux = f'R$0,00'
    else:
        aux = f'R${float(termo):.2f}'.replace('.', ',', 1)
    return aux


def resumo(n, a, r, show=False):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    if show:
        print(f'{"Preço analisado:":<25} {reais(n)}')
        print(f'{"Dobro do Preço:":<25} {dobro(n, show)}')
        print(f'{"Metade do valor:":<25} {metade(n, show)}')
        print(f'{f"{a}% de aumento:":<25} {aumentaPorcento(n, a, show)}')
        print(f'{f"{r}% de redução":<25} {diminuiPorcento(n, r, show)}')
    else:
        print(f'{"Preço analisado:":<25} {n}')
        print(f'{"Dobro do Preço:":<25} {dobro(n)}')
        print(f'{"Metade do valor:":<25} {metade(n)}')
        print(f'{f"{a}% de aumento:":<25} {aumentaPorcento(n, a)}')
        print(f'{f"{r}% de redução":<25} {diminuiPorcento(n, r)}')


