n = 0

while(1):
    n = int(input())
    
    if(n == -1):
        break
    
    div_set = []
    sum = 0
    
    for i in range(n // 2):
        if ( n % (i+1) == 0 ):
            div_set.append(i+1)
            sum += i+1
            
    if (sum == n):
        print("%d =" %(n), end=" ")
        for i in range(len(div_set) - 1):
            print("%d +" % (div_set[i]),end=" " )
        print(div_set[-1])
    else :
        print("%d is NOT perfect." %(n))