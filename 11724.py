def BFS_map(graph, start):
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        start = queue.pop(0)
        for i in range(n):
            if graph[start][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                    
n, m = map(int, input().split())
graph = [ [0 for j in range(n)] for i in range(n)]
visited = [ 0 for i in range(n)]
num_connected = 0

for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a][b] = 1
    graph[b][a] = 1
    
for i in range(n):
    if visited[i] == 0:
        BFS_map(graph, i)
        num_connected += 1
        
print(num_connected)