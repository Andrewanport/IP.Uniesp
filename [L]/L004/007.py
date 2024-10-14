"""""
Calculadora de Fatorial:
Contexto: Implemente um programa que calcule o fatorial de um número fornecido pelo usuário. 
Utilize um loop para realizar as multiplicações necessárias.
"""""


def calcular_fatorial():
    N = int(input('Digite um número para calcular o fatorial: '))
    F = 1
    for i in range(2, N + 1):
        F *= i
    print(f'O fatorial de {N} é {F}.')


if __name__ == '__main__':
    calcular_fatorial()
