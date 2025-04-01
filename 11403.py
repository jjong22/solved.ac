import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

adj_matrix = [list(map(int, input().split())) for _ in range(n)]
d = [[float("Inf")] * n for _ in range(n)]
# Inf는 연결이 없음을 의미
        
for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] == 1:
            d[i][j] = 1
        
def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
floyd_warshall()
        
for i in range(n):
    for j in range(n):
        if d[i][j] != float("Inf"):
            print("1 ")
        else:
            print("0 ")
    print("\n")