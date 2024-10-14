"""""
Tabuada Personalizada:
Contexto: Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse número (de 1 a 10). 
Utilize um loop para realizar as multiplicações e exibir os resultados de forma organizada.
"""""


def tabuada():
    N = int(input('Digite um número para ver sua tabuada: '))

    for i in range(1, 11):

        print(f'|{N} x {i}| = \033[1;32m{N * i}\033[m')


if __name__ == '_main__':
    tabuada()
