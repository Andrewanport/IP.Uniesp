"""""
Contexto: Cinema. 
Questão: Escreva um programa que pergunta ao usuário sua idade e informa o valor do ingresso do cinema: 
abaixo de 12 anos e acima de 60, R$ 15.00; entre 12 e 60 anos, R$ 25.00.
"""""

I = int(input('Digite a sua idade: '))

if I < 12 or I > 60:
    print('R$15.00')

elif 12 <= I <= 60:
    print('R$25.00')


