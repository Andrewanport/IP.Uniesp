"""""
A Caverna dos Desafios
a. Descrição: Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número
de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta
escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.
b. Conceito: Match-case, operadores relacionais.
"""""

P = int(input('[1] - Porta 1'
              '\n[2] - Porta 2'
              '\n[3] - Porta 3'
              '\n[4] - Porta 4'
              '\n[5] - Porta 5'
              '\nSelecione a sua escolha: '))

match P:

    case 1:
        print('Você enfrentará um leão')

    case 2:
        print('Você enfrentará um rinoceronte')

    case 3:
        print('Você enfrentará um dragão')

    case 4:
        print('Você enfrentará um Dinossauro')

    case 5:
        print('Você enfrentará o Datena (Final Boss)')

    case _:
        print(f'Não existe uma porta número {P}')
