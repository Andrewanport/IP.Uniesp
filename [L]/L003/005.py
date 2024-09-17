"""""
Jornada no Deserto
a. Descrição: Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de
água que tem é suficiente para chegar ao próximo oásis. Ele calcula que precisa de 2 litros de
água para cada quilômetro. Crie um programa que receba a quantidade de água disponível e a
distância até o oásis, e informe se a água é suficiente.
b. Conceito: Operadores aritméticos, desvio condicional simples.
"""""

A = float(input("Quantos litros de água você tem? "))
D = float(input("Qual a distância até o oásis em km? "))

if A >= (D * 2):
    print("A água disponível é suficiente para chegar ao oásis.")
else:
    print("A água disponível não é suficiente para chegar ao oásis.")
