# Создать текстовый файл. Записать в него построчно данные
# которые вводит пользователь. Окончанием ввода
# будет служить пустая строка

# file = open ('text.txt', 'w')
# # while True:
# #     words = input('Введите текст:\n')
# #     if words.isspace() or len(words) == 0:
# #         break
# #     else:
# #         file.write(words + '\n')
# # file.close()
# # file = open('text.txt')
# # print(file.read())
# # file.close()


# Из файла посчитать количество строк, а также
# для каждой строки количество символов и слов

# file = open('Home_Work.txt')
# my_lynes = file.readlines()
# lines = len(my_lynes)
# count_lines = 1
# print('В файле ', lines, ' строк:')
# for f in my_lynes:
#     print(count_lines, ' строка: ', len(f.replace(' ', '')), ' символов',
#           ' и ', len(f.split()), ' слов.')
#     count_lines += 1
# file.close()


# Создать файл. Написать программу, которая
# откроет этот файл в режиме чтения, считает
# из него данные и запишет строки в другой файл
# из ("один, два, три...")
# в ("one, two, three...")

# file = open('Vocabulary.txt')
# voc = file.read()
# print(voc)
# file.close()
# voc_dict = {'один': 'one',
#             'два': 'two',
#             'три': 'three',
#             'четыре': 'four',
#             'пять': 'five'}
# cab = voc.replace(',', '')
# file = open('new_vocabulary.txt', 'w')
# for f in cab.split():
#     if f in voc_dict:
#         file.write(voc_dict[f]+ ', ')
# file.close()
# file = open('new_vocabulary.txt', 'r')
# print(file.read().rstrip(' ,'))
# file.close()


# Создать файл в котором несколько чисел записаны
# через пробел(100 200 300...). Затем открыть файл
# и посчитать сумму этих чисел

# file = open('some_text_file.txt', 'w')
# print('Введите числа которые нужно просуммировать:')
# while True:
#     income = input()
#     if income.isnumeric():
#         file.write(income)
#         file.write(' ')
#     elif income.isspace() or len(income) == 0:
#         break
#     else:
#         print('Вы ввели некорректное число!!!')
# file.close()
# file = open('some_text_file.txt')
# calc = []
# for f in file.read().split():
#     calc.append(int(f))
# print('Результат:\n', sum(calc))
# file.close()


# В данном массиве найдите два наименьших элемента

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     mal = min(my_list)
#     my_list.remove(min(my_list))
#     print('Два наименьших элемента массива:\n', mal, 'и', min(my_list))


# Определите, есть ли в массиве повторяющиеся элементы

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 10))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     work_list = my_list.copy()
#     count_dict = {}
#     for f in my_list:
#         if f in work_list:
#             work_list.remove(f)
#             if f in work_list:
#                 count = work_list.count(f)
#                 count_dict[f] = count + 1
#                 while count > 0:
#                     work_list.remove(f)
#                     count -= 1
#     if len(count_dict.keys()) > 0:
#         for i in count_dict:
#             print(i, 'в количестве', count_dict.get(i), 'шт.')
#     else:
#         print('В массиве нет повторяющихся элементов!!!')


# В данном массиве найдите наибольшую серию подряд идущих элементов,
# расположенных по возрастанию

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 50))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     count = 1
#     serial_list = []
#     count_list = []
#     count_for_count_list = []
#     work_list = my_list.copy()
#     for f in my_list[:-1]:
#         serial_list.append(f)
#         if work_list[0] < work_list[1]:
#             count += 1
#             serial_list.append(work_list[1])
#             count_for_count_list.append(count)
#             work_list.pop(0)
#         else:
#             if len(serial_list) > len(count_list):
#                 count_list = serial_list
#                 serial_list = []
#                 count = 1
#             else:
#                 serial_list = []
#                 count = 1
#             work_list.pop(0)
#         if len(serial_list) > 0:
#             serial_list.pop()
#     print('Наибольшая серия:\n', max(count_for_count_list), '\n', count_list)


# В массиве найдите количество серий из четверок
# подряд идущих попарно различных элементов
# (версия как я понял)

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 3))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     ind = 1
#     count = 0
#     count_dict = {}
#     for f in my_list[:-4]:
#         if f == my_list[ind] and f != my_list[ind + 1] and my_list[ind + 1] == my_list[ind +2]:
#             count += 1
#             ind += 1
#             count_dict[count] = my_list[ind - 2:ind + 2]
#         else:
#             ind +=1
#     if count > 0:
#         print('Количество серий:', count)
#         for i in count_dict:
#             print(count_dict.get(i))
#     else:
#         print('Искомой серии не найдено!!!')


# В массиве найдите количество серий из четверок
# подряд идущих попарно различных элементов
# (версия как объяснил Google трактовку условия)

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 5))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     ind = 1
#     count = 0
#     count_dict = {}
#     for f in my_list[:-4]:
#         if f != my_list[ind] and f != my_list[ind + 1] and f != my_list[ind + 2]\
#                 and my_list[ind] != my_list[ind + 1] and my_list[ind] != my_list[ind + 2]\
#                 and my_list[ind + 1] != my_list[ind + 2]:
#             count += 1
#             ind += 1
#             count_dict[count] = my_list[ind - 2:ind + 2]
#         else:
#             ind +=1
#     if count > 0:
#         print('Количество серий:', count)
#         for i in count_dict:
#             print(count_dict.get(i))
#     else:
#         print('Искомой серии не найдено!!!')


# Определите, можно ли вычеркнуть из данного массива одно число так,
# чтобы оставшиеся числа оказались упорядоченными по возрастанию

# def chek_sort(some_list):
#     ind = 1
#     for f in some_list[:-1]:
#         if f > some_list[ind]:
#             return False
#         else:
#             ind += 1
#     if ind == len(some_list):
#         return True
#
#
# my_list = [1, 2, 3, 4, 5, 9, 3, 8]
# if chek_sort(my_list):
#     print('Список сортирован по возрастанию!')
# else:
#     ind = 0
#     count = 1
#     for f in my_list:
#         work_list = my_list.copy()
#         work_list.pop(ind)
#         if chek_sort(work_list):
#             print('Если вычеркнуть', my_list[ind], 'то список отсотрирован')
#             ind += 1
#         elif count == len(my_list):
#             print('Нужно вычеркнуть более одного числа!!!')
#         else:
#             ind += 1
#             count += 1


# В массиве заменить все числа, большие данного числа,
# на среднее арифметическое всех чисел массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 10))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     zad = int(input('Введите число: '))
#     ind = 0
#     arif = round(sum(my_list)/len(my_list), 2)
#     for f in my_list:
#         if f > zad:
#             my_list[ind] = arif
#             ind += 1
#         else:
#             ind += 1
#     print('Среднее арифметическое всех чисел: ', arif, '\n', 'Итоговый массив:\n', my_list)


# Дан массив. Заменить все числа, меньшие последнего
# элемента массива, на первый элемент

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 10))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     ind = 0
#     for f in my_list:
#         if f < my_list[-1]:
#             my_list[ind] = my_list[0]
#             ind += 1
#         else:
#             ind += 1
#     print('Итоговый массив:\n', my_list)


# Поменять местами наибольший и наименьший элементы массива

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     bol = max(my_list)
#     men = min(my_list)
#     ind_bol = my_list.index(bol)
#     ind_men = my_list.index(men)
#     my_list[ind_bol] = men
#     my_list[ind_men] = bol
#     print('наибольшее и наименьшее числа: ', bol, 'и', men, '\n', 'Итоговый массив:\n', my_list)


# Найти наибольший четный элемент массива
# и поменять его местами с наименьшим нечетным элементом.
# Если одного из таких элементов нет,
# то всем элементам массива присвоить значение, равное нулю

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     work_list = my_list.copy()
#     for j in my_list:
#         if j % 2 != 0:
#             work_list.remove(j)
#     bol = max(work_list)
#     men = min(work_list)
#
#     def nul(x):
#         return x*0
#
#     if bol in my_list and men in my_list and bol != men:
#         ind_bol = my_list.index(bol)
#         ind_men = my_list.index(men)
#         my_list[ind_bol] = men
#         my_list[ind_men] = bol
#         print('наибольшее и наименьшее чётные числа: ', bol, 'и', men, '\n', 'Итоговый массив:\n', my_list)
#     else:
#         my_list = list(map(nul, my_list))
#         print('Итоговый массив:\n', my_list)


# Заменить каждый элемент массива с четным номером на соседний слева элемент

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     ind = 1
#     for f in my_list[1::2]:
#         my_list[ind] = my_list[ind - 1]
#         ind += 2
#     print('Итоговый массив:\n', my_list)
