import math

n = int(input())
t_shirt = list(map(int, input().split()))
t_bundle, p_bundle = map(int, input().split())

t_num = 0
for num in t_shirt:
    t_num += math.ceil(num / t_bundle)
    
p1, p2 = n // p_bundle, n % p_bundle

print(t_num)
print(p1, p2)