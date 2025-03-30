import sys
input = sys.stdin.readline
print = sys.stdout.write

global mod
mod = 1000000007

max_n = 4000000  # 필요한 최대 n값
factorial_dp = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    factorial_dp[i] = (factorial_dp[i - 1] * i) % mod  # 필요하면 % mod 추가

def factorial(n):
    return factorial_dp[n]

def binomial(n, k):
    return ((factorial(n) * pow(factorial(k), -1, mod)) % mod) * pow(factorial(n - k), -1, mod) % mod

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(str(binomial(n, k)) + '\n')
    
