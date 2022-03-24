from datetime import date

def voto(a):
    if a < 18:
        return 'NEGADO'
    if 65 >= a >= 18:
        return 'OBRIGATÓRIO'
    if a > 65:
        return 'OPICIONAL'


ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'Idade: {idade} ➙ Característica do voto: \33[;33m{voto(idade)}\33[m')