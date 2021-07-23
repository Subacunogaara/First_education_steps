# 4. Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

# trig = False
# for i in range(999, 99, -1):
#     if trig == False:
#         for j in range(i, i-2, -1):
#             mul = str(i * j)
#             if len(mul) % 2 == 0:
#                 r = int(len(mul)/2)
#                 for n in range(r):
#                     if mul[n] == mul[::-1][n]:
#                         continue
#                     else:
#                         break
#                 else:
#                     print(mul, ' ', i, '*', j)
#                     trig = True
#                     break
#             else:
#                 r = int((len(mul)-1)/2)
#                 for n in range(r):
#                     if mul[n] == mul[::-1][n]:
#                         continue
#                     else:
#                         break
#                 else:
#                     print(mul, ' ', i, '*', j)
#                     trig = True
#                     break
#     else:
#         break


# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# import time

# ran = 1
# for n in range(1, 21):
#     ran *= n
# print(ran)
# start = time.time()
# for i in range(20, ran+1):
#     for j in range(2, 21):
#         if i % j == 0:
#             continue
#         else:
#             break
#     else:
#         print(i)
#         break
# print('%s секунд' % (time.time() - start))
