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
    num = int(input())
    
    if (_ == 0):
        min = num
        prev = num
        continue
    
    if (_ == 1):
        diff_num = num - prev

    if (diff_num > gcd(diff_num, num - prev)):
        diff_num = gcd(diff_num, num - prev)

    if (_ == n-1):
        max = num
    
    prev = num
        
print( (max - min) // diff_num - n + 1 )