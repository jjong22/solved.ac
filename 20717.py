v, x, m = map(int, input().split())

for i in range(1, m):
    p = i 
    try : 
        q = pow(v, -1, m) * p % m
        assert x <= p / q  and p / q < x + 1
    except :
        continue
    
    print(p, q)
    exit()
    
print(-1)