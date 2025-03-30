mod = 1000000007
max_n = 1000000

dp = [1] * (max_n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, max_n+1):
    dp[i] = dp[i-1] * i % mod

def factorial (n):
    return dp[n]

n, r = map(int, input().split())
print(( (factorial(n) * pow(factorial(r), mod-2, mod)) % mod) * pow(factorial(n-r), mod-2, mod) % mod)