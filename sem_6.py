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

n1 = int(input("Введите размер первого массива: "))
n2 = int(input("Введите размер второго массива: "))
list_1 = []
list_2 = []
print(array_filling(n1, list_1))
print(array_filling(n2, list_2))
print(*array_sort(list_1, list_2))


