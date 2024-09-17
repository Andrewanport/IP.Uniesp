"""""
Adivinhação de Animais
a. Descrição: Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil. Se for
mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir
que é uma tartaruga.
b. Conceito: Desvio condicional composto, variáveis.
"""""

A = input("Seu animal favorito é um mamífero ou réptil? ").lower().i

if A == "mamífero":
    print("Seu animal favorito é provavelmente um cachorro.")
elif A == "réptil":
    print("Seu animal favorito é provavelmente uma tartaruga.")
else:
    print("Animal desconhecido.")
