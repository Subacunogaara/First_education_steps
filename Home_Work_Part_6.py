# Удалить в массиве первый и
# последний элементы

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 100))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     my_list.pop(0)
#     my_list.pop(-1)
#     print('В итоге получим:\n', my_list)


# Удалить в массиве все числа, которые повторяются более двух раз

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 5))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     work_list = my_list.copy()
#     for f in my_list:
#         if work_list.count(f) > 2:
#             work_list.remove(f)
#     print('Итоговый массив:\n', work_list)


# Найти в массиве все серии подряд идущих одинаковых элементов и
# удалить из них все элементы кроме одного

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 3))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     ind = -1
#     for f in my_list[-2::-1]:
#        if f == my_list[ind]:
#             my_list.pop(ind)
#        else:
#             ind -= 1
#     print('Итоговый массив:\n', my_list)


# Удалить в массиве все наибольшие элементы

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 3))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     count = my_list.count(max(my_list))
#     while count:
#         my_list.remove(max(my_list))
#         count -= 1
#     print('Массив без всех наибольших элементов:\n', my_list)


# Переставить элементы массива в обратном порядке

# import random
# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     while long:
#         my_list.append(random.randint(0, 3))
#         long -= 1
#     print('Ваш массив\n', my_list)
#     my_list.reverse()
#     print('Ваш массив в обратном порядке:\n', my_list)


