import random
import array as ar
a1 = 'cleber'
a2 = 'joao'
a3 = 'jose'
a4 = 'maria'

lista = [a1, a2, a3, a4]

sorteio1 = random.choice(lista)
lista.remove(sorteio1)
sorteio2 = random.choice(lista)
lista.remove(sorteio2)
sorteio3 = random.choice(lista)
lista.remove(sorteio3)
sorteio4 = random.choice(lista)
print('A orde da apresentações é a seguinte')
print(sorteio1)
print(sorteio2)
print(sorteio3)
print(sorteio4)