"""""
Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. 
Depois:
a. Imprima o resultado da soma de todos os valores da matriz no terminal;
b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;
"""""

import random

A = [[random.randint(1, 99) for _ in range(10)] for _ in range(10)]


soma = sum(sum(linha) for linha in A)
print(f"Soma de todos os valores da matriz A: \033[1;34m{soma}\033[m")
print(24 * '~~')


B = [[A[i][j] * 3 for j in range(10)] for i in range(10)]

print("Matriz A:")
for linha in A:
    print(linha)

print(24 * '~~')

print("Matriz B:")
for linha in B:
    print(linha)

print(24 * '~~')
