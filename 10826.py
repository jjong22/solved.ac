sum1 = 0
sum2 =1

save = 1

n = int(input())

for i in range (n - 2):
    sum2 = sum2 + sum1
    sum1 = save
    save = sum2
    
if (n == 0):
    print(0)
elif (n == 1):
    print(1)
else :
    print(sum2 + sum1)