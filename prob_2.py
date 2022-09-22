# 2 Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

num = int(input('Введите нартуральное число:'))
list1= []
count = 2
while num > 1:
    if num % count == 0:
        list1.append(count)
        num = num/count
    else:
        count += 1
print(list1)