# Fm+n = Fm-1 * Fn + Fm * Fn+1
# F2n-1 = Fn * Fn + F(n-1) * F(n-1)
# F2n = (Fn+1 + Fn-1)(Fn+1 - Fn-1)
# ...
# sum(Fk) = Fn+2 - 1
# sum(F2k) = F2n+1 - 1
# sum(F2k-1) = F2n -1

# https://blog.naver.com/skh8464/220927977692
import math

def recursive_fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2 :
        return 1
    elif n == 3:
        return 2
    elif n % 2 == 0: # even
        m = n // 2
        f_np = recursive_fib(m+1)
        f_nm = recursive_fib(m-1)
        memo[n] = ((f_np + f_nm) * (f_np - f_nm))
    else: # odd
        m = n // 2
        f_n = recursive_fib(m)
        f_np = recursive_fib(m+1)
        memo[n] = (f_n * f_n + f_np * f_np)
    return memo[n]

n = int(input())

for i in range(n):
    p, q = map(int, input().split())
    value = recursive_fib(p)
    print(f"Case #{i+1}: {value % q}")