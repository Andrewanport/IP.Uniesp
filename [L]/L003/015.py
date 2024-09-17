"""""
Portal de Viagem no Tempo
a. Descrição: Um cientista está criando um portal de viagem no tempo que só pode ser ativado se
todos os parâmetros estiverem corretos: energia acima de 80%, coordenadas de destino
precisas, e o tempo ajustado corretamente. Crie um programa que receba esses valores e use
operadores lógicos para verificar se o portal pode ser ativado. Se qualquer parâmetro estiver
incorreto, o programa deve indicar qual é o problema.
b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.
"""""

E = int(input("Digite o nível de energia (%): "))
C = input("As coordenadas de destino estão precisas? (S/N) ").upper()
T = input("O tempo está ajustado corretamente? (S/N) ").upper()

if E > 80 and C == "S" and T == "S":
    print("O portal de viagem no tempo pode ser ativado.")

else:

    if E <= 80:
        print("Energia insuficiente.")

    if C != "S":
        print("Coordenadas imprecisas.")

    if T != "S":
        print("O tempo não está ajustado corretamente.")
