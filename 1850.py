def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
gcd_num = gcd(a, b)
result = '1' * gcd_num

print(result)