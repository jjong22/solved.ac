a = int(input())
b = int(input())

c = b % 10 # 1의 자릿수
d = int(((b % 100) - c) / 10) # 10의 자릿수
e = int(((b % 1000) - (c + 10*d)) / 100) # 100의 자릿수

print(a * c)
print(a * d)
print(a * e)
print(a * b)