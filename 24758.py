import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_partial(n):
    if n % 4 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % (pow(i, 2)) == 0:
            return False
    return True

a, b = map(int, input().split())

if a == b:
    print('no credit')
elif is_prime(a) and is_prime(b):
    print('full credit')
else:
    if is_partial(a) and is_partial(b) and math.gcd(a, b) == 1: # 제곱 인수가 없을 경우!
        print('partial credit')
    
    else :
        print('no credit')