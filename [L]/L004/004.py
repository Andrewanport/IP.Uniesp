"""""
Jogo de Adivinhação:
Contexto: Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. 
Utilize um loop para permitir que o usuário faça várias tentativas, fornecendo dicas (maior ou menor) a cada tentativa.
"""""

import random


def jogo_adivinhacao():
    A = random.randint(1, 100)
    T = 0

    while True:
        U = int(input('Tente adivinhar o número (entre 1 e 100): '))
        T += 1

        if U < A:
            print("Mais alto!")
        elif U > A:
            print("Mais baixo!")
        else:
            if T == 1:
                print(f'Tá de hack! Você precisou de \033[1;34m{T}\033[m tentativas.')

            elif 1 < T < 10:
                print(f'Jogou muito! Você precisou de \033[1;34m{T}\033[m tentativas.')

            else:
                print(f'Finalmente! Você precisou de \033[1;34m{T}\033[m tentativas.')
            break


if __name__ == "__main__":
    jogo_adivinhacao()
