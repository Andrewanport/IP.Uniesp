"""""
O Tesouro Escondido
a. Descrição: Um mapa do tesouro tem duas partes, A e B. A primeira parte está escondida no X
número de passos para o norte, e a segunda no Y número de passos para o leste. Crie um
programa que receba os valores de X e Y e calcule a distância total que o pirata precisa
percorrer para chegar ao tesouro (soma de X e Y).
b. Conceito: Operadores aritméticos, variáveis.
"""""

X = int(input("Digite o número de passos para o norte (X): "))
Y = int(input("Digite o número de passos para o leste (Y): "))

D = X + Y

print(f"A distância total que o pirata precisa percorrer é: {D} passos.")
