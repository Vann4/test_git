import math
print('')
print('Найдем дискриминант\n')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

D = b**2 - 4*a*c

if D > 0:
    x1 = ((-b+math.sqrt(D)) / (2*a))
    x2 = ((-b-math.sqrt(D)) / (2*a))
