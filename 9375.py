n = int(input())
mylist = []
result = 1
myresult = []

for i in range (n):
    m = int(input())
    for j in range(m):
        name, sort = map(str, input().split())
        mylist.append(sort)
        mylist.append(1)
        if (mylist.count(sort) == 2):
            mylist.pop()
            mylist.pop()
            mylist[mylist.index(sort) + 1] += 1 
            
    for j in range (len(mylist)):
        if (j % 2 == 0):
            continue
        else:
            result *= (mylist[j] + 1)
    
    result = result - 1
    myresult.append(result)
    result = 1
    mylist.clear()
            
for i in range(len(myresult)):
    print(myresult[i])