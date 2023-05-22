from random import choice

def boneco(erros):

    if erros == 1:

        print('')
        print('|---------')
        print('|        |')
        print('|        O')
        print('|       /|\ ')
        print('|       /')
        print('|')
        print('')

    if erros == 2:

        print('')
        print('|---------')
        print('|        |')
        print('|        O')
        print('|       /|\ ')
        print('|')
        print('|')
        print('')

    if erros == 3:

        print('')
        print('|---------')
        print('|        |')
        print('|        O')
        print('|       /|')
        print('|')
        print('|')
        print('')

    if erros == 4:

        print('')
        print('|---------')
        print('|        |')
        print('|        O')
        print('|        |')
        print('|')
        print('|')
        print('')

    if erros == 5:

        print('')
        print('|---------')
        print('|        |')
        print('|        O')
        print('|')
        print('|')
        print('|')
        print('')

    if erros == 6:

        print('')
        print('|---------')
        print('|        |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('')

temas = {
    1: ['cachorro', 'gato', 'passaro'],
    2: ['italia', 'franca', 'uruguai'],
    3: ['maca', 'banana', 'pessego']
}

print('')
print('----------------------------------- JOGO DA FORCA -----------------------------------')
print('')

acertos = 0
erros = 0
palavra = []

def condicoes(escolha):

    global acertos, erros, palavra
    letras_palavra = set(escolha)
    while erros < 6:

        print()
        letra = input('Digite uma letra: ')

        if letra == '':
            print('Opção inválida.')
            continue

        if letra in escolha:

            if letra not in palavra:
                print('Você acertou a letra!')
                acertos += escolha.count(letra)
                palavra.extend([letra] * escolha.count(letra))

                if set(palavra) == letras_palavra:
                    break
            else:
                print('Você já acertou essa letra!')
        else:
            print('Você errou a letra!')
            erros += 1
            boneco(erros)
            
    print('')

    if set(palavra) == letras_palavra:
        print(f'Parabéns! Você acertou a palavra {escolha.upper()}!') 
    else:
        print(f'O jogo acabou! A palavra escolhida era {escolha.upper()}.')

tema = int(input('Escolha um tema: [1] ANIMAIS - [2] PAÍSES - [3] FRUTAS: '))
print()

if tema in temas:
    palavra_escolhida = choice(temas[tema])
    print(f'Você escolheu o tema: {list(temas.keys())[list(temas.values()).index(temas[tema])]}.')
    condicoes(palavra_escolhida)