import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
d = [[float("Inf")] * n for _ in range(n)]
# Inf는 연결이 없음을 의미

for i in range(m):
    a, b, c = map(int, input().split())   
    d[a-1][b-1] = min(d[a-1][b-1], c)
    
def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    d[i][j] = 0
                else:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
floyd_warshall()
        
for i in range(n):
    for j in range(n):
        if d[i][j] != float("Inf"):
            print(str(d[i][j]) + " ")
        else:
            print("0 ")
    print("\n")
    