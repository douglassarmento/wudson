m = (float (input ('Primeira nota:')) + float (input ('Segunda nota:')))/2
if m >= 9:
    print (f'Média: {m}. Conceito: A. Estado: APROVADO.')
elif m >= 7.5:
    print (f'Média: {m}. Conceito: B. Estado: APROVADO.')
elif m >= 6:
    print (f'Média: {m}. Conceito: C. Estado: APROVADO.')
elif m >= 4:
    print (f'Média: {m}. Conceito: D. Estado: REPROVADO.')
else:
    print (f'Média: {m}. Conceito: E. Estado: REPROVADO.')