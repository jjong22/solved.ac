def is_prime(num):
    if (num == 0):
        return False
    
    if (num == 1):
        return False
    
    for i in range(2, int(pow(num, 1/2)) + 1, 1):
        if (num % i == 0):
            return False
    
    return True

def count_prime(num):
    cnt = 0
    for i in range(num + 1, 2 * num + 1, 1):
        if (is_prime(i)):
            cnt += 1
    
    return cnt

while(1):
    n = int(input())
    
    if (n == 0): break
    
    print(count_prime(n))
    