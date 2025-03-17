from itertools import permutations

n = int(input())
number = []
result = []

for i in range(n):
    num = int(input())
    number.append(num)

for i in range(n):
    if (number[i] == 1): result.append(1)
    elif (number[i] == 2): result.append(2)
    elif (number[i] == 3): result.append(4)
    elif (number[i] == 4): result.append(7)
    elif (number[i] == 5): result.append(13)
    elif (number[i] == 6): result.append(24)
    elif (number[i] == 7): result.append(44)
    elif (number[i] == 8): result.append(81)
    elif (number[i] == 9): result.append(149)
    elif (number[i] == 10): result.append(274)
    
for i in range(n):
    print(result[i])