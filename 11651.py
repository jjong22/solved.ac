mymap = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    mymap.append((x, y))
    
mymap.sort(key=lambda x: (x[1], x[0]))

for x, y in mymap:
    print(x, y)