"""""
Calculadora de Média de Notas:
Contexto: Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. 
Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada 
(por exemplo, -1).
"""""


def calcular_media():
    notas = []

    while True:

        nota = float(input('Digite a nota (ou -1 para encerrar): '))
        if nota == -1:
            break

        notas.append(nota)

    if notas:
        media = sum(notas) / len(notas)
        print(f'A média das notas é: \033[1;34m{media:.2f}\033[m')
    else:
        print('Nenhuma nota foi inserida.')


if __name__ == '__main__':
    calcular_media()
