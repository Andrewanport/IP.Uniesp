"""""
Contexto: Pesquisa eleitoral.
Questão: Solicite ao usuário que insira um número: 
1 para o candidato A, 2 para o candidato B, 3 para o candidato C 
e qualquer outro número para voto nulo. 
Em seguida, informe a qual candidato o voto foi destinado ou se foi nulo.
"""""

print(20 * '-')
C = int(input('[1] - A'
              '\n[2] - B'
              '\n[3] - C'
              '\n[0] - Nulo'
              '\n--------------------'
              '\nSeu voto: '))

if C not in range(0, 4):
    print('Escolha inválida!')

elif C in range(0, 4):
    if C == 1:
        print(f'Voto computado para o candidado: {C}')

    elif C == 2:
        print(f'Voto computado para o candidado: {C}')

    elif C == 3:
        print(f'Voto computado para o candidado: {C}')

    else:
        print('Você votou nulo!')
