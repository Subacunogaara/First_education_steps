# 9. Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

# import time

# start = time.time()
# trig = False
# for i in range(1001):
#     if trig == False:
#         for j in range(i + 1, 1001):
#             if trig == False:
#                 for l in range(j + 1, 1001):
#                     if i**2 + j**2 == l**2:
#                         if i + j + l == 1000:
#                             print('Искомые числа: ', i, j, l, '\nпроизведение: ', i*j*l, '\nвремя вычисления: ', round(time.time() - start, 2), 'c')
#                             trig = True
#                             break
#             else:
#                 break
#     else:



# 10. Найдите сумму всех простых чисел меньше двух миллионов.

# import time, multiprocessing

# def counting(number, limit, queue):
#     print(multiprocessing.current_process().name, ' -- Start')
#     summa = 0
#     while number < limit:
#         d = 2
#         while d**2 <= number and number % d != 0:
#             d += 1
#         if d**2 > number:
#             summa += number
#         number += 1
#     else:
#         queue.put(summa)
#     print(multiprocessing.current_process().name, ' -- Finish')

# if __name__ == '__main__':
#     start = time.time()
#     queue = multiprocessing.Queue()
#     my_list = []
#     process1 = multiprocessing.Process(target=counting, args=(2, 1000000, queue))
#     process2 = multiprocessing.Process(target=counting, args=(1000000, 1500000, queue))
#     process3 = multiprocessing.Process(target=counting, args=(1500000, 2000001, queue))

#     process1.start()
#     process2.start()
#     process3.start()

#     process1.join()
#     process2.join()
#     process3.join()

#     for i in range(queue.qsize()):
#         my_list.append(queue.get())
#     print(sum(my_list), 'за', round(time.time() - start, 2), 'c')


# 11. Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, 
# расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?

# import numpy as np
# import math

# row_string = \
# '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \n\
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \n\
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \n\
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \n\
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \n\
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \n\
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \n\
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \n\
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \n\
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \n\
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \n\
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \n\
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \n\
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \n\
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \n\
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \n\
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \n\
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \n\
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \n\
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
# """
# Преобразования
# """
# list_of_rows = row_string.splitlines()
# array_of_lists = [x.strip().splitlines() for x in list_of_rows]
# two_d_array_of_lists_of_strings = [x[0].split(' ') for x in array_of_lists]
# final_array = []
# for i in two_d_array_of_lists_of_strings:
#     j = [int(x) for x in i]
#     final_array.append(j)
# arr = np.array(final_array)
# """
# Решение
# """
# big_horizontal = 0
# a = 0
# for i in range(20):
#     for j in range(17):
#         counter = math.prod(arr[i, j:j+4])
#         a += 1
#         if counter > big_horizontal:
#             big_horizontal = counter

# big_vertical = 0
# a = 0
# for i in range(20):
#     for j in range(17):
#         counter = math.prod(arr[j:j+4, i])
#         a += 1
#         if counter > big_vertical:
#             big_vertical = counter

# big_diagonal_from_left_to_right = 0
# a = 0
# for i in range(17):
#     for j in range(17):
#         counter = math.prod([arr[i,j], arr[i+1, j+1], arr[i+2, j+2], arr[i+3, j+3]])
#         a += 1
#         if counter > big_diagonal_from_left_to_right:
#             big_diagonal_from_left_to_right = counter

# big_diagonal_from_right_to_left = 0
# a = 0
# for i in range(17):
#     for j in range(17):
#         counter = math.prod([arr[i, j+3], arr[i+1, j+2], arr[i+2, j+1], arr[i+3, j]])
#         a += 1
#         if counter > big_diagonal_from_right_to_left:
#             big_diagonal_from_right_to_left = counter
# my_list = [big_horizontal, big_vertical, big_diagonal_from_left_to_right, big_diagonal_from_right_to_left]
# print('Наибольшее произведение:', max(my_list))
