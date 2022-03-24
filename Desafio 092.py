from datetime import date

dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Ano'] = int(input('Ano de nascimento: '))
dados['CT'] = int(input('Carteira de trabalho: '))

idade = date.today().year - dados["Ano"]
# Método 01 -> mais personalizado
if dados['CT'] != 0:
    dados['Contrato'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    print(f'Nome: {dados["Nome"]}')
    print(f'Idade: {idade} anos')
    print(f'CTPS: {dados["CT"]}')
    print(f'Ano de Contratação: {dados["Contrato"]}')
    print(f'Salário: R${dados["Salario"]}')
    print(f'Aposentadoria será com: {idade + 35} anos')
else:
    print(f'Nome: {dados["Nome"]}')
    print(f'Idade: {idade}')

# Método 02 -> mais rápido
print('-='*40)
for c, v in dados.items():
    print(f'{c} tem o valor de {v}')

