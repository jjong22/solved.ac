n = int(input())

a_list = []
b_list = []

for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

a_list.sort(reverse=True)
result = 0 

for i in range(n):
    result += a_list[i] * (n - i) + b_list[i]

print(result)