"""""
Guerreiro da Idade Média
a. Descrição: Um guerreiro precisa de uma armadura especial para a batalha. Para forjar a
armadura, ele precisa de uma liga metálica que combina ferro e ouro. O ferreiro diz que a liga
precisa ter no mínimo 70% de ferro. Crie um programa que receba a quantidade de ferro e
ouro em kg e verifique se a porcentagem de ferro na liga é suficiente.
b. Conceito: Operadores aritméticos, operadores lógicos, desvio condicional simples.
"""""

F = float(input("Digite a quantidade de ferro em kg: "))
O = float(input("Digite a quantidade de ouro em kg: "))

PF = (F / (F + O)) * 100

if PF >= 70:
    print(f"A liga tem {PF:.2f}% de ferro. É suficiente para a armadura.")
else:
    print(f"A liga tem {PF:.2f}% de ferro. Não é suficiente para a armadura.")
