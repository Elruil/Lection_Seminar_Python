# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел 
# a0, a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
n = int(input("Введите номер элемента: "))

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(n + 1))    
list_1 = []
for i in range(2, 10):
    list_1.append(fib(i))
print(list_1)   
print(list_1[n -1])

# факториал
a = int(input("Введите число:  "))
def factorial(a):
     if a == 1:
         return a
     else:
         return a*factorial(a - 1)
print(f"Факториал {a} равен {factorial(a)}")     
        
        
# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1



# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


m = int(input("Введите число: "))


def ch(m,x = 2):
    if m == 2 or x*x > m:
        return True
    elif m%x == 0:
        return False
    return ch(m, x + 1)

print(ch(m))

# 37
def revers(g, st):
    
    if g < 1:
        return st
    return  revers(g - 1,input("Введите число: ")) + st

g = int(input("Число "))
st = ""
print(revers(g,st))

s = input("Введите слово для проверки ")
def pal(s):
    if len(s) <=1:
        return True
    elif s[0] != s[-1]:
        return False
    return pal(s[1:-1])
print(pal(s))