n = int (input ('Digite a quantidade de maçãs compradas:'))
if n >= 12:
    print (f'O preço das {n} maças é de R$ {n} reais.')
else:
    print (f'O preço das {n} maças é de R$ {n*1.30} reais.')