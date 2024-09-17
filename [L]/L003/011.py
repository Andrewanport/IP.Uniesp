"""""
Decisão da Coroa Real
a. Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo
governante entre três candidatos, baseado na sua pontuação em uma série de provas. 

Crie um programa que receba as notas dos três candidatos e determine qual deles teve a maior média.

Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
que há um empate.
b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.
"""""

C1 = float(input('Digite a média do primeiro candidato: '))
C2 = float(input('Digite a média do segundo candidato: '))
C3 = float(input('Digite a média do terceiro candidato: '))

print(max(C1, C2, C3))

if C1 == C2 or C1 == C3 or C2 == C3:
    print('Há um empate.')


