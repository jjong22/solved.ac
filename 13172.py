def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

m = int(input())
mod = 1000000007
result = 0

for i in range(m):
    n, s = map(int, input().split())
    gcd_num = gcd(n, s)

    n, s = n // gcd_num, s // gcd_num
    result = (result + ((s * pow(n, -1, mod)) % mod)) % mod
    
print(result)