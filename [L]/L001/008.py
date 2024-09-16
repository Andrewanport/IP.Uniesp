"""""
Peça ao usuário para inserir seu nome e idade e, em seguida, imprima uma mensagem informando quantos anos ele terá em 2025.
"""""

from datetime import date

I = int(input('Digite a sua idade: '))

A = I + (2025 - date.today().year)

print(f"Sua idade em 2025 será: {A}")
