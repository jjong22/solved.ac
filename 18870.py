n = int(input())

num_list = list(map(int, input().split()))

for i in range(n):
    num_list[i] = [num_list[i], i]

num_list.sort()
prev_value = None
result = 0

for i in range(n):
    if i == 0:
        prev_value = num_list[i][0]
        num_list[i][0] = 0
    else:
        if num_list[i][0] == prev_value:
            num_list[i][0] = result
        else:
            prev_value = num_list[i][0]
            result += 1
            num_list[i][0] = result

num_list.sort(key=lambda x: x[1])

for i in range(n):
    print(num_list[i][0], end=' ')