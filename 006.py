"""""
Contagem de Moedas

a. Descrição: Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de
25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o
valor total que o colecionador tem.

b. Conceito: Operadores aritméticos, tipos de dados (float).

"""""
S = 0

print(15 * '~~')
print('         Seu depósito:')
print(15 * '~~')

while True:

    x = int(input(('| [1] R$ 1,00'
                   '\n| [2] R$ 0,50'
                   '\n| [3] R$ 0,25'
                   '\n| [4] Finalizar programa'
                   '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
                   '\nSelecione qual tipo de moeda deseja depositar: ')))

    if x == 4:
        break

    y = int(input('Digite a quantidade de moedas que deseja depositar: '))

    if x == 1:
        S += (1 * y)

    elif x == 2:
        S += (0.5 * y)

    elif x == 3:
        S += (0.25 * y)

print(30 * '~~')

print(f'O valor total depositado foi de: R${S:.2f}')

print(30 * '~~')
