s = int(input())

n = 0
cnt = 1

while(1):
    n += cnt
    s -= cnt
    if cnt >= s:
        break
    cnt += 1
    
print(cnt)