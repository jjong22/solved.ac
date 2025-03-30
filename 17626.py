n = int(input())
dp = [50000] * (n + 1)
dp[0] = 0

squres = [i * i for i in range(1, int(n ** 0.5) + 1)]

for s in squres:
    for i in range(s, n + 1):
        dp[i] = min(dp[i], dp[i - s] + 1)
        
print(dp[n])