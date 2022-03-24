aluno = {}

nome = str(input('Digite seu nome: ')).capitalize()
media = float(input(f'Digite a média de {nome}: '))

aluno['Nome'] = nome
aluno['Nota'] = media

if media >= 7:
    resu = '\33[;32mAPROVADO!\33[m'
else:
    resu = '\33[;31mREPROVADO!\33[m'

print(f'{aluno["Nome"]} ➙ {aluno["Nota"]:.2f} ➙ {resu}')

