"""""
Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de 
um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', 
senão escrever a mensagem 'Efetuar compra'.
"""""

QA = int(input('Digite a quantidade ATUAL em estoque: '))

QMAX = int(input('Digite a quantidade MÁXIMA em estoque: '))

QMIN = int(input('Digite a quantidade MÍNIMA em estoque: '))

QMED = (QMAX + QMIN)/2

if QA >= QMED:
    print('Não efetuar a compra!')

else:
    print('Efetuar a compra!')
