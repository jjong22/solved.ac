n = int(input())
cnt = 2

while(1):
    if (n % cnt == 0):
        
        while(1):
            print(cnt)
            n = n // cnt
            
            if (n % cnt != 0):
                break
    
    if (n == 1):
        break
    
    cnt += 1