# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random
list_1 = list()
count = 0
for i in range(int(input("введите число:  "))):
    list_1.append(random.randint(1,10))
print(*list_1)
num = int(input("Ведите число "))
for i in range(len(list_1)):
    if list_1[i] == num:
        count += 1

print(f"число {num} в списке {list_1} встречается {count} раз")        