"""""
Classificação de Plantas Mágicas
a. Descrição: Um botânico está classificando plantas mágicas em uma floresta. Ele quer saber se
uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros), ou grande (mais de 3
metros). Crie um programa que receba a altura da planta e informe a sua classificação.
b. Conceito: Operadores relacionais, desvio condicional aninhado.
"""""

def L003Q007(A):
    if A < 1:
        print("A planta é pequena.")
    elif 1 <= A <= 3:
        print("A planta é média.")
    else:
        print("A planta é grande.")


if __name__ == '__main__':
    T = float(input("Digite a altura da planta (em metros): "))

    L003Q007(T)
