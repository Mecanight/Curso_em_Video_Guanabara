import math
catopo = float(input('Diga o cateto oposto'))
catadj = float(input('Diga o cateto adjacente'))

hipo = math.hypot(catopo, catadj)
print(f'A hipotenusa é {hipo}')

