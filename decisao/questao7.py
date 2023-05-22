c = float (input ('Crédito:'))
s = float (input ('Saldo:'))
d = float (input ('Débito:'))
sa = s - d + c
if sa >= 0:
    print (f'Saldo = {sa}. SALDO POSITIVO.')
else:
    print (f'Saldo = {sa}. SALDO NEGATIVO.')