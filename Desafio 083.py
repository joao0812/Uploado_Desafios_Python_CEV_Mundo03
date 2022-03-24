cont = c = 0
expressao = input('Digite uma expressão: ')
num = len(expressao)
while num > 0:
    if expressao[c] == '(':
        cont += 1
    elif expressao[c] == ')':
        cont -= 1
    if cont < 0:
        print('Sua expressão está incorreta')
        break
    c += 1
    num -= 1
if cont == 0 or (expressao.count('(') == 0 and expressao.count(')') == 0):
    print('Sua expressão está correta')