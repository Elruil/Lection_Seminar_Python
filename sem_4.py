# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

user_str = input('Введите символы строки через пробел: ').split()
print(user_str)
my_list = {}
# <sep>.join(<iterable>)
for i in user_str:
    if i in my_list:
        print(f"{i}_{my_list[i]}", end =" ")
    else:
        print(f"{i}", end = " ")
    my_list[i] = my_list.get(i, 0) + 1  
print()    
print(my_list)  

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

user_text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells ".upper().split()
array_text = []
print(user_text)
m_text = set(user_text)
print(len(m_text))
for i in user_text:
    if i not in array_text:
        array_text.append(i)
print(len(array_text))     

s = "a a a a b ----- c  ++++++a+++++ a"
s1 = s.replace("+"," ").replace("-"," ").split()
print(s1)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
list_1 = []
list_2 = []
a, b = input("Введите два числа через пробел: ").split()
print(f"{a}, {b}")  

for i in range(int(a)):
    list_1.append(random.randint(1, 10))

for i in range(int(b)):
    list_2.append(random.randint(1, 10)) 
print(*list_1)    
print(*list_2)  
mn_1 = set(list_1)
mn_2 = set(list_2)
print(mn_1)    
print(mn_2) 
mn_3 = mn_1.intersection(mn_2)
print(sorted(mn_3))


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import random

a = int(input("количество кустов черники: "))
list_1 = []

for i in range(int(a)):
    list_1.append(random.randint(1, 10))

print(*list_1) 
count = 0
max_summa = 0
summa = 0
while count < a :
    for i in range(count - 3, count):
        summa = list_1[i] + summa
    count += 1  
    if max_summa < summa:
        max_summa = summa 
    summa = 0
print(max_summa)           
      
  