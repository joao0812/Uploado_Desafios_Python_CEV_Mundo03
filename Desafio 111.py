# Na questão foi pedido dois pacotes "Moeda" e "dados" só q eu já tinha criado eles dentro de "aulas", não precisando
# recriar os mesmos, só iria ter uma pasta a mais q tem a pasta "aula" nela, aí para importar "Moeda" ficaria:
# from PastaMaior.aula import Moeda -> onde "PastaMaior" seria a pasta q engloba as demais pastas

from aula import Moeda

n1 = input('Digite um número: ')
Moeda.resumo(n1, 80, 30, True)