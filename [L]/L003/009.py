"""""
Escolha de Feitiços
a. Descrição: Um mago tem três feitiços: fogo, água e terra. Crie um programa que receba a
escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o comando match-case para
exibir o feitiço escolhido.
b. Conceito: Match-case, variáveis.
"""""

F = int(input("Escolha um feitiço:"
              "\n[1] - FOGO "
              "\n[2] - ÁGUA"
              "\n[3] - TERRA"
              "\n-> "))

# Uso do match-case
match F:
    case 1:
        print("Você escolheu o feitiço de fogo.")
    case 2:
        print("Você escolheu o feitiço de água.")
    case 3:
        print("Você escolheu o feitiço de terra.")
    case _:
        print("Escolha inválida.")
