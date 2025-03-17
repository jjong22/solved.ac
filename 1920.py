from sys import stdin
n = int(stdin.readline())

num_set = set(map(int, stdin.readline().split()))

m = int(stdin.readline())

result_set = list(map(int, stdin.readline().split()))

for num in result_set:
    if num in num_set:
        print(1)
    else:
        print(0)
        
# search는 set에서 O(1)의 시간 복잡도를 가진다!