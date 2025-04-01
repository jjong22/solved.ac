a, b = map(int, input().split())
cnt = 0

while(1):
    if b % 10 == 1 and a * 10 < b: # 최솟값에 1을 더한 경우
        b -= 1
        b //= 10
        cnt += 1
    elif b % 2 == 0: # 최솟값에 2를 곱한 경우
        b //= 2
        cnt += 1
    else:
        print(-1)
        break
    
    if a == b:
        print(cnt + 1)
        break