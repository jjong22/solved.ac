from itertools import accumulate

def can_make_min_value(numlist, mid, k):
    total_k = 0
    for num in numlist:
        if num < mid:
            total_k += mid - num
    return total_k <= k

n, k = map(int, input().split())
num_list = [int(input()) for _ in range(n)]
num_list.sort()

left = num_list[0]
right = num_list[-1] + k # max value
result = left

while left <= right:
    mid = (left + right) // 2
    if can_make_min_value(num_list, mid, k):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(result)
