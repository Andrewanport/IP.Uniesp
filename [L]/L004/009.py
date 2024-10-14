"""""
Desenho de Padrões com Caracteres:
Contexto: Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos. 
Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.
"""""


def desenhar_triangulo():
    A = int(input('Digite a altura do triângulo: '))

    for i in range(1, A + 1):

        E = ' ' * (A - i)  # Número de espaços à esquerda

        print(E + '#' * (2 * i - 1))  # Centraliza o triângulo com 2*i - 1 caracteres '#' (pra ser ímpar)


if __name__ == '__main__':
    desenhar_triangulo()

