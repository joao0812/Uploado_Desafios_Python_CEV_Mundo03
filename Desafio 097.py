def escreva(txt):
    org = len(txt) + 2
    print('~' * org)
    print(f'{txt:^{org}}')
    print('~' * org)


texto = str(input('Digite uma palavra: ')).strip().capitalize()
escreva(texto)
