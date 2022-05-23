from random import shuffle
a1 = input("Diga o nome do aluno ")
a2 = input("Diga o nome do aluno ")
a3 = input("Diga o nome do aluno ")
a4 = input("Diga o nome do aluno ")

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A orde de apresentação é \n {lista}')

# sorteio1 = random.choice(lista)
# lista.remove(sorteio1)
# sorteio2 = random.choice(lista)
# lista.remove(sorteio2)
# sorteio3 = random.choice(lista)
# lista.remove(sorteio3)
# sorteio4 = random.choice(lista)
# print('A orde da apresentações é a seguinte')
# print(sorteio1)
# print(sorteio2)
# print(sorteio3)
# print(sorteio4)
