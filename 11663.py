import sys

def binary_search_left(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if lines[mid] == target:
            return mid
        elif lines[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def binary_search_right(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if lines[mid] == target:
            return mid
        elif lines[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1 

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

lines = list(map(int, input().split()))
lines.sort()

for i in range(m):
    x, y = map(int, input().split())
    if y < x:
        x, y = y, x
    left_idx = binary_search_left(0, n-1, x)
    right_idx = binary_search_right(0, n-1, y)
    
    if left_idx > right_idx:
        print("0\n")
    else:
        print(str(right_idx - left_idx + 1) + "\n")