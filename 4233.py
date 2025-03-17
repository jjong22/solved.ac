def is_prime(num):
    if (num == 0):
        return False
    
    if (num == 1):
        return False
    
    for i in range(2, int(pow(num, 1/2)) + 1, 1):
        if (num % i == 0):
            return False
    
    return True

while(1):
    p, a = map(int, input().split())
    
    if ( (a == 0) and (p == 0)):
        break
    
    if (pow(a, p, p) != a):
        print("no")
        continue
    else :
        if is_prime(p) :
            print("no")
        else :
            print("yes")