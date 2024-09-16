"""""
Contexto: Condições climáticas. 
Questão: Peça ao usuário para inserir a temperatura atual e informe se: 
está frio (< 15°C), ameno (entre 15°C e 25°C) ou quente (> 25°C).
"""""

T = float(input('Digite a temperatura atual: '))

if T < 15:
    print('Está frio')

elif T > 25:
    print('Está quente')

else:
    print('Está ameno')
