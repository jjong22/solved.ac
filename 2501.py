n, m = map(int, input().split())
cnt = 1
num_of_div = 0

while(1):
    if (n % cnt == 0):
        num_of_div += 1
    
    if (num_of_div == m):
        print(cnt)
        break
    
    if (cnt == n):
        print(0)
        break
    
    cnt += 1