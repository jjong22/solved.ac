a = 1
b = 1
c = []
i = 0

while(a != 0 and b != 0):
    a, b = map(int, input().split())
    c.append(a)
    c.append(b)
    i = i+1

for j in range(i-1):
    print(c[2*j] + c[2*j + 1])