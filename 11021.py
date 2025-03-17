import sys

n = int(sys.stdin.readline())
c = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c.append(a)
    c.append(b)

for i in range(n):
    
    print("Case #"+str(i+1)+":",c[2*i] + c[2*i+1])