algo = input('Digite algo')
print('Seu tipo primitivo é ', type(algo))
print('Ele é alfabético?', algo.isalpha())
print('Ele é numérico?', algo.isnumeric())
print('Ele é alfanumérico?', algo.isalnum())
print('É somente letras maiúsculas?', algo.isupper())
print('É somente letras minúsculas?', algo.islower())
print('Tem somente espaços?', algo.isspace())
print('Está capitalizada? (primeira maiuscula)', algo.istitle())
