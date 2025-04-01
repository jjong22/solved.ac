import sys
input = sys.stdin.readline
print = sys.stdout.write

def div_matrix(M):
    n = len(M)
    m = n // 2
    
    A = [row[:m] for row in M[:m]]
    B = [row[m:] for row in M[:m]]
    C = [row[:m] for row in M[m:]]
    D = [row[m:] for row in M[m:]]
    
    return A, B, C, D

def count_01_in_matrix(M):
    n = len(M)
    only_0 = True
    only_1 = True
    
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                only_1 = False
            else:
                only_0 = False
    return only_0, only_1

# zero is white, one is blue

def calculate_white_blue(M):
    only_0, only_1 = count_01_in_matrix(M)
    
    if only_0:
        return 1, 0
    elif only_1:
        return 0, 1
    
    A, B, C, D = div_matrix(M)
    
    x1, y1 = calculate_white_blue(A)
    x2, y2 = calculate_white_blue(B)
    x3, y3 = calculate_white_blue(C)
    x4, y4 = calculate_white_blue(D)
    
    return x1 + x2 + x3 + x4, y1 + y2 + y3 + y4

n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]

white, blue = calculate_white_blue(M)
print(str(white) + '\n')
print(str(blue) + '\n')