"""""
Escreva um programa que verifique se um número é maior, menor ou igual a 50.
"""""

N = float(input('Digite um número qualquer: '))

if N > 50:
    print(f'{N:.1f} > 50')

elif N < 50:
    print(f'{N:.1f} < 50')

else:
    print(f'{N:.1f} = 50')
