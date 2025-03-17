n1 = input()
numlist1 = map(int, input().split())

bst = dict()
for num in numlist1:
    if num in bst:
        bst[num] += 1
    else:
        bst[num] = 1
    
n2 = input()
numlist2 = map(int, input().split())

for num in numlist2:
    if num in bst:
        print(bst[num], end=' ')
    else:
        print(0, end=' ')