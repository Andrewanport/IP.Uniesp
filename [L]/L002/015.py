"""""
Contexto: Controle de velocidade. 
Questão: Peça ao usuário para inserir a velocidade atual de um carro. 
Informe se ele está abaixo do limite (80 km/h), ou se ele deverá ser multado (acima de 80 km/h). 
Se ele for multado, informe que a multa será de R$5,00 por km acima do limite.
"""""

V = float(input('Velocidade atual do veículo: '))
L = 80
M = (V - L) * 5

if V <= L:
    print('\033[1;34mDentro do limite de velocidade.\033[0m')

else:
    print('Fora do limite de velocidade.')
    print(f'Valor da multa: \033[1;31mR${M}\033[0m')

