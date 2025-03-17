n = int(input())

def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)   

for _ in range(n):
    a, b = map(int, input().split())
    
    r = gcd(a, b)
    
    print( (a // r) * b)