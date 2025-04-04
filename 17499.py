n, q = map(int, input().split())

numlist = list(map(int, input().split()))
ptr = 0
        
def print_all_num(numlist, ptr, n):
    for i in range(n):
        print(numlist[(ptr + i) % n], end = " ")  

for i in range(q):
    line = list(map(int, input().split()))
    if len(line) == 2:
        oper, shift = line[0], line[1]
        if oper == 2:
            ptr = (ptr - shift) % n
        if oper == 3:
            ptr = (ptr + shift) % n
            
    if len(line) == 3:
        _, idx, val = line[0], line[1], line[2]
        idx = idx - 1
        numlist[(ptr + idx) % n] += val
        
print_all_num(numlist, ptr, n)
      
