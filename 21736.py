import sys
sys.setrecursionlimit(10**6) # 최대한 재귀 없이 stack 구현하는게 좋긴 하다!

n, m = map(int, input().split())
x_start, y_start = 0, 0
global result
result = 0

graph_map = [ [" " for i in range(m)] for j in range(n) ]

for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == "I":
            x_start, y_start = i, j
        graph_map[i][j] = (line[j]) # 1 or 0

visited = [ [False for i in range(m)] for j in range(n) ]

def DFS(i, j, visited):
    global result
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[i][j] = True
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x >= 0 and x < n and y >= 0 and y < m:
            if graph_map[x][y] != 'X' and not visited[x][y]:
                if graph_map[x][y] == 'P':
                    result += 1
                DFS(x, y, visited)
      
DFS(x_start, y_start, visited)
if result == 0:
    print("TT")
else:
    print(result)