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


# 5. 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
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


# 6. Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

# sum_kvad = 0
# summa = 0
# for i in range(1, 101):
#     sum_kvad += i**2
#     summa += i
# kvad_sum = summa**2
# print('Квадрат суммы ', kvad_sum, ' , сумма квадратов ', sum_kvad)
# print('Разница ', kvad_sum - sum_kvad)


# 7. Какое число является 10001-м простым числом?

# import time

# start = time.time()
# count = 0
# check_number = 2
# while count != 10001:
#     checker = 0
#     for i in range(2, check_number + 2):
#         if checker < 2:
#             if check_number % i == 0:
#                 checker += 1
#         else:
#             break
#     else:
#         count += 1
#     check_number += 1
# else:
#     print(check_number - 1, ' - время расчёта: ', round((time.time() - start), 2), 'c')


# 8. Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.

# import time, math
# start = time.time()

# our_number = 0
# our_list = []
# number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# str_of_number = str(number)
# for i in range(len(str_of_number) - 12):
#     list_of_numbers = [int(x) for x in list(str_of_number[i:i+13])]
#     multiple = math.prod(list_of_numbers)
#     if multiple > our_number:
#         our_number = multiple
#         our_list = list_of_numbers

# print(our_number, ' за', round(time.time() - start, 2), 'c\n', 'список чисел: ', our_list)


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
