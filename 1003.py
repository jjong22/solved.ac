def fibonacchi(n):

    sum1 = 0
    sum2 =1

    save = 1

    for i in range (n - 2):
        sum2 = sum2 + sum1
        sum1 = save
        save = sum2
    
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else :
        return sum2 + sum1

mylist_0 = []    
mylist_1 = [] 
    
num = int(input())

for i in range(num):
    in_num = int(input())
    if (in_num == 0):
        mylist_0.append(1)
        mylist_1.append(0)
    else:
        mylist_0.append(fibonacchi(in_num - 1))
        mylist_1.append(fibonacchi(in_num))

for i in range(num):
    print(mylist_0[i],mylist_1[i])