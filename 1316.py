n = int(input())
mylist = []
no_group = 0
tot = 0

for i in range(n):
    word = input()
    length = len(word)
    
    mylist.append(word[0])
    for i in range(length-1):
        mylist.append(word[i+1])
        if(mylist[i+1] == mylist[i]):
            continue
        elif(mylist.count(word[i+1]) > 1):
            no_group = 1
            break
    if (no_group != 1):
        tot += 1
    no_group = 0
    mylist.clear()
    
print(tot)