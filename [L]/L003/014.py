"""""
O Julgamento do Sábio
a. Descrição: Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual
guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa.
Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o
vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve
considerar a defesa como critério de desempate.
b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.
"""""

A1 = int(input("Digite o ataque do primeiro guerreiro: "))
D1 = int(input("Digite a defesa do primeiro guerreiro: "))

A2 = int(input("Digite o ataque do segundo guerreiro: "))
D2 = int(input("Digite a defesa do segundo guerreiro: "))

S1 = A1 + D1
S2 = A2 + D2

if S1 > S2:
    print("O primeiro guerreiro é o vencedor.")

elif S2 > S1:
    print("O segundo guerreiro é o vencedor.")

else:

    if D1 > D2:
        print("O primeiro guerreiro é o vencedor pelo critério de desempate (defesa).")

    elif D2 > D1:
        print("O segundo guerreiro é o vencedor pelo critério de desempate (defesa).")

    else:
        print("Os guerreiros empataram.")
