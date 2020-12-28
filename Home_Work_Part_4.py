# Remastered 17
# Заполните массив случайным образом нулями, единицами и двойками так,
# чтобы первая двойка в массиве встречалась раньше первой единицы,
# количество единиц было в точности равно суммарному количеству нулей и двоек

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива(чётное число): '))
#     while long:
#         my_list.append(random.randint(0, 2))
#         long -= 1
#         if (my_list.count(1) > 0) and (my_list.count(2) > 0):
#             if my_list.index(1) < my_list.index(2):
#                 my_list.remove(1)
#                 long += 1
#         if (my_list.count(1) > 0) and ((my_list.count(2) + my_list.count(0)) > 0):
#                 if my_list.count(1) > (my_list.count(2) + my_list.count(0)):
#                     my_list.remove(1)
#                     long += 1
#                 elif my_list.count(1) < (my_list.count(2) + my_list.count(0)):
#                     my_list.pop(0)
#                     my_list.append(1)
#                     if (my_list.count(1) > 0) and (my_list.count(2) > 0):
#                         if my_list.index(1) < my_list.index(2):
#                             my_list.remove(1)
#                             long += 1
#     print(my_list)


# Найти количество чисел в массиве, которые делятся на 3,
# но не делятся на 7

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     count = 0
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -=1
#     print('Получен случайный массив:\n', my_list)
#     for f in my_list:
#         if (f % 3 == 0) and (f % 7 != 0):
#             count +=1
#     print('Количество искомых чисел:\n ', count)


# Определите, каких чисел в массиве больше: которые делятся на первый
# элемент массива или которые делятся на последний элемент массива.

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 10))
#         long -=1
#     print('Ваш массив\n', my_list)
#
#     def counts(massive, first, last):
#         count1st = 0
#         countLst = 0
#         for f in massive:
#             if f % first == 0:
#                 count1st += 1
#             if f % last == 0:
#                 countLst += 1
#         # res = (count1st, countLst)
#         # return res
#         if count1st > countLst:
#             print('Чисел которые делятся на первый элемент\n'
#                   'массива больше')
#         elif countLst > count1st:
#             print('Чисел которые делятся на последний элемент\n'
#                   'массива больше')
#         elif count1st == countLst and count1st > 0:
#             print('Чисел которые делятся на первый элемент\n'
#                   'и чисел которые делятся на последний элемент\n'
#                   'массива одинаковое количество')
#     counts(my_list, my_list[0], my_list[len(my_list) - 1])


# Найдите сумму и произведение элементов массива.

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     summa = 0
#     pro = 1
#     while long:
#         my_list.append(random.randint(1, 100))
#         long -=1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         summa += f
#         pro = pro * f
#     print('Сумма элементов массива\n', summa)
#     print('Произведение элментов массива\n', pro)


# Найдите сумму четных чисел массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     summa = 0
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -=1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         if f % 2 == 0:
#             summa = summa + f
#     print('Сумма чётных чисел массива:\n', summa)


# Найдите сумму нечетных чисел массива, которые не превосходят 11

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     summa = 0
#     while long:
#         my_list.append(random.randint(0, 25))
#         long -=1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         if (f % 2 != 0) and f <= 11:
#             summa = summa + f
#     print('Сумму нечетных чисел массива, которые не превосходят 11:\n', summa)


# Найдите сумму чисел массива, которые расположены до первого четного числа массива.
# Если четных чисел в массиве нет, то найти сумму всех чисел за исключением крайних

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     summa = 0
#     another_summa = 0
#     count = 0
#     while long:
#         my_list.append(random.randint(1, 100))
#         long -=1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         if f % 2 != 0:
#             summa += f
#             count += 1
#         else:
#             break
#     if count == len(my_list):
#         summa = sum(my_list) - my_list[0] - my_list[-1]
#         print('Чётных чисел в массиве нет\n', 'Сумма чисел за исключением крайних: ', summa)
#     elif summa > 0:
#         print('Сумма чисел: ', summa)
#     else:
#         print('Первое число массива четное')


# Найдите сумму чисел массива, которые стоят на четных местах

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     summa = 0
#     while long:
#         my_list.append(random.randint(1, 100))
#         long -=1
#     print('Ваш массив\n', my_list)
#     for f in my_list[1::2]:
#         summa += f
#     print('Сумма чисел массива, которые стоят на четных местах\n', summa)


# Найдите сумму чисел массива, которые стоят на нечетных местах
# и при этом превосходят сумму крайних элементов массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     summa = 0
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list[0::2]:
#         if (my_list[0] + my_list[-1]) < f:
#             summa += f
#     print('Искомая сумма: ', summa)


# Дан массив x из n элементов. Найдите x1−x2+x3−…−xn−1+xn

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива x(n элементов): '))
#     itog1 = 0
#     itog2 = 0
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         itog1 = sum(my_list[0::2])
#         itog2 = sum(my_list[1::2])
#         f = itog1 - itog2
#     print('Результат: ', f)


# Дан массив x из n элементов. Найдите x1xn+x2xn−1+…+xnx1

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива x(n элементов): '))
#     summa = 0
#     count = -1
#     while long:
#         my_list.append(random.randint(1, 10))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         summa += f * my_list[count]
#         count -= 1
#     print('Результат:\n', summa)


# Дан массив x из n элементов. Найдите xn(xn+xn−1)(xn+xn−1+xn−2)…(xn+…+x1)

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива x(n элементов): '))
#     count = -2
#     while long:
#         my_list.append(random.randint(1, 3))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     pro = my_list[-1]
#     for f in my_list[:-1]:
#         pro *= sum(my_list[count:])
#         count -= 1
#     print('Результат:\n', pro)


# Найти наибольший элемент массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(-99, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     bol = max(my_list)
#     print('Наибольший элемент массива:\n', bol, '\nИмеет порядковый номер:\n',
#           (my_list.index(bol) + 1))


# Найдите сумму наибольшего и наименьшего элементов массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(-99, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     bol = max(my_list)
#     men = min(my_list)
#     summa = int(bol) + int(men)
#     print('Сумма наибольшего: ', bol, ' и наименьшего: ', men,  '\nэлементов массива:\n', summa)


# Найдите количество элементов массива,
# которые отличны от наибольшего элемента не более чем на 10%

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     count = 0
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         if f/max(my_list) >= 0.9:
#             count +=1
#     print('Количество искомых элементов:\n', count)


# Найдите наименьший четный элемент массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     while len(my_list) > 0:
#         if min(my_list) % 2 == 0:
#             print('Наименьший чётный элемент массива:\n', min(my_list))
#             break
#         else:
#             my_list.remove(min(my_list))


# Среди элементов с нечетными номерами
# найдите наибольший элемент массива, который делится на 3

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     new = []
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list[::2]:
#         if f % 3 == 0:
#             new.append(f)
#     if len(new) > 0:
#         print('Наибольший элемент массива кратный 3:\n', max(new))
#     else:
#         print('В массиве нет элементов удовлетворяющих условиям поиска')


# Дан массив и число p. Найдите два различных числа в массиве,
# сумма которых наиболее близка к p

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     new_dict = {}
#     new_dict2 = {}
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     p = int(input('Введите число р:'))
#     while len(my_list) > 0:
#         for f in my_list[1:]:
#             new_dict[f + my_list[0]] = "{0} и {1}".format(my_list[0], f)
#         my_list.pop(0)
#     for i in new_dict.keys():
#         new_dict2[round(abs(i/p - 1), 2)] = i
#     print('Сумма ', new_dict[new_dict2[min(new_dict2.keys())]], 'наиболее близка к ', p)


# Дан массив. Найдите два соседних элемента, сумма которых минимальна

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     new_dict = {}
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     while len(my_list) > 1:
#             new_dict[my_list[0] + my_list[1]] = "{0} и {1}".format(my_list[0], my_list[1])
#             my_list.pop(0)
#     print('Минимальная сумма у элементов: ', new_dict[min(new_dict.keys())])


# Дан массив. Найдите три последовательных элемента в массиве,
# сумма которых максимальна

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     new_dict = {}
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     while len(my_list) > 2:
#         new_dict[my_list[0] + my_list[1] + my_list[2]] = \
#             "{0} и {1} и {2}".format(my_list[0], my_list[1], my_list[2])
#         my_list.pop(0)
#     print('Максимальная сумма у элементов: ', new_dict[max(new_dict.keys())])


# В данном массиве найдите количество чисел,
# соседи у которых отличаются более чем в 2 раза

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     count = 0
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     while len(my_list) > 2:
#         if my_list[0]/my_list[2] >= 2 or my_list[2]/my_list[0] >=2:
#             count += 1
#             my_list.pop(0)
#         else:
#             my_list.pop(0)
#     print('Количество чисел, соседи у которых отличаются более чем в 2 раза:\n', count)


# Найдите количество чисел,
# каждое из которых равно сумме квадратов своих соседей
# и при этом не является наибольшим в массиве

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     count = 0
#     while long:
#         my_list.append(random.randint(0, 10))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     my_list1 = my_list.copy()
#     while len(my_list) > 2:
#         if (my_list[0]**2 + my_list[2]**2) == my_list[1] and my_list[1] != max(my_list1):
#             count += 1
#             my_list.pop(0)
#         else:
#             my_list.pop(0)
#     print('Количество искомых чисел:\n', count)


# Проверьте, содержит ли данный массив из n чисел, все числа от 1 до n

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива n чисел: '))
#     long_copy = long
#     count = 0
#     new_list = []
#     while long:
#         my_list.append(random.randint(1, long_copy))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in range(1, long_copy + 1):
#         if f in my_list:
#             count += 1
#         else:
#             new_list.append(f)
#     if count == long_copy:
#         print('В массиве есть все числа от 1 до ', long_copy)
#     else:
#         print('В массиве нет чисел:\n', new_list)


# Проверьте, образует ли элементы массива в данном порядке
# арифметическую или геометрическую прогрессии

# my_list = [1,2,3,4,5]
# new_list = [1,2,4,8,16]
# # проверка арифметической прогрессии
# my_list_copy = my_list.copy()
# while len(my_list_copy) > 2:
#     if my_list_copy[2] - my_list_copy[1] == my_list_copy[1] - my_list_copy[0]:
#         my_list_copy.pop(0)
#         if len(my_list_copy) == 2:
#             print('Элементы массива образуют арифметическую прогрессию')
#             break
#     else:
#         print('Арифметическая прогрессия не образована')
#         break
# # проверка геометрической прогрессии
# new_list_copy = new_list.copy()
# while len(new_list_copy) > 2:
#     if new_list_copy[2] / new_list_copy[1] == new_list_copy[1] / new_list_copy[0]:
#         new_list_copy.pop(0)
#         if len(new_list_copy) == 2:
#             print('Элементы массива образуют геометрическую прогрессию')
#             break
#     else:
#         print('Геометрическая прогрессия не образована')
#         break


# Проверьте, является ли данный массив возрастающим или убывающим

# my_list = [9,9,8,7,6,5,4,3,2,2,2,1,1]
# trig = len(my_list)
# count = 1
# for f in my_list[:-1]:
#     if f <= my_list[my_list.index(f) + 1]:
#         count += 1
#     else:
#         break
# if count == trig:
#     print('Массив возрастающий')
# else:
#     count = 1
#     for i in my_list[:-1]:
#         if i >= my_list[my_list.index(i) + 1]:
#             count += 1
#         else:
#             break
#     if count == trig:
#         print('Массив убывающий')
#     else:
#         print('Массив не является возрастающим или убывающим')


# Найдите количество различных элементов данного массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     new_list = []
#     while long:
#         my_list.append(random.randint(0, 8))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         if f not in new_list:
#             new_list.append(f)
#     print('Количество различных элементов:\n', len(new_list))


# Определите количество перемен знаков элементов массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     count = 0
#     while long:
#         my_list.append(random.randint(-10, 10))
#         long -= 1
#         if 0 in my_list:
#             my_list.remove(0)
#             long += 1
#     print('Ваш массив\n', my_list)
#     while len(my_list) > 1:
#         if (my_list[0] > 0 and my_list[1] > 0) or (my_list[0] < 0 and my_list[1] < 0):
#             my_list.pop(0)
#         else:
#             count += 1
#             my_list.pop(0)
#     print('Количесвто перемен знаков:\n', count)


# В данном массиве найти максимальное количество одинаковых элементов

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     count_list = []
#     while long:
#         my_list.append(random.randint(0, 5))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         count_list.append(my_list.count(f))
#     print('Максимальное количество одинаковых элементов:\n', max(count_list))


# Найти наиболее часто встречающийся элемент в массиве целых чисел

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     value_list = []
#     count_list = []
#     while long:
#         my_list.append(random.randint(0, 5))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     for f in my_list:
#         if f not in value_list:
#             value_list.append(f)
#             count_list.append(my_list.count(f))
#     if count_list.count(max(count_list)) == 1:
#         print('Наиболее часто встречающийся элемент:\n', value_list[count_list.index(max(count_list))])
#     elif len(value_list) == len(my_list):
#         print('Все элементы повторяются одинаковое количество раз')
#     elif count_list.count(max(count_list)) > 1:
#         count = count_list.count(max(count_list))
#         print('Наиболее часто встречающиеся элементы:')
#         while count > 0:
#             print(value_list[count_list.index(max(count_list))])
#             value_list.pop(count_list.index(max(count_list)))
#             count_list.remove(max(count_list))
#             count -=1


# В одномерном массиве, состоящем из n вещественных элементов,
# вычислите номер минимального элемента массива и сумму элементов массива,
# расположенных между первым и вторым отрицательными элементами

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(round(random.uniform(-99.99, 99.99), 2))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     print('Номер минимальнго элемента массива:\n', my_list.index(min(my_list)) + 1)
#     find_list = []
#     count = 0
#     for f in my_list:
#         if f < 0 and (f not in find_list) and count < 2:
#             find_list.append(f)
#             count +=1
#         elif count == 2:
#             break
#         elif f >= 0:
#             pass
#         else:
#             print('В массиве недостаточно отрицательных элементов')
#             break
#     if len(find_list) == 2:
#         if (my_list.index(find_list[1]) - my_list.index(find_list[0])) > 1:
#             print('Сумма элементов между первым и вторым отрицательными:\n',
#                   sum(my_list[(my_list.index(find_list[0]) + 1):my_list.index(find_list[1])]))
#         else:
#             print('Мужду первым и вторым отрицатеьными элементами нет других элементов')


# Напишите программу, которая вводит с клавиатуры непустой массив целых чисел,
# и выводит число локальных максимумов
# (элемент является локальным максимумом, если он не имеет соседей, больших, чем он сам)

# while 1:
#     my_list = []
#     long = int(input('Введите количество значений массива: '))
#     while long:
#         a = (int(input('Введите число: ')))
#         my_list.append(a)
#         long -= 1
#     print('Ваш массив\n', my_list)
#     count_list = []
#     for f in my_list[1:-1]:
#         if my_list[my_list.index(f) - 1] < f > my_list[my_list.index(f) + 1]:
#             count_list.append(f)
#         else:
#             pass
#     print('Число локальных максимумов:\n', len(count_list))











