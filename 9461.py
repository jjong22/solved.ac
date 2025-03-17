"""
def padovan(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return padovan(n-2) + padovan(n-3)
    
cnt = int(input())
for i in range(cnt):
    n = int(input())
    print(padovan(n))
"""
    
# with dp

def padovan(n):
    f_data = [1 if i <= 2 else 0 for i in range(n + 1)]

    last_pos = 2
    if(f_data[n-1] == 0):
        for i in range(last_pos + 1, n + 1):
            f_data[i] = (f_data[i - 2] + f_data[i - 3])
        last_pos = n - 1
    return f_data[n-1]

cnt = int(input())
for i in range(cnt):
    n = int(input())
    print(padovan(n))