"""""
Contagem de Moedas
a. Descrição: Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de
25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o
valor total que o colecionador tem.
b. Conceito: Operadores aritméticos, tipos de dados (float).
"""""

M1 = int(input("Número de moedas de R$ 1.00: "))
M50 = int(input("Número de moedas de R$ 0.50: "))
M25 = int(input("Número de moedas de R$ 0.25: "))

T = M1 * 1.00 + M50 * 0.50 + M25 * 0.25

print(f"O valor total das moedas é: R${T:.2f}")
