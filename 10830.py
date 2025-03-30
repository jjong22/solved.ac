# matrix mul with divide and conquer

def matadd(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

def matsub(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]


def matmul(X, Y): # for n x n matrices
    if len(X) == 1 :
        return [[X[0][0] * Y[0][0] % 1000 ]]
    
    n = len(X)
    m = len(X) // 2
    
    
    A = [row[:m] for row in X[:m]]
    B = [row[m:] for row in X[:m]]
    C = [row[:m] for row in X[m:]]
    D = [row[m:] for row in X[m:]]
    
    E = [row[:m] for row in Y[:m]]
    F = [row[m:] for row in Y[:m]]
    G = [row[:m] for row in Y[m:]]
    H = [row[m:] for row in Y[m:]]
    
    
    P1 = matmul(A, matsub(F, H)) 
    P2 = matmul(matadd(A, B), H)
    P3 = matmul(matadd(C, D), E)
    P4 = matmul(D, matsub(G, E))
    P5 = matmul(matadd(A, D), matadd(E, H))
    P6 = matmul(matsub(B, D), matadd(G, H))
    P7 = matmul(matsub(A, C), matadd(E, F))
    
    xy1 = matadd(matadd(P5, P4), matsub(P6, P2))
    xy2 = matadd(P1, P2)
    xy3 = matadd(P3, P4)
    xy4 = matsub(matadd(P1, P5), matadd(P3, P7))
    
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        for j in range(m):
            result[i][j] = xy1[i][j]
            result[i][j+m] = xy2[i][j]
            result[i+m][j] = xy3[i][j]
            result[i+m][j+m] = xy4[i][j]
            
    return result

def next_power_of_2(n):
    power = 1
    while power < n:
        power *= 2
    return power

def pad_matrix(M, size):
    n = len(M)
    padded = [row + [0]*(size - n) for row in M]
    for _ in range(size - n):
        padded.append([0]*size)
    return padded

def trim_matrix(M, n):
    return [row[:n] for row in M[:n]]

def matrix_multiplication(X, Y):
    n = len(X)
    m = next_power_of_2(n)
    if m != n:
        X_padded = pad_matrix(X, m)
        Y_padded = pad_matrix(Y, m)
        result_padded = matmul(X_padded, Y_padded)
        return trim_matrix(result_padded, n)
    else:
        return matmul(X, Y)
    
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

bin_b = bin(b)[2:]
squ_matrix = [A]
result = identity_matrix(n)

for _ in range(len(bin_b) - 1):
    A = matrix_multiplication(A, A)
    squ_matrix.append(A)

for i in range(len(bin_b)):
    if bin_b[-1 - i] == '1':
        if i == 0:
            result = squ_matrix[i]
        else:
            result = matrix_multiplication(result, squ_matrix[i])
            
for row in result:
    print(*[x % 1000 for x in row])
    
