def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    size = len(n)
    for i in range(size // 2): # meet in the middle
        if n[i] != n[size - i - 1]:
            return False
    return True

n = int(input())

while True:
    if is_palindrome(str(n)) and isprime(n):
        print(n)
        break
    n += 1