def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())

num_of_gcds = {}
num_of_gcds[1] = n

for i in range(2, n+1):
    for j in range(1, m+1):
        gcd_value = gcd(i, j)
        
        if num_of_gcds.get(gcd_value) == None:
            num_of_gcds[gcd_value] = 0
        num_of_gcds[gcd_value] += 1
            
result = 1        
for key, value in num_of_gcds.items():
    result *= pow(key, value, 1000000007)
    result %= 1000000007
    
print(result)