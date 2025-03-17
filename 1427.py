n = int(input())
k =[]

while (n != 0):
    k.append(n % 10)
    n = n // 10

k.sort()

for i in range (len(k)):
    print(k[len(k)-1-i], end="")