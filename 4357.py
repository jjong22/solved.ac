# https://gist.github.com/0xTowel/b4e7233fc86d8bb49698e4f1318a5a73
from math import ceil, sqrt


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None

import sys

for line in sys.stdin:
    p, b, n = map(int, line.split())

    # b ^ l = n (mod p)
    # b ^ p-1 = 1 mod p

    if n == 1:
        l = 0
    elif n == b:
        l = 1
    else :
        l = bsgs(b, n, p)
        
    if l is None:
        print('no solution')
    else:
        print(l)  