sum = 0

for i in range (5):
    n = int(input())
    if (n < 40):
        sum += 40
    else:
        sum += n

equ = int(sum/5)
print(equ)