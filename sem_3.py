s = "POPOOOOPPPPPOOPP"
n = 0

while "O"*n in s:
    n+=1
    
print(n - 1)
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

uniq_count = 0
count = 0 
m = [1, 1, 2, 0, -1, 3, 4, 4]
n = set(m)
print(len(n))
print(m)
uniq_count = 0
for i in range(len(m)):
        for j in range(len(m)):
            if m[i] == m[j]:
                count+=1
                if count == 1:
                    uniq_count +=1
                elif count > 1:
                    uniq_count = uniq_count 
        count = 0            
print(uniq_count)                








    
     