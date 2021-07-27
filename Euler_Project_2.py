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


