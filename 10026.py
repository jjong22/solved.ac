import sys

n = int(input())

graph_map = [ [0 for i in range(n)] for j in range(n) ]

for i in range(n):
    line = input()
    for j in range(n):
        graph_map[i][j] = line[j]

num_of_connected_components = 0
visited = [ [False for i in range(n)] for j in range(n) ]
result_of_connected_components = []

def connected_components(graph, num_of_connected_components, result_of_connected_components, visited, target):
    for i in range(n):
        for j in range(n):
            result_of_DFS = []
            
            if graph_map[i][j] == target and not visited[i][j]:
                num_of_connected_components += 1
                DFS(i, j, visited, result_of_DFS, target)
                result_of_connected_components.append(result_of_DFS)
                
    return num_of_connected_components, result_of_connected_components

def connected_components_blind(graph, num_of_connected_components, result_of_connected_components, visited, target):
    for i in range(n):
        for j in range(n):
            result_of_DFS = []
            
            if target == "B":
                if graph_map[i][j] == target and not visited[i][j]:
                    num_of_connected_components += 1
                    DFS_blind(i, j, visited, result_of_DFS, target)
                    result_of_connected_components.append(result_of_DFS)
            else:
                if graph_map[i][j] != "B" and not visited[i][j]:
                    num_of_connected_components += 1
                    DFS_blind(i, j, visited, result_of_DFS, target)
                    result_of_connected_components.append(result_of_DFS)
                
    return num_of_connected_components, result_of_connected_components

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(i, j, visited, result_of_DFS, target):
    stack = [(i, j)]
    visited[i][j] = True
    
    while stack:
        x, y = stack.pop()
        result_of_DFS.append((x, y))
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph_map[nx][ny] == target and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

def DFS_blind(i, j, visited, result_of_DFS, target):
    stack = [(i, j)]
    visited[i][j] = True
    
    while stack:
        x, y = stack.pop()
        result_of_DFS.append((x, y))
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if target == "B":
                    if graph_map[nx][ny] == target and not visited[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    if graph_map[nx][ny] != "B" and not visited[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = True
            
            
num_r, result_of_connected_components = connected_components(graph_map, num_of_connected_components, result_of_connected_components, visited, "R")
num_g, result_of_connected_components = connected_components(graph_map, num_of_connected_components, result_of_connected_components, visited, "G")
num_b, result_of_connected_components = connected_components(graph_map, num_of_connected_components, result_of_connected_components, visited, "B")

sum_rgb_normal = num_r + num_g + num_b
visited = [ [False for i in range(n)] for j in range(n) ]

num_r, result_of_connected_components = connected_components_blind(graph_map, num_of_connected_components, result_of_connected_components, visited, "R")
num_g, result_of_connected_components = connected_components_blind(graph_map, num_of_connected_components, result_of_connected_components, visited, "G")
num_b, result_of_connected_components = connected_components_blind(graph_map, num_of_connected_components, result_of_connected_components, visited, "B")

sum_rgb_blind = num_r + num_g + num_b

print(str(sum_rgb_normal) + " " + str(sum_rgb_blind))