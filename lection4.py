def f(x):
    return(x*x)
print (f(5))
a = f
print(type(f))
print(type(a))
print(a(5))
"""
def calc1(a,b):
    return a + b
"""  
calc1 = lambda a,b: a + b  
# def calc2(a,b):
#     return a*b
calc2 = lambda a,b: a*b
def math(op,x,y):
    print(op(x,y))
math(calc1,5,45)
math(calc2,5,45)   
#  В списке хрнятся числа, получить вывод тольео четные и их квадрат
list1 = [1,2,3,5,8,15,23,38] 
list2 = list()
for i in range(len(list1)):
    if list1[i]%2 == 0:
        list2.append((list1[i],list1[i]*list1[i])) 
print(list2)        


data = [1,2,3,5,8,15,23,38] 
res = map(int, data)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x:(x, x**2), res))
print(res)


list_3 = [x for x in range(1,20)]
print(list_3)
list_3 = list(map(lambda x: x + 10, list_3))
print(list_3)

ls = "12 435 65 7 77 7777 23424 45"
print(ls)
ls = list(map(int, ls.split()))
print(ls)


ls4 = [12,33,45,46,57,568,55]
res = list(filter(lambda x: x % 10 == 5, ls4))
print(ls4)
print(res)

# функция ZIP
# применяется к набору итерируемых объектов и возвращает
# итератор с  кортежами из элементов входных данных
users = ['user1','user2','user3']
ids = [1234,4536,4567]
salary = [111,222,333,444,555]
data = list(zip(users,ids,salary))
print(data)

# Функция enumerate применяется к итерируемому объекту и возвращает
# новый итератор из индекса и элементов входных данных
ls5 =['Казань', 'Смоленск','Рыбки','Чикаго']
print(list(enumerate(ls5)))


# РАБОТА с ФАЙЛАМИ
'''
colors = ['red', 'green','blue']
data = open('file.txt','a')
data.writelines(colors)
data.close
создание файла и зпапись в него
'''
# with open ('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
# Перезапись данных в файле
    
print(45) 
# path = 'file.txt'
# data = open('file.txt','r')
# for line in data:
#     print(line)
# data.close()       
    # считывает указанные данные из файла и выводит их