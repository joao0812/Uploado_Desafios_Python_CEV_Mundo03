import colorama
colorama.init()


def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(colorama.Fore.RED + 'ERRO! - Digite um número inteiro válido' + colorama.Style.RESET_ALL)
            continue
        except KeyboardInterrupt:
            print(colorama.Fore.YELLOW + 'O usuário interrompeu o programa' + colorama.Style.RESET_ALL)
            return 0
        else:
            return n


def leiafloat():
    while True:
        try:
            n = float(input('Digite um número flutuante: '))
        except (ValueError, TypeError):
            print(colorama.Fore.RED + 'ERRO! - Digite um número flutuante válido' + colorama.Style.RESET_ALL)
            continue
        except KeyboardInterrupt:
            print(colorama.Fore.YELLOW + 'O usuário interrompeu o programa' + colorama.Style.RESET_ALL)
            return 0
        else:
            return n
            

num_int = leiaInt()
num_float = leiafloat()
print(f'O número inteiro digitado foi {num_int}')
print(f'O número inteiro digitado foi {num_float}')
