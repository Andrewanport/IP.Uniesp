"""""
Contexto: Sistema de senhas. 
Questão: Peça ao usuário para inserir uma senha. 
Se a senha for "Python123", imprima "Acesso concedido". 
Caso contrário, imprima "Acesso negado".
"""""

S = input('Digite a senha: ')

if S == "Python123":
    print("\033[1;32mAcesso concedido.\033[0m")

else:
    print('\033[1;31mAcesso negado!\033[0m')