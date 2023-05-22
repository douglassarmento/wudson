cadastro = []
cadastrogeral = []
c = int (input ('Número de cadastros:'))
for x in range (0, c):
    print ()
    nome = str (input ('Nome:'))
    idade = int (input ('Idade:'))
    email = str (input ('E-mail:'))
    print ()
    cadastro = [nome, idade, email]
    cadastrogeral.append (cadastro)
print ('-------------------- CADASTROS --------------------')
print ()
for cadastro in cadastrogeral:
    print (f'Nome: {cadastro [0]} | Idade: {cadastro [1]} anos | E-mail: {cadastro [2]}')
    print ()