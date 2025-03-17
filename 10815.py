n1 = input()
numlist1 = map(int, input().split())

bst = dict()
for num in numlist1:
    bst[num] = 1
    
n2 = input()
numlist2 = map(int, input().split())

for num in numlist2:
    if num in bst:
        print(1, end=' ')
    else:
        print(0, end=' ')