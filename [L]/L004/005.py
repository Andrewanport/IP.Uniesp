"""""
Sequência de Fibonacci:
Contexto: Desenvolva um programa que gere os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário. 
Utilize um loop para calcular e exibir os termos da sequência.
"""""


def fibonacci():
    n = int(input('Número de valores da sequência de Fibonacci: '))
    a, b = 0, 1

    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()


if __name__ == '__main__':
    fibonacci()

