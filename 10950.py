a = int(input())
d = []

for i in range(a):
    b, c = map(int, input().split())
    d.append(b)
    d.append(c)


for i in range(a):
    print(d[2*i]+d[2*i+1])