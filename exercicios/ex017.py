from math import hypot
catopo = float(input('Diga o cateto oposto'))
catadj = float(input('Diga o cateto adjacente'))

# hipo = ((catopo**2) + (catadj**2))** (1/2)

hipo = hypot(catopo, catadj)
print(f'A hipotenusa é {hipo:.2f}')
