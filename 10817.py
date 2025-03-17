mylist = list(map(int, input().split()))
mylist.remove(max(mylist))
print(max(mylist))