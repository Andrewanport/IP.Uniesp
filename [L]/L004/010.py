"""""
Simulador de Lançamento de Dados:
Contexto: Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário. 
Utilize um loop para realizar os lançamentos e exibir os resultados.
"""""

from time import sleep
import random


def lancar_dado():

    J = int(input('Número de jogadas: '))
    for i in range(J):

        R = random.randint(1, 6)

        print(f'{i+1}º jogada: \033[1;34m{R}\033[m')
        sleep(1)


if __name__ == '__main__':
    lancar_dado()

