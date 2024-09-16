"""""
Contexto: Cálculo de imposto. 
Questão: Peça ao usuário para inserir seu salário mensal. 
Calcule o imposto de renda com base no seguinte: até R$2000, isento; de R$2000,01 até R$3500, 10%; acima de R$3500, 15%.
"""""

R = float(input('Digite o valor do seu rendimento mensal: '))

if R <= 2000:
    print('Insento de impostos!')

elif 2000.01 <= R <= 3500:
    print('Imposto de 10% em relação ao valor de rendimento mensal.')
    print(f'Valor de imposto: {R * 0.10}')

else:
    print('Imposto de 15% em relação ao valor de rendimento mensal.')
    print(f'Valor de imposto: {R * 0.15}')
