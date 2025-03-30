def recursive_fib(n, modulo, memo = {}):
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
        f_np = recursive_fib(m+1, modulo)
        f_nm = recursive_fib(m-1, modulo)
        memo[n] = ((f_np + f_nm) * (f_np - f_nm)) % modulo
    else: # odd
        m = n // 2
        f_n = recursive_fib(m, modulo)
        f_np = recursive_fib(m+1, modulo)
        memo[n] = (f_n * f_n + f_np * f_np) % modulo
    return memo[n]

def gcd_for_fibonacci(a, b, mod):
    if b == 0:
        return recursive_fib(a, mod)
    return gcd_for_fibonacci(b, a % b, mod)

# 11238.py
cnt = int(input())
for _ in range(cnt):
    n, m = map(int, input().split())
    print(gcd_for_fibonacci(n, m, 1000000007))

# 11778.py
# n, m = map(int, input().split())
# print(gcd_for_fibonacci(n, m, 1000000007))