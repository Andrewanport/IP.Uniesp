"""""
Calculadora de Bônus
a. Descrição: Um rei deseja distribuir bônus aos seus cavaleiros com base em suas conquistas. Se
um cavaleiro completou mais de 10 missões, ele recebe um bônus de 100 moedas de ouro. Se
completou entre 5 e 10 missões, recebe 50 moedas de ouro. Se completou menos de 5, recebe
10 moedas de ouro. Crie um programa que receba o número de missões completadas e
informe o valor do bônus.
b. Conceito: Desvio condicional aninhado, operadores relacionais.
"""""

def L003Q008(M):

    if M > 10:
        print("O cavaleiro receberá 100 moedas de ouro.")
    elif 5 <= M <= 10:
        print("O cavaleiro receberá 50 moedas de ouro.")
    else:
        print("O cavaleiro receberá 10 moedas de ouro.")


if __name__ == '__main__':
    M = int(input("Digite o número de missões completadas: "))

    L003Q008(M)
