n = int(input())

for i in range(n):
    height, width, num = map(int, input().split())
    first = num % height
    second = num // height + 1
 
    if (num % height == 0):
        first = height
        second = num // height
    else :
        fisrt = num % height
        second = num // height + 1

    print( str(first) + str(second).zfill(2))