dp_fibonacci = {}
dp_is_negative = {}
mod = 1000000000

def precompute_fibonacci(n):
    dp_fibonacci[-2] = -1
    dp_fibonacci[-1] = 1
    dp_fibonacci[0] = 0
    dp_fibonacci[1] = 1
    
    dp_is_negative[-2] = True
    dp_is_negative[-1] = False
    dp_is_negative[0] = False
    dp_is_negative[1] = False
    
    for i in range(2, n+1):
        dp_fibonacci[i] = (dp_fibonacci[i-1] + dp_fibonacci[i-2]) % mod
        dp_is_negative[i] = False
        
    for i in range(-2, -n-1, -1):
        dp_fibonacci[i] = (dp_fibonacci[i+2] - dp_fibonacci[i+1]) % mod
        dp_is_negative[i] = not (dp_is_negative[i+1])

precompute_fibonacci(1000000)

n = int(input())
if n == 0:
    print(0)
    print(0)
elif dp_is_negative[n]:
    print(-1)
    print(abs(dp_fibonacci[n] - mod))
else:
    print(1)
    print(dp_fibonacci[n])