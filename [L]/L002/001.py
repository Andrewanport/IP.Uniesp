"""""
Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga 
se o aluno foi ou não aprovado (considerar que nota igual ou maior a 6 o aluno é aprovado). 
Escrever também o resultado da média calculada.
"""""

N1 = float(input('Digite a 1ª Nota: '))
N2 = float(input('Digite a 2ª Nota: '))

M = (N1 + N2) / 2

if M >= 6:
    print(f'Aluno aprovado! Média: {M:.2f}')

else:
    print(f'Aluno Reprovado! Média: {M:.2f}')


