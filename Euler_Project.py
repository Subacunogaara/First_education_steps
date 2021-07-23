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


