"""""
A Batalha Final
a. Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
busque uma nova arma.
b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.
"""""

EA = int(input("Digite o poder de ataque da espada: "))
ED = int(input("Digite a durabilidade da espada: "))

AA = int(input("Digite o poder de ataque do arco: "))
AD = int(input("Digite a durabilidade do arco: "))

LA = int(input("Digite o poder de ataque da lança: "))
LD = int(input("Digite a durabilidade da lança: "))

if EA > 50 and ED > 70:
    print("A espada é a arma mais adequada.")
elif AA > 50 and AD > 70:
    print("O arco é a arma mais adequada.")
elif LA > 50 and LD > 70:
    print("A lança é a arma mais adequada.")
else:
    print("Nenhuma arma é adequada. O herói deve buscar uma nova arma.")
