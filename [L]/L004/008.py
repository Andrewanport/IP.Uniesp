"""""
Conversor de Decimal para Binário:
Contexto: Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária. 
Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.
"""""

# Aproveitei pra fazer umas outras bases já que já estou estudando para arquitetura mesmo kk.


def calculadora_bases():

    print(40 * '~~')
    print('                      CALCULADORA DE BASES DIFERENTES')
    print(40 * '~~')

    print(f'[1] | {"Decimal":<12} -> {"Binário":<12} | (\033[1;32m10\033[m) -> (\033[1;32m2\033[m)\n'
          f'[2] | {"Decimal":<12} -> {"Octal":<12} | (\033[1;32m10\033[m) -> (\033[1;32m8\033[m)\n'
          f'[3] | {"Decimal":<12} -> {"Hexadecimal":<12} | (\033[1;32m10\033[m) -> (\033[1;32m16\033[m)\n'
          f'[4] | {"Binário":<12} -> {"Decimal":<12} | (\033[1;32m2\033[m)  -> (\033[1;32m10\033[m)\n'
          f'[5] | {"Octal":<12} -> {"Decimal":<12} | (\033[1;32m8\033[m)  -> (\033[1;32m10\033[m)\n'
          f'[6] | {"Hexadecimal":<12} -> {"Decimal":<12} | (\033[1;32m16\033[m) -> (\033[1;32m10\033[m)')

    print(40 * '~~')

    C = int(input(f'Selecione uma opção de conversão: '))

    match C:
        case 1:
            decimal = int(input("Digite um número decimal: "))
            binario = bin(decimal)[2:]
            print(f'O número {decimal} em binário é: {binario}')

        case 2:
            decimal = int(input("Digite um número decimal: "))
            octal = oct(decimal)[2:]
            print(f'O número {decimal} em octal é: {octal}')

        case 3:
            decimal = int(input("Digite um número decimal: "))
            hexadecimal = hex(decimal)[2:]
            print(f'O número {decimal} em hexadecimal é: {hexadecimal}')

        case 4:
            binario = input("Digite um número binário: ")
            decimal = int(binario, 2)
            print(f'O número {binario} em decimal é: {decimal}')

        case 5:
            octal = input("Digite um número octal: ")
            decimal = int(octal, 8)
            print(f'O número {octal} em decimal é: {decimal}')

        case 6:
            hexadecimal = input("Digite um número hexadecimal: ")
            decimal = int(hexadecimal, 16)
            print(f'O número {hexadecimal} em decimal é: {decimal}')

        case _:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 6.")


if __name__ == "__main__":
    calculadora_bases()

