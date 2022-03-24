from time import sleep
import aula
from aula import interface
def arqexiste(nome): # Veriffica se o arquivo existe no diretório, obs: o arquivo tem q estar na mesma linha de identação do arquivo q está rodando o prorgama
    try:
        a = open(nome, 'rt') # Função responsável por ler Read Text('rt') o arquivo txt 'nome'
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararq(nome): # Utilziado para criar o arquivo, caso o mesmo não exista -> essa condição de criação foi feita no main código
    try:
        a = open(nome, 'wt+') # Write Text + -> o '+' faz com que se crie o arquivo .txt
        a.close
    except:
        print('Houve um erro na criação do arquivo')
    else: 
        print(f'O arquivo "{nome}" foi criado')


def ver_pessoa(nome):
    i = 1
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo')
    else:
        sleep(0.5)
        interface.cabeçalho('lista de pessoas')
        sleep(1)
        print(f'{"Nº":<5}', end='')
        print(f'{"Nome":<30}', end='')
        print(f'{"Idade"}', end='\n')
        sleep(0.5)
        for v in a:
            valor = v.split(';')
            valor[1] = valor[1].replace('\n', '')
            sleep(0.5)
            print(f'{i:<5}{valor[0]:<30}{valor[1]} anos')
            i += 1
    finally:
        a.close()
        
def cadastrar_pessoa(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at', encoding='utf-8') # Append Text, abre o arquivo 'impera.txt' para que seja possível add um valor nesse arquivo
    except:
        print('Erro ao tentar abrir o arquivo')
    else:
        try:
            a.write(f'\n{nome};{idade}') # escreve os valores no arquivo 'impera.txt'
        except:
            print('Erro ao tentar escrever os dados no arquivo')
        else:
            print(f'{nome} adicionado a lista')
            a.close()
    