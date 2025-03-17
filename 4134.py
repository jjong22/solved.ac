def next_prime(num):
    cnt = 0
    
    while(1):
        if (is_prime(num + cnt)):
            return num + cnt
        else : cnt += 1

def is_prime(num):
    if (num == 0):
        return False
    
    if (num == 1):
        return False
    
    for i in range(2, int(pow(num, 1/2)) + 1, 1):
        if (num % i == 0):
            return False
    
    return True

n = int(input())

for i in range(n):
    num = int(input())
    print(next_prime(num))

