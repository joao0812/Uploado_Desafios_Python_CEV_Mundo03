def notas(* num, sit=False):
    aluno = {}
    soma = cont = 0
    for c in num:
        soma += c
        cont += 1
    media = soma/len(num)
    maior = max(num)
    menor = min(num)

    aluno['Total'] = cont
    aluno['Maior'] = maior
    aluno['Menor'] = menor
    aluno['Média'] = media
    if sit:
        if media >= 7:
            aluno['Situação'] = 'BOA'
        if media < 7 and media >= 5:
            aluno['Situação'] = 'RASOÁVEL'
        if media < 5:
            aluno['Situação'] = 'RUIM'
    return aluno


resp = notas(3, 1, 10, sit=True)
print(resp)