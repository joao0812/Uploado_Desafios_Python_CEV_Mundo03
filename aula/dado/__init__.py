def verifica(msg):
    from colorama import Fore, Style
    while True:
        try:
            n = int(input(f'{msg}'))
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO! ' + Style.RESET_ALL + 'Digite um número inteiro válido')
        except KeyboardInterrupt:
            print(Fore.RED + 'Usuário finalizou o programa' + Style.RESET_ALL)
            return 0
        else:
            return n
    
