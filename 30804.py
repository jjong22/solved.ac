import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
fruits = list(map(int, input().split()))

fruit_count = {}
left = 0
max_length = 0

for right in range(n):
    fruit = fruits[right]
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

    while len(fruit_count) > 2:  # 과일 종류가 2개 초과하면 left 이동
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(str(max_length) + '\n')
