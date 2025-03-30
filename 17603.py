# a0 = b0 * b1 mod p
# a1 = b0 + b1 mod p
# x^2 - a1x + a0 = 0

# https://ssongkit.tistory.com/436?category=1124259
def tonelli_shanks(n, p):
    def isQR(x, p):
        return pow(x, (p-1)//2, p) == 1
    if not isQR(n, p):
        return -1
    Q, S = p-1, 0
    while Q % 2 == 0:
        S += 1
        Q //= 2
    z = None
    for x in range(2, p):
        if not isQR(x, p):
            z = x
            break
    M, c, t, R = S, pow(z, Q, p), pow(n, Q, p), pow(n, (Q+1)//2, p)
    while True:
        if t == 0:
            return 0
        elif t == 1:
            return R
        k = t*t % p
        ii = None
        for i in range(1, M):
            if k == 1:
                ii = i
                break
            k *= k
            k %= p
        b = pow(c, 2**(M-i-1), p) % p
        M = ii % p
        c = b*b % p
        t = t*c % p
        R = R*b % p

n = int(input())
for _ in range(n):
    p, a0, a1 = map(int, input().split())
    
    if p == 2:
        if a0 == 0 and a1 == 0:
            print(0, 0)
        elif a0 == 0 and a1 == 1:
            print(0, 1)  # 또는 (1, 0)
        elif a0 == 1 and a1 == 0:
            print(1, 1)
        else:
            print(-1)
        continue
        
    delta = (a1 * a1 - 4 * a0) % p # modular 방정식에서의 판별식
    if delta == 0:
        x = a1 * pow(2, -1, p) % p
        print(x, x)
        continue
    else :
        r = tonelli_shanks(delta, p) # quadratic residue
        
    if r == -1:
        print(-1)
        continue
    
    x1 = (a1 + r) * pow(2, -1, p) % p
    x2 = (a1 - r) * pow(2, -1, p) % p
    
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)