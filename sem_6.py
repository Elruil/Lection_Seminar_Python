# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
import random
def array_filling(a, list):
    for i in range(a):
        list.append(random.randint(1, 10))
    return list   
def array_sort(my_list_1, my_list_2):
    result = []
    for i in range(len(my_list_1)):
        if my_list_1[i] not in my_list_2:
            result.append(my_list_1[i])
    return result

def min_around_num(list):
    count = 0
    for i in range(1,len(list)):
        if list[i] > list[i -1] and list[i] > list[i+1]:
            count= count + 1
    return count  

n1 = int(input("Введите размер первого массива: "))
n2 = int(input("Введите размер второго массива: "))
list_1 = []
list_2 = []
print(array_filling(n1, list_1))
print(array_filling(n2, list_2))
print(*array_sort(list_1, list_2))


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

n3 = n1 = int(input("Введите размер массива: "))
list_3 = []
print(array_filling(n3, list_3))

print(f"Количество элементов соответствущих условию : {min_around_num(list_3)}")