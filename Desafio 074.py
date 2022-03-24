from random import randint
valores = ''
menor = maior = 0
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {num}')
print(f'O maior número vale: {max(num)}')
print(f'O menor número vale: {min(num)}')