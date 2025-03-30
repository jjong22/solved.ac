n = int(input())

graph_map = [ [0 for i in range(n)] for j in range(n) ]

for i in range(n):
    line = input()
    for j in range(n):
        graph_map[i][j] = int(line[j]) # 1 or 0

num_of_connected_components = 0
visited = [ [False for i in range(n)] for j in range(n) ]
result_of_connected_components = []
result_of_DFS = []

def connected_components(graph, num_of_connected_components, result_of_connected_components, visited):
    for i in range(n):
        for j in range(n):
            result_of_DFS = []
            
            if graph_map[i][j] == 1 and not visited[i][j]:
                num_of_connected_components += 1
                DFS(i, j, visited, result_of_DFS)
                result_of_connected_components.append(result_of_DFS)
                
    return num_of_connected_components, result_of_connected_components

def DFS(i, j, visited, result_of_DFS):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited[i][j] = True
    result_of_DFS.append((i, j))
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x >= 0 and x < n and y >= 0 and y < n:
            if graph_map[x][y] == 1 and not visited[x][y]:
                DFS(x, y, visited, result_of_DFS)
            
            
num_of_connected_components, result_of_connected_components = connected_components(graph_map, num_of_connected_components, result_of_connected_components, visited)

print(num_of_connected_components)
result_of_connected_components.sort(key=lambda x: len(x))
for i in result_of_connected_components:
    print(len(i))

