times = ('Atlêtico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'Chapecoense', 'Atlêtico-GO', 'Santos')
print('-'*40)
print(f'Top 5: {times[:5]}')
print('-'*40)
print(f'Lanterna: {times[-4:]}')
print('-'*40)
print(f'Ordem alfabética: {sorted(times)}')
print('-'*40)

if times.count('Chapecoense') == 0:
    print(f'Chapecoense não está no TOP {len(times)} do Brasileirão 2021')
else:
    print(f'Posição do Chapecoense: {times.index("Chapecoense") + 1}º')
print('-'*40)