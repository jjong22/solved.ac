from collections import Counter

n = int(input())
numbers = []

sum = 0

for i in range(n):
    num = int(input())
    sum += num
    numbers.append(num)
    
numbers.sort()

arith_mean = int(round(sum / n, 0))
median = numbers[n//2]

counter = Counter(numbers)
mode = counter.most_common()
try:
    if (mode[0][1] == mode[1][1] ): # 최빈값이 여러개
        mode = mode[1][0]
    else :
        mode = mode[0][0]
except:
    mode = mode[0][0]
    
rnge = numbers[-1] - numbers[0]

print(arith_mean)
print(median)
print(mode)
print(rnge)