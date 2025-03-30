import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

m, n = map(int, input().split())

graph_map = [ [0 for i in range(m)] for j in range(n) ]
tomato = deque() # much faster for pop(0) than list

for i in range(n):
    line = input().split()
    for j in range(m):
        graph_map[i][j] = int(line[j]) # 1 or 0
        if graph_map[i][j] == 1:
            tomato.append((i, j))

visited = [ [False for i in range(m)] for j in range(n) ]
max_days = []

def BFS(G, S):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = S
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if G[nx][ny] == 0 and not visited[nx][ny]:
                        G[nx][ny] = 1
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    return days
    
days = BFS(graph_map, tomato)
    
for line in graph_map:
    if 0 in line:
        print("-1")
        exit()

print(str(days))