n = int(input())
mylist = list(map(int, input().split()))

sorted_set = set()
for num in mylist:
    sorted_set.add(num)
    
sorted_list = list(sorted(sorted_set))

for num in sorted_list:
    print(num, end=' ')