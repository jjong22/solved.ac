n, a = map(int, input().split())

inv_add = -a % n
try:
    inv_mul = pow(a, -1, n)
except:
    inv_mul = -1

print(inv_add, inv_mul)