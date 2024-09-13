"""""
Crie uma constante chamada PI com valor 3.14 e peça ao usuário o raio de um círculo. Em seguida, calcule o perímetro do círculo.
"""""

# C = 2 * 3.14 * r

R = float(input('Digite o raio do círculo (cm): '))

C = 2 * 3.14 * R

print(f'A circunferência do círculo de raio {R:.2f}cm será de: {C:.2f}cm')
