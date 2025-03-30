n = int(input())
result = 0
mod = pow(10, 9) + 7

for i in range(n):
    c, k = map(int, input().split())
    # 미분
    result += ((c * k % mod) * pow(2, k-1, mod)) % mod
    
print(result % mod)     