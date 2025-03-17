n = int(input())
star = ""

for i in range(n):
    for j in range(i+1):
        star = star + "*"
    print(star)
    star = ""