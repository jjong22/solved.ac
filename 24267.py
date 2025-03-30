n = int(input())

sum = 0 

if n <= 2:
    sum = 0
else:
    sum = n * (n-1) * (n-2) // 6
            
print(sum)
print(3)