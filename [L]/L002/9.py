"""""
Contexto: Avaliação de desempenho de um funcionário. 
Questão: Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou. 
Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00". 
Caso contrário, imprima "Sem bônus".
"""""

E = int(input('Digite o numero de horas extras: '))
F = int(input('Digite o numero de horas faltadas: '))

if E >= (F * 1.5):
    print('Bônus de R$500')

else:
    print('Sem bônus')
