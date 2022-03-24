from pickle import APPEND
from time import sleep
from colorama import Fore, Style, Back, init
init()

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.upper().center(42))
    print(linha())

def menu(lista, msg):
    sleep(0.5)
    cabeçalho(msg)
    c = 1
    for item in lista:
        print(Fore.CYAN + f'[{c}] ➙  {item}' + Style.RESET_ALL)
        c+=1
    print(linha())


'''def ver_pessoa(lista):
    cabeçalho('lista de pessoas')
    valor = (len(lista))/2
    print(f'{"Nº":<5}', end='')
    print(f'{"Nome":<30}', end='')
    print(f'{"Idade"}')
    for c in range(0, int(valor)):
        print(f'{c+1:<5}', end='')
        print(f'{lista[c*2]:<30}', end='')
        print(f'{lista[(c*2)+1]} anos')
        sleep(0.5)'''
    
'''def cadastrar_pessoa(lista):
    nome = str(input('Nome: '))
    lista.append(nome)
    idade = int(input('Idade: '))
    lista.append(idade)'''

# def Sair():





   