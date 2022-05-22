import random
a1 = input("Diga o nome do aluno")
a2 = input("Diga o nome do aluno")
a3 = input("Diga o nome do aluno")
a4 = input("Diga o nome do aluno")

apaga = random.randint(1, 4)
print(apaga)
if (apaga == 1):
    print(f'{a1} apaga o quadro')
if (apaga == 2):
    print(f'{a2} apaga o quadro')
if (apaga == 3):
    print(f'{a3} apaga o quadro')
if (apaga == 4):
    print(f'{a4} apaga o quadro')