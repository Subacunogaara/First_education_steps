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
