"""""
Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', 
senão escrever a mensagem 'Saldo Negativo'.
"""""

N = int(input('Número da conta: '))
S = float(input('Saldo: '))
D = float(input('Débito: '))
C = float(input('Credito: '))

SA = S - D + C

if SA >= 0:
    print(f'Saldo Positivo! Saldo atual: R${SA}')

else:
    print(f'Saldo Negativo! Saldo atual: R${SA}')