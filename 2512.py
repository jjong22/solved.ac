def binary_search(numlist, requested_value):
    start = 0
    end = numlist[-1]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        sum_value = 0

        for num in numlist:
            if num > mid:
                sum_value += mid
            else:
                sum_value += num

        if sum_value > requested_value:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result    

n = int(input())

numlist = list(map(int, input().split()))
sum_value = sum(numlist)

requested_value = int(input())

numlist.sort()

if (sum_value < requested_value):
    print(numlist[-1]) # max vlaue
else:
    print(binary_search(numlist, requested_value))