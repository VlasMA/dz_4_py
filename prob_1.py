# Вычислить число c заданной точностью d

import math
from tokenize import Double

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
point = float(input('С какой точностью вы хотите найти число(пример: 0.001):'))
count = 0

while point != 1:
    count = count + 1
    point = point * 10
print(count)

ansver = round(number_1 / number_2, int(count))
print(ansver)

point_2 = int(input('с какой точностью найти "Пи": '))
print(round(math.pi, point_2))