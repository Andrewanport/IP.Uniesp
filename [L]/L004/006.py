"""""
Verificador de Número Primo:
Contexto: Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo. 
Utilize um loop para testar a divisibilidade do número por outros números menores.
"""""


def numero_primo():
    N = int(input('Digite um número: '))
    if N < 2:
        print(f'{N} não é primo.')
        return

    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            print(f'{N} não é primo.')
            return

    print(f'{N} é primo.')


if __name__ == '__main__':
    numero_primo()

