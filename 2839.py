n = int(input())

e = int()
num = int()
num_squ = int()
save = int()

f = []

for i in range(n):
    e = i * 3
    for j in range(n):
        num = n - e
        if (num < 0):
            break
        if (num % 5 == 0):
            num_squ = int(num/5)
            f.append(num_squ + i)

if (len(f)==0):
    print(-1)
else :
    print(min(f))