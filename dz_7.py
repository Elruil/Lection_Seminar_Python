# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                              Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам             Парам пам-пам
# word = input("Введите строку песни: ")
# def rithm(word):
#     lst = word.split()
#     lst_gls = 'ауоыиэяюёе'
#     count = ""
#     arr_count = []
#     for i in range(len(lst)):
#         for j in lst[i].lower():
#             if j in lst_gls:
#                 count += j
#             print(count)    
#             arr_count.append(count)
#             count = ''
#     for i in range(len(arr_count) - 1):
#         if arr_count[i] == arr_count[i+1]:
#             return print("Парам пам-пам")
#         else:                    
#             return print("“Пам парам”")
# rithm(word)

# def rhythm(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum_w += 1
#         list_1.append(sum_w)
#     return len(list_1) == list_1.count(list_1[0])


# str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# if rhythm(str_1):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
phrase = stroka.split()
if len(phrase) <= 1:
    print("Количество фраз должно быть больше одной!")
else:    
    count_wovels = lambda phrase: sum(1 for i in phrase if i.lower() in 'аеёиоуыэюя')
    count_wovels_in_prase = [count_wovels(phrase) for phrase in phrase ]
    if all(count == count_wovels_in_prase[0] for count in count_wovels_in_prase):
        print('Парам пам-пам')
    else:
        print("Пам парам")    
        
        
# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36         
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!") 
#     else:        
#         a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#         for i in a:
#             print(*[f"{x}" for x in i])
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))
print_operation_table(lambda x, y: x - y, 5, 5)

