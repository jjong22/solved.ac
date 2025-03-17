import sys

n = int(sys.stdin.readline())  # 빠른 입력

count = [0] * 10001  # 각 숫자의 등장 횟수를 저장하는 배열

# 입력을 받아서 등장 횟수 증가
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)  # 등장 횟수만큼 출력