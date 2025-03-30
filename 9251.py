str1 = input()
str2 = input()

dp = [0] * (len(str1) + 1)

for i in range(1, len(str2) + 1):
    prev = 0
    for j in range(1, len(str1) + 1):
        tmp = dp[j]
        if str2[i-1] == str1[j-1]:
            dp[j] = prev + 1
        else:
            dp[j] = max(dp[j], dp[j-1])
        prev = tmp
         
print(dp[-1])