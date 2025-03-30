import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

m, n, h = map(int, input().split())

graph_map = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
tomato = deque()

for k in range(h):
    for i in range(n):
        line = input().split()
        for j in range(m):
            graph_map[k][i][j] = int(line[j])
            if graph_map[k][i][j] == 1:
                tomato.append((k, i, j))  # (z, x, y) 순서로 저장

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

def BFS(G, S):
    dz = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]

    queue = S
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            z, x, y = queue.popleft()  # (h, n, m) 순서로 꺼냄
            for k in range(6):
                nz = z + dz[k]
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                    if G[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
                        G[nz][nx][ny] = 1
                        visited[nz][nx][ny] = True
                        queue.append((nz, nx, ny))  # (h, n, m) 순서 유지 필요

    return days

days = BFS(graph_map, tomato)

for k in range(h):
    for i in range(n):
        if 0 in graph_map[k][i]:
            print("-1\n")
            exit()

print(f"{days}\n")
