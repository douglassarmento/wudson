from random import choice
convidados = ['Mozart', 'Bach', 'Palestrina', 'Vivaldi', 'Tchaikovsky']
convidadosformat = ', '.join(char for char in convidados if char != "'")
print ()
for x in convidados:
    print (f'Olá, Sr. {x}. Gostaríamos de contar com sua presença em nosso jantar.')
ausente = choice (convidados)
print ()
print (f'O convivado {ausente} não poderá jantar.')
convidados.remove (ausente)
listaespera = ['Chopin', 'Liszt', 'Beethoven']
escolhido = choice (listaespera)
print ()
print (f'O escolhido para se apresentar ao jantar foi {escolhido}.')
listageral = convidados.append (escolhido)
print ()
print (f'A lista definitiva é composta pelos Srs. {convidadosformat}.')
print ()
for y in convidados:
    print (f'Olá, Sr. {y}. Gostaríamos de contar com sua presença em nosso jantar.')