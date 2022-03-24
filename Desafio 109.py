from aula import Moeda

n1 = float(input('Digite um número: '))

print(f'A metade de {Moeda.reais(n1)} = {Moeda.metade(n1, True)}')
print(f'O dobro de {Moeda.reais(n1)} = {Moeda.dobro(n1, True)}')
print(f'Aumentando 10% de {Moeda.reais(n1)} = {Moeda.aumentaPorcento(n1, 10, True)}')
print(f'Aumentando 13% de {Moeda.reais(n1)} = {Moeda.diminuiPorcento(n1, 13, True)}')