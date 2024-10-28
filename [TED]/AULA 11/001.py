"""""
Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
números repetidos no vetor VET e em que posições se encontram.
"""""

VET = []

for i in range(10):
    num = int(input(f"Digite o número [{i + 1}]: "))
    VET.append(num)

R = {}              # Números repetidos

for i in range(len(VET)):
    if VET.count(VET[i]) > 1:
        if VET[i] not in R:
            R[VET[i]] = []
        R[VET[i]].append(i)

if R:
    print("Números repetidos e suas posições:")

    for num, P in R.items():                        # P = Posições
        print(f"Número {num} nas posições {P}")

else:
    print("Não há números repetidos no vetor.")
