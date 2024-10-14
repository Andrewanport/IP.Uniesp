"""""
Contador de Vogais e Consoantes:
Contexto: Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela.
Utilize um loop para percorrer cada caractere da frase e realizar a contagem.
"""""


def contar_vogais_consoantes():
    F = input('Digite uma frase: ').lower()
    V = 'aeiou'
    Vcount = 0
    Ccount = 0

    for L in F:
        if L in V:
            Vcount += 1
        else:
            Ccount += 1

    print(f'Número de vogais: \033[1;32m{Vcount}\033[m')
    print(f'Número de consoantes: \033[1;31m{Ccount}\033[m')


if __name__ == '__main__':
    contar_vogais_consoantes()



