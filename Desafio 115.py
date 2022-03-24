from time import sleep
from aula import dado, interface, arquivo
from colorama import Fore, Style, Back, init


init()
menu_lista = ['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sitema']


arq = 'impera.txt'
if not arquivo.arqexiste(arq):
    arquivo.criararq(arq)

while True:
    interface.menu(menu_lista, 'menu principal')
    n = dado.verifica('Sua Opção: ')
    if n == 0:
        break
    elif n == 1:
        arquivo.ver_pessoa(arq)
    elif n == 2:
        interface.cabeçalho('novo cadastro')
        sleep(1)
        nome = input('Nome: ')
        idade = dado.verifica('Idade: ')
        arquivo.cadastrar_pessoa(arq, nome, idade)
    elif n == 3:
        break
    else:
        print(Fore.RED + 'ERRO! ' + Style.RESET_ALL + 'Digite uma opção válida')
        sleep(1)
print('ENCERRANDO PROGRAMA')
sleep(1)

