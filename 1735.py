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
        
    
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

r = b1 // gcd(b1, b2) * b2 # b1, b2 분모의 최대공약수

a1 = a1 * r // b1
a2 = a2 * r // b2

r2 = gcd(a1+a2, r)

print( (a1+a2) // r2, r // r2 )