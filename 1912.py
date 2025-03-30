n = int(input())

mylist = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = mylist[i]
    if i > 0:
        dp[i] = max(dp[i], dp[i-1] + mylist[i])
        
print(max(dp))
