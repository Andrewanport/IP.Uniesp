"""""
Solicite ao usuário um valor numérico, inteiro ou real (float), e verifique se ele é maior ou menor que 10. 
O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.
"""""

N = float(input('Digite um número qualquer: '))

if N > 10:
    print(f'{N:.1f} > 10')

elif N < 10:
    print(f'{N:.1f} < 10')

else:
    print(f'{N:.1f} = 10')
