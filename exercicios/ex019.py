from random import choice
a1 = input("Diga o nome do aluno ")
a2 = input("Diga o nome do aluno ")
a3 = input("Diga o nome do aluno ")
a4 = input("Diga o nome do aluno ")

lista = [a1, a2, a3, a4]

escolha = choice(lista)
print(f'{escolha} irá apagar o quadro')

# escolha = choice(lista)
# if (escolha == a1):
#     print(f'{a1} apaga o quadro')
# if (escolha == a2):
#     print(f'{a2} apaga o quadro')
# if (escolha == a3):
#     print(f'{a3} apaga o quadro')
# if (escolha == a4):
#     print(f'{a4} apaga o quadro')
