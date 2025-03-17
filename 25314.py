n = int(input())

a = int(n / 4)

st = "int"

for i in range(a):
    st = "long " + st

print(st)