from aula import Moeda

n1 = input('Digite um número: R$')

print(f'A metade de {Moeda.reais(n1)} = {Moeda.reais(Moeda.metade(n1))}')
print(f'O dobro de {Moeda.reais(n1)} = {Moeda.reais(Moeda.dobro(n1))}')
print(f'Aumentando 10% de {Moeda.reais(n1)} = {Moeda.reais(Moeda.aumentaPorcento(n1, 10))}')
print(f'Aumentando 13% de {Moeda.reais(n1)} = {Moeda.reais(Moeda.diminuiPorcento(n1, 13))}')