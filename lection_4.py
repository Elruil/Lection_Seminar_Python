# def sumnumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)    
# sumnumbers(int(input("Ввыедите число : ")))    

# def sumnumbers(n, y = "Hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa    
# print(sumnumbers(int(input("Ввыедите число : "))))   

# def sum_str(*args):
#     res = ""
#     for i in args:
#         res += i
#     return res  
# print(sum_str("q", "e", "l", "df", "d")) 
# print(sum_str(1, 2, 3)) 
    
# from module import *    
# import module as m1    
# # from module import max1
# print(m1.max1(5,9))    
    
    
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)    

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]    
    greater = [i for i in array[1:] if i > pivot]  
    return quick_sort(less) + [pivot] + quick_sort(greater) 
print(quick_sort([2,1,2,4,5,8,1,5,8,3,5,1,9,9]))   


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j += 1  
            k += 1  
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1  
        while j< len(right):
            nums[k] = right[j]
            j += 1
            k += 1  
            
list = [1,3,6654,564,464,65464,54,4,4889,5]    
merge_sort(list)
print(list)      