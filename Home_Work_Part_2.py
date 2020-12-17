# Заполнить массив нулями, кроме первого и последнего элементов,
# которые должны быть равны единице.

# while 1:
#     my_list=[]
#     long=int(input('Введите длину массива больше 2: '))
#     if long > 2:
#         my_list.append(1)
#         for f in range(2, long):
#             my_list.append(0)
#         my_list.append(1)
#         print(my_list)
#     else:
#         print('Вы ввели неверную длину массива')


# Заполнить массив нулями и единицами, при этом данные значения чередуются,
# начиная с нуля.

# while 1:
#     my_list = []
#     long = int(input('Введите длину массива: '))
#     if long == 1:
#         my_list.append(0)
#         print(my_list)
#     elif (long %2) ==0:
#         for f in range(0, long//2):
#             my_list.append(0)
#             my_list.append(1)
#         print(my_list)
#     else:
#         for f in range(0, (long-1)//2):
#             my_list.append(0)
#             my_list.append(1)
#         my_list.append(0)
#         print(my_list)


# Заполнить массив последовательными нечетными числами,
# начиная с единицы.

# while 1:
#     my_list=[1]
#     long=int(input('Введите длину массива больше 1: '))
#     if long > 1:
#         for f in range(2, long*2):
#             if (f % 2) != 0:
#                 my_list.append(f)
#         print(my_list)
#     else:
#         print('Вы ввели неверное значение')


# Сформировать массив из элементов арифметической прогрессии
# с заданным первым элементом x и разностью d

# while 1:
#     my_list=[]
#     x=int(input('Введите первый элемент арифметической прогрессии: '))
#     d=int(input('Введите шаг арифметической прогрессии: '))
#     long=int(input('Введите длину арифметической прогрессии(больше 1): '))
#     if long > 1:
#         my_list.append(x)
#         for f in range(1, long):
#             my_list.append(x+d)
#             x = x+d
#         print(my_list)
#     else:
#         print('Вы ввели неверную длину арифметической прогрессии')


# Сформировать возрастающий массив из четных чисел

# while 1:
#     my_list=[]
#     first=int(input('Введите первое четное число: '))
#     if (first % 2) == 0:
#         long=int(input('Введите длину массива: '))
#         my_list.append(first)
#         for f in range(1, long):
#             first += 2
#             my_list.append(first)
#         print(my_list)
#     else:
#         print('Введено нечётное число')


# Сформировать убывающий массив из чисел, которые делятся на 3.

# while 1:
#     my_list=[]
#     first=int(input('Введите первое число которое делится на 3: '))
#     if (first % 3) ==0:
#         long=int(input('Введите длину массива: '))
#         my_list.append(first)
#         for f in range(1, long):
#             first -= 3
#             my_list.append(first)
#         print(my_list)
#     else:
#         print('Введенное число не делится на 3')


# Создать массив из n первых чисел Фибоначчи

# while 1:
#     my_list=[]
#     long=int(input('Введите длину массива из чисел Фибоначчи: '))
#     add1 = 0
#     add2 = 1
#     if long >=2:
#         my_list.append(0)
#         my_list.append(1)
#         for f in range(2, long):
#             fib = add1 + add2
#             my_list.append(fib)
#             add1 = add2
#             add2 = fib
#         print(my_list)
#     elif long == 1:
#         my_list.append(0)
#         print(my_list)
#     else:
#         print('Введена некорректная длина массива!!!')
