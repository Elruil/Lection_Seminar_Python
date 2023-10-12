'''
Список - это упорядоченный конечный набор элементов.
Тот же массив, в котором можно хранить элементы любых типов данных.
'''
'''
import random
list_1 = []
list_1 = list()
list_1 = [1, 8, 3, 4, 10]
print(list_1)
print(*list_1)     # * убрать запятые и скобки
for i in list_1:
    print(i)
print(len(list_1)) # размер списка
list_1.append(8)  # .append -  функция добавления указанного в скобках элемента в конец списка
print(list_1)
list_2 = list()
for i in range(int(input("введите число:  "))):
    list_2.append(random.randint(1,10))
    print(*list_2)
for i in range(len(list_2)):
    n = list_2.pop()
                    # .pop() - удаляет последний элемент списка по дефолту, значение в скобках удаляет элемент с данным индексом
    print(*list_2)  
print(n)  
list_3 = [1,3,4,5]
print(list_3)
list_3.insert(0,2)   # - .insert(1,1) - вставляет элемент ( , 1) на указанный индекс (1 , )
list_3.insert(5,7)
print(list_3)

'''
'''
кортеж - это неизменяемый список. Для защиты каких либо данных от изменний,
намеренных или случайных. Занимает меньше места в памяти и работают быстрее
, по сравнению со списками.
'''
'''
t = ()

print(type(t))
t= (1,3,4,5,)
print(type(t))
v = [3,7,7]
print(type(v))
print(v)
v = tuple(v)
print(type(v))
print(v)
a,b,c = v
print(a,b,c)
'''

'''
# словари - неупорядоченные коллекции произвольных объектов с доступом по ключу,
В списках в качестве ключа исполбзуется индекс элемента. В словаре для определения 
элемента используется значение ключа(строка, число).

'''

'''
d = {}
d = dict()
d["q"] = "qwerty"
d["e"] = "ewerty"
print(d)
print(d["q"])
dictionary = {}
dictionary = {'up':'↑','left':'←','down':'↓','right':'→'}
print(dictionary['down'])
print(dictionary['left'])
print(dictionary['up'])
print(dictionary['right'])
del dictionary['left']  # удаление ключа
dictionary[895] = 453634
for item in dictionary:
    print('{}: {} '.format(item, dictionary[item]))
for (k, v) in dictionary.items():
    print(k, v)
print(dictionary.items())    


'''


'''

Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два множества 
Вы можете совершать над ними любые стандартные операции, например, объединение,
пересечение и разность.
'''
'''
colors = {'red','green','blue'}
print(colors)
colors.add('red')  # .add  - добавляет значение в множество.
print(colors)
colors.add('Red')
print(colors)
colors.remove('red') # .remove - удаляет значение из множества, но если значения нет, выдает ошибку
print(colors)
colors.discard('red') # .discsrd - проверяет есть ли запрашиваемое значение и если есть удаляет его
colors.clear()  # .clear - удаляет все элементы из множества
print(colors)
q = set()  # создание множества

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # в новое создоваемое множество копируется указанное множество
print(c == a)
u = a.union(b) # объединянет два множества
print(u)
i = a.intersection(b) # находит пересечение указанных множеств
print(i)
d1 = a.difference(b) # разность множеств
print(d1)
d2 = b.difference(a)
print(d2)
d3 = b.difference(b)
print(d3)

q = a.union(b).difference(a.intersection(b))
print(q)

n = {1, 4, 5}
m = frozenset(n) # замораживаем множество, делая его неизменным
print(m)
'''
'''
LIST COMREHENSION
'''
list_1 = []
print(list_1) 
for i in range(1, 101):
    list_1.append(i)
print(list_1)   

list_2 = [i for i in range(1,101)]
print(list_2)
list_3 = [i for i in range(1,101) if i % 2 == 0]
print(list_3)
list_4 = [(i , i * i) for i in range(1, 101) if i % 1 == 0]
print(list_4)
list_5 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(list_5)