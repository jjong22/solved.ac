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

mod = pow(10, 9)
n = int(input())

for i in range(n):
    x = int(input())
    print(recursive_fib(x, mod))