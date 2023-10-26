# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
import random
def arifmetic_progress(n1,n2,n3):
    arr = []    
    for i in range(1,n3 + 1):        
        arr.append(n1 + (i - 1)*n2)
    return arr
  
a = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите шаг прогрессии: "))
size = int(input("Введите количество элементов прогрессии: "))
print(arifmetic_progress(a,d,size))  


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random
def array_filling(a, list):
    for i in range(a):
        list.append(random.randint(-10, 10))
    return list  
def sort_arr(arr,min,max):
    res = []
    for i in range(len(arr)):
        if arr[i] >= min and arr[i] <= max:
            res.append(i)
    return res        

n = int(input("Введите размер массива: "))
min_number = int(input("Введите минимальное число искомого диапазона: "))
max_number = int(input("Введите максимальное число искомого диапазона: "))
list_1 = []
print(array_filling(n, list_1))
print(sort_arr(list_1, min_number,max_number))


