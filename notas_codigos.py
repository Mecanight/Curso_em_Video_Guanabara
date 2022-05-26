# print('Ola, Mundo!')
# print(7+4)
# print('7'+'4')
# 7+4
# '7'+'4'
# print('Ola', 5)
# nome = 'Guanabara'
# idade = 25
# peso = 75.8
# print(nome, idade, peso)
# nome = input('Qual é o seu nome?')
# idade = input('Quantos anos você tem?')
# peso = input('Qual é o seu peso')
# print(nome, idade, peso)

# nome = input('Qual é o seu nome?')
# print('Seja bem Vindo', nome)

# dia = input('Que dia você nasceu?')
# mes = input('Que mês você nasceu?')
# ano = input('Que ano você nasceu?')
# print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

# numero_1 = int(input('Informe um número'))
# numero_2 = int(input('Informe outro número'))
# soma = numero_1 + numero_2
# print('A soma dos dois números é:', soma)
# print(f'A soma entre {numero_1} e {numero_2} é {soma}')
#
# n = input('Digite algo')
# print(type(n))
# print(n)
# print(n.isnumeric())
# print(n.isalpha())
# print(n.upper())


#AULA 07

# print('19+2 =',19+2)
# print('19-2 =',19-2)
# print('19*2 =',19*2)
# print('19/2 =',19/2)
# print('19**2 =',19**2)
# print('19//2 =',19//2)
# print('19%2 =',19%2)
#
# nome = input('Qual é seu nome')
# print('Prazer em te conhecer {nome:20}!')
# print('Prazer em te conhecer {nome:>20}!')
# print('Prazer em te conhecer {nome:<20}!')
# print('Prazer em te conhecer {nome:^20}!')

# n1 = int(input('Um valor: '))
# n2 = int(input('Outro valor'))
# soma = n1+n2
# subt = n1-n2
# mult = n1*n2
# divi = n1/n2
# divint = n1//n2
# poten = n1**n2
#
#
# print(f'A soma é {soma}, a subtração é {subt}, o produto é {mult}, a divisão é {divi:.2f},', end = " ")
# print(f'a divisão inteira é {divint} e a potencia é {poten}')


#Aula 08

# import math
# num = int(input('Digite um numero'))
# raiz = math.sqrt(num)
# print(f'A raiz de {num} é igual a {raiz:.2f}')

# from math import sqrt, floor
# num = int(input('Digite um numero'))
# raiz = sqrt(num)
# print(f'A raiz de {num} é igual a {floor(raiz):.2f}')

# import random
# num = random.random()
# print(num)

# import random
# num = random.randint(1, 10)
# print(num)

# AULA 09

# print("""Formações com conteúdo do mercado de trabalho:
# sequências de cursos e conteúdo para você se capacitar
# em tecnologia e negócios digitais.
# São 1338 cursos e novos lançamentos toda semana, além
# de atualizações e melhorias constantes.
# Garantimos conhecimento com profundidade e diversidade,
# para se tornar um profissional em T!
# Faça parte de uma comunidade de apaixonados por tudo que
# é digital. Mergulhe na comunidade Alura.""")

frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
alterar = frase.replace('Python', 'Android')
print(alterar)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
frase_split = frase.split()
print(frase_split)
print(frase_split[0])
print(frase_split[0][3])
frase_join = '-'.join(frase_split)
print(frase_join)
