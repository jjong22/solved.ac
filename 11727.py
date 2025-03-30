n = int(input())
dp = [0] * (n + 1)

def tile(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if dp[n] != 0:
        return dp[n]
    dp[n] = (tile(n - 1) + 2 * tile(n - 2)) % 10007
    return dp[n]

print(tile(n))