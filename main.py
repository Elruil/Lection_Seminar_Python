# n = 5
# m = None
# print(type(m))
# m = "dfiog\"hdfiugh"
# print(type(m))
# print(m)
# m = 1233
# print(type(m))
# print(f"m = {m}")
# a = 7865
# b = 324
# c = 765
# print("a = {}, b = {}, c = {}".format(a, b, c))
# print('Введите первое число')
# a = int(input())
# print(f"Введенное число а = {a}")
# b = int(input("Введите второе число :  "))
# print(f"Введенное число b = {b}")
# print(a, " + ", b ," = ", a % b)

# a = 4.443535
# b = 6.435355
# print(round(a*b, 3))

# username = input("Ведите имя :  ")
# if username == "Маша":
#     print(' Ура, это же Маша')
# elif username == "Марина":
#     print(" Я так ждала вас Марина")
# elif username == "Ильнвр":
#     print("Ильнар - топ")
# else:
#     print("Привет, ", username)    

# n = int(input("Введите число : "))
# flag = True
# i = 2
# while flag:
#     if n % i == 0: 
#         flag = False
#         print(i)
#     elif i > n // 2 :
#         print(n)
#         flag = False
#     i += 1       


# a = "qwerty"  
# print(a[0])  
# for i in a:
#     print(i)  

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "+"
#     print(line)  

# text = "СъЕШЬ еще этих МяГкИх францухскиъ булок "
# print(len(text))   
# print("еще" in text)
# print(text.lower())
# print(text.upper())   
# print(text.replace("ЕЩЕ" , "еще"))   


# # - обозначение строки как комментарий
# """
# заключенный 
# между апострофами текст 
# закоментирован
# """
# # - выделив нужный объем кода и зажав
# #   CTRL + K , а затеи CTRL + C
# #   закоментирует этот код.
# #   Анологично CTRL + K , а затеи CTRL + U
# #   раскоментирует выделенный объем кода.
#     # / - деление по умолчанию
#     # // - целочисленное деление
#     # % - остаток от деления
#     # ** - возведение в степень

# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2


# n = int(input("Введите число n :  "))
# m = int(input("Введите введите число m :  "))
# print((m + n - 1 ) // n)

# Задача 2: Найдите сумму цифр трехзначного числа.

# number = int(input("Введите трехзначное число : "))
# summa = 0
# while number > 0:
#     summa = number%10 + summa
#     number = number //10
# print(summa)    

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# s = int(input("Введите общее число журавликов "))

# n1 = int(s*1/6)
# n2 = int(s*4/6)
# n3 = n1
# print(n1, n2, n3)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# num = int(input("Введите номер билета для проверки :  "))
# num1 = num//1000
# num2 = num%1000
# res1 = int(num1/100) + int((num1%100)//10) + int(num1%10) 
# res2 = int(num2/100) + int((num2%100)//10) + int(num2%10) 
# if res1 == res2:
#     print("YES")
# else:
#     print("NO")    

# # Задача 8: Требуется определить, можно ли от шоколадки размером n
# # × m долек отломить k долек, если разрешается сделать один разлом по
# # прямой между дольками (то есть разломить шоколадку на два
# # прямоугольника).

# a = int(input("Введите количество долек по одной стороне:  "))
# b = int(input("Введите количество долек по другой стороне :  "))
# c = int(input("Введите число долек которое вы хотите получить :  "))

# if  c < a * b and ((c % a == 0) or(c % b == 0)):
#     print("yes")
# elif c == 1 or c > a * b:
#     print("no")  

# Задача №9. Общее обсуждение
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

# n = int(input("Введите число :  "))
# i = 1
# res = 1
# while n >= i:
#     res *= i
#     i = i + 1
# print(res)    

# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6	

# F(n) = F(n-1) + f(n-2)
# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)

# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
# а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31