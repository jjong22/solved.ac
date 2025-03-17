x = int(input())
n = int(input())
c = []
d = int()

for i in range(n):
    a, b = map(int, input().split())
    c.append(a)
    c.append(b)

for i in range(n):
    d = d + (c[2*i] * c[2*i+1])

if (x == d):
    print("Yes")
else :
    print("No")


