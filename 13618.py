import math
import random
 
# Function to calculate (base^exponent)%modulus 
def modular_pow(base, exponent,modulus):
 
    # initialize result 
    result = 1
 
    while (exponent > 0):
     
        # if y is odd, multiply base with result 
        if (exponent & 1):
            result = (result * base) % modulus
 
        # exponent = exponent/2 
        exponent = exponent >> 1
 
        # base = base * base 
        base = (base * base) % modulus
     
    return result
 
# method to return prime divisor for n 
def PollardRho( n):
 
    # no prime divisor for 1 
    if (n == 1):
        return n
 
    # even number means one of the divisors is 2 
    if (n % 2 == 0):
        return 2
 
    # we will pick from the range [2, N) 
    x = (random.randint(0, 2) % (n - 2))
    y = x
 
    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite. 
    c = (random.randint(0, 1) % (n - 1))
 
    # Initialize candidate divisor (or result) 
    d = 1
 
    # until the prime factor isn't obtained.
    # If n is prime, return n 
    while (d == 1):
     
        # Tortoise Move: x(i+1) = f(x(i)) 
        x = (modular_pow(x, 2, n) + c + n)%n
 
        # Hare Move: y(i+1) = f(f(y(i))) 
        y = (modular_pow(y, 2, n) + c + n)%n
        y = (modular_pow(y, 2, n) + c + n)%n
 
        # check gcd of |x-y| and n 
        d = math.gcd(abs(x - y), n)
 
        # retry if the algorithm fails to find prime factor
        # with chosen x and c 
        if (d == n):
            return PollardRho(n)
     
    return d

n, e, c = map(int, input().split())

p = PollardRho(n)
q = n // p

phi = (p-1) * (q-1)
d = pow(e, -1, phi)

print(pow(c, d, n))