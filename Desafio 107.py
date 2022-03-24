from aula import Moeda

n1 = float(input('Digite um número: '))

print(f'A metade de {n1} = {Moeda.metade(n1)}')
print(f'O dobro de {n1} = {Moeda.dobro(n1)}')
print(f'Aumentando 10% de {n1} = {Moeda.aumentaPorcento(n1, 10):.2f}')
print(f'Aumentando 13% de {n1} = {Moeda.diminuiPorcento(n1, 13)}')