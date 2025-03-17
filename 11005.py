N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    s += str(arr[N%B])
    N //= B

print(s[::-1])

# 진법의 의미....
# 모듈러를 생각하자.