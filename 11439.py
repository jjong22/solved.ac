import sys
input = sys.stdin.readline
print = sys.stdout.write

global mod

max_n = 4000000  # 필요한 최대 n값
factorial_dp = [1] * (max_n + 1)
n, k, mod = map(int, input().split())

for i in range(1, max_n + 1):
    factorial_dp[i] = (factorial_dp[i - 1] * i) % mod  # 필요하면 % mod 추가
    if factorial_dp[i] == 0:
        factorial_dp[i] = mod

def factorial(n):
    return factorial_dp[n]

def binomial(n, k):
    return ((factorial(n) // factorial(k) % mod) // factorial(n - k)) % mod

print(str(binomial(n, k)) + '\n')