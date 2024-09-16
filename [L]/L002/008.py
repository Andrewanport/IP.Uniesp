"""""
Contexto: Um programa de descontos em uma loja. 
Questão: Escreva um programa que dê descontos de acordo com o valor da compra: 
acima de R$100, desconto de 10%; entre R$50 e R$100, desconto de 5%; abaixo de R$50, sem desconto. 
Calcule e mostre o valor do desconto e o valor total a pagar.
"""""

V = float(input('Digite o valor da compra: R$'))

if V > 100:
    D = V * 0.10
    T = V - D
elif 50 <= V <= 100:
    D = V * 0.05
    T = V - D
else:
    D = 0
    T = V

print(f'Valor base do produto: R${V:.2f}')
print(f'Valor do desconto do produto: R${D:.2f}')
print(f'Valor final do produto: R${T:.2f}')

