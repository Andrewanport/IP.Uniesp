"""""
Campeonato de Corrida de Dragões
a. Descrição: Em um campeonato de corrida de dragões, cada dragão corre uma determinada
distância em um certo tempo. Crie um programa que receba a distância e o tempo de dois
dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma
velocidade.
b. Conceito: Operadores aritméticos, operadores relacionais, desvio condicional composto.
"""""

D1 = float(input("Digite a distância percorrida pelo primeiro dragão (em km): "))
T1 = float(input("Digite o tempo gasto pelo primeiro dragão (em horas): "))
D2 = float(input("Digite a distância percorrida pelo segundo dragão (em km): "))
T2 = float(input("Digite o tempo gasto pelo segundo dragão (em horas): "))

V1 = D1 / T1
V2 = D2 / T2

if V1 > V2:
    print("O primeiro dragão é mais rápido.")
elif V2 > V1:
    print("O segundo dragão é mais rápido.")
else:
    print("Ambos os dragões têm a mesma velocidade.")
