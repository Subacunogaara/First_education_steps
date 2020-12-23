# вывести максимальное числовое логическое значение из последовательности

# Вариант1 (с двумя отдельными массивами)
# a = [1, 2, 3, 100, '1000', 'Alex']
# b = []
# c = []
# for f in a:
#     if type(f) == int:
#         b.append(f)
#     else:
#         if type(f) == str and f.isdigit():
#             c.append(int(f))
# if max(b)>max(c):
#     print(max(b))
# else:
#     print(max(c))

# Вариант2 (всё в один массив)
# a = [1, 2, 3, 100, '1000', 'Alex']
# b = []
# for f in a:
#     if type(f) == int:
#         b.append(f)
#     else:
#         if type(f) == str and f.isdigit():
#             b.append(int(f))
# print(max(b))


# Заполнить массив заданной длины различными простыми числами.
# Натуральное число, большее единицы, называется простым,
# если оно делится только на себя и на единицу.

# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     test = []
#     for f in range(2, 100000000):
#         for i in range(2, f+1):
#             if f % i == 0:
#                 test.append(f)
#         if len(test) == 1:
#             my_list.append(f)
#             test.clear()
#         else:
#             test.clear()
#         if len(my_list) == long:
#             break
#     print(my_list)


# Создать массив, каждый элемент которого равен квадрату своего номера

# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     for f in range(1, long+1):
#         my_list.append(f*f)
#     print(my_list)


# Создать массив, на четных местах в котором стоят единицы,
# а на нечетных местах - числа, равные остатку от деления своего номера на 5

# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     if (long % 2) != 0 and long > 1:
#         for f in range(1, long+1, 2):
#             my_list.extend([(f % 5), 1])
#         my_list.pop()
#         print(my_list)
#     elif long == 1:
#         my_list.append(1 % 5)
#         print(my_list)
#     else:
#         for f in range(1, long+1, 2):
#             my_list.extend([(f % 5), 1])
#         print(my_list)


# Создать массив, состоящий из троек подряд идущих одинаковых элементов

# while 1:
#     my_list = []
#     seq = list(input('Введите последовательность: '))
#     test = []
#     for f in seq:
#         if f.isdigit():
#             test.append(int(f))
#         else:
#             test.append(f)
#     for i in test:
#         my_list.extend([i, i, i])
#     print(my_list)


# Создать массив, который одинаково читается как слева направо,
# так и справа налево

# while 1:
#     my_list = list(input('Введите последовательность: '))
#     test = my_list.copy()
#     test.reverse()
#     my_list.extend(test)
#     print(my_list)


# Сформировать массив из случайных чисел, в которых ровно две единицы,
# стоящие на случайных позициях

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     large = int(input('Введите максимально возможное число: '))
#     a = 2
#     for f in range(2, long):
#         my_list.append(random.randint(0, large))
#     while a:
#         my_list.insert(random.randint(0, long + 1), 1)
#         a = a - 1
#     print(my_list)


# Заполните массив случайным образом нулями и единицами так,
# чтобы количество единиц было больше количества нулей

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     long1 = long
#     if (long % 2) == 0:
#         my_list.insert(random.randint(0, long1 - 1), 1)
#         long -= 1
#         while long:
#             my_list.insert(random.randint(0, long1 - 1), 1)
#             long -= 1
#             if long == 0:
#                 break
#             else:
#                 my_list.insert(random.randint(0, long1 - 1), 0)
#                 long -= 1
#     else:
#         while long:
#             my_list.insert(random.randint(0, long1 - 1), 1)
#             long -= 1
#             if long == 0:
#                 break
#             else:
#                 my_list.insert(random.randint(0, long1 - 1), 0)
#                 long -= 1
#     print(my_list)


# Сформировать массив из случайных целых чисел от 0 до 9 ,
# в котором единиц от 3 до 5 и двоек больше троек

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива больше 6: '))
#     a = long
#     while long:
#         if a > 6:
#             my_list.append(random.randint(0, 9))
#             long -= 1
#             if long != 0:
#                 if 3 <= my_list.count(1) <= 5 and my_list.count(2) > my_list.count(3):
#                     my_list.append(random.randint(0, 9))
#                     long -= 1
#                 elif 3 <= my_list.count(1) <= 5:
#                     if my_list.count(3) >= my_list.count(2):
#                         my_list.insert(random.randint(0, a), 2)
#                     else:
#                         my_list.insert(random.randint(0, a), 3)
#                     long -= 1
#                 else:
#                     my_list.insert(random.randint(0, a), 1)
#                     long -= 1
#             else:
#                 break
#         else:
#             print('Введёная длина меньше 6!!!')
#     print(my_list)


# Создайте массив, в котором количество отрицательных чисел
# равно количеству положительных и положительные числа расположены
# на случайных местах в массиве

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива(чётное число): '))
#     a = long
#     if (long % 2) == 0:
#         while long:
#             my_list.insert(random.randint(0, a), random.randint(-1000, 0))
#             my_list.insert(random.randint(0, a), random.randint(0, 1000))
#             long -= 2
#         print(my_list)
#     else:
#         print('Вы ввели нечётное число!!!')


# Заполните массив случайным образом нулями, единицами и двойками так,
# чтобы первая двойка в массиве встречалась раньше первой единицы,
# количество единиц было в точности равно суммарному количеству нулей и двоек

# import random
#
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива(чётное число): '))
#     if (long % 2) == 0:
#         while long:
#             my_list.append(random.randint(0, 2))
#             long -= 1
#             if my_list.count(1) > 0 and my_list.count(2) > 0:
#                 if my_list.index(1) < my_list.index(2):
#                     my_list.remove(1)
#                     long += 1
#             if my_list.count(1) != (my_list.count(0) + my_list.count(2)):
#                 if my_list.count(1) < (my_list.count(0) + my_list.count(2)):
#                     my_list.pop(0)
#                     my_list.append(1)
#                 elif my_list.count(1) > (my_list.count(0) + my_list.count(2)) and my_list.count(1) > 0:
#                     my_list.remove(1)
#                     long += 1
#         print(my_list)
#     else:
#         print('Вы ввели нечётное число!!!')


# Придумайте правило генерации массива заданной длины.
# Определите, сгенерирован ли данный массив вашим правилом или нет

# import random
# while 1:
#     print('Сгенерированный массив должен состоять из трёхзначных чисел\n'
#           'каждый последующий член массива должен иметь противоположный знак( + или -)')
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     my_list.append(random.randint(-999, 999))
#     long -= 1
#     while long:
#         if len(my_list) != 0:
#             if -100 < my_list[len(my_list) - 1] < 100:
#                 my_list.remove(my_list[len(my_list) - 1])
#                 long += 1
#             else:
#                 if long != 0 and my_list[len(my_list) - 1] > 0:
#                     my_list. append(random.randint(-999, -100))
#                     long -= 1
#                 elif long != 0 and my_list[len(my_list) - 1] < 0:
#                     my_list. append(random.randint(100, 999))
#                     long -= 1
#                 else:
#                     break
#         elif len(my_list) == 0:
#             my_list.append(random.randint(-999, -999))
#             long -=1
#         else:
#             break
#     print(my_list)
# блок проверки массива
#     check = len(my_list)
#     while check:
#         if (-1000 < my_list[-check] < -99) or (1000 > my_list[-check] > 99):
#             if check > 1:
#                 if ((my_list[-check] > 0) and (my_list[-check + 1] < 0)) or ((my_list[-check] < 0)
#                                                                              and (my_list[-check + 1] > 0)):
#                     check -= 1
#                 else:
#                     print('Последовательность не соблюдается!!!')
#             elif check == 1:
#                 if ((my_list[-check] > 0) and (my_list[-check - 1] < 0)) or ((my_list[-check] < 0)
#                                                                              and (my_list[-check - 1] > 0)):
#                     check -= 1
#                 else:
#                     print('Последовательность не соблюдается!!!')
#         else:
#             print('Массив содержит не трёхзначное число!!!')
#     print('Проверка окончена')


# Определить, содержит ли массив данное число x

# while 1:
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     x = int(input('Введите число которое может содержать массив: '))
#     count = 0
#     for f in my_list:
#         if f == x:
#             print('Такое число присутствует в массиве!!!')
#         elif f != x:
#             count += 1
#         if count == len(my_list):
#             print('Такого числа в массиве нет!!!')


# Найти количество четных чисел в массиве

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for f in my_list:
#     if (f % 2) == 0:
#         count += 1
# print('В массиве ' + str(count) + ' чётных чисел')
