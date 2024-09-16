"""""
Contexto: Determinação do tipo de triângulo. 
Questão: Peça ao usuário para inserir três lados de um triângulo e determine se é:
um triângulo equilátero, isósceles ou escaleno.
"""""

L1 = float(input(f'Insira o valor do lado (1): '))
L2 = float(input(f'Insira o valor do lado (2): '))
L3 = float(input(f'Insira o valor do lado (3): '))

if L1 == L2 == L3:
    print('Este triângulo é equilátero!')

elif L1 != L2 != L3:
    print('Este triângulo é Escaleno!')

else:
    print('Este triângulo é Isóceles!')
